# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Book Loan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'loan_date desc'

    # ── Relational Fields ─────────────────────────────────────────
    book_id = fields.Many2one(
        comodel_name='library.book',
        string='Book',
        required=True,
        ondelete='restrict',
        tracking=True,
        domain=[('status', '=', 'available')],
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Borrower',
        required=True,
        ondelete='restrict',
        tracking=True,
        default=lambda self: self.env.user.partner_id,
    )

    # ── Date Fields ───────────────────────────────────────────────
    loan_date = fields.Date(
        string='Loan Date',
        required=True,
        default=fields.Date.today,
        tracking=True,
    )
    return_date = fields.Date(
        string='Expected Return Date',
        tracking=True,
    )
    actual_return_date = fields.Date(
        string='Actual Return Date',
        readonly=True,
        copy=False,
    )

    # ── State ─────────────────────────────────────────────────────
    state = fields.Selection(
        selection=[
            ('draft',    'Draft'),
            ('active',   'Active / Borrowed'),
            ('returned', 'Returned'),
            ('overdue',  'Overdue'),
        ],
        string='State',
        default='draft',
        required=True,
        tracking=True,
        copy=False,
    )

    # ── Computed ──────────────────────────────────────────────────
    is_overdue = fields.Boolean(
        string='Is Overdue?',
        compute='_compute_is_overdue',
        store=True,
    )

    @api.depends('return_date', 'state')
    def _compute_is_overdue(self):
        today = fields.Date.today()
        for loan in self:
            loan.is_overdue = (
                loan.state == 'active'
                and bool(loan.return_date)
                and loan.return_date < today
            )

    # ── Constraints ───────────────────────────────────────────────
    @api.constrains('loan_date', 'return_date')
    def _check_dates(self):
        for loan in self:
            if loan.return_date and loan.loan_date > loan.return_date:
                raise ValidationError(
                    _('Return date must be after the loan date.')
                )

    # ── Workflow Actions ──────────────────────────────────────────
    def action_confirm(self):
        """Confirm the loan and mark the book as Borrowed."""
        for loan in self:
            if loan.state != 'draft':
                raise UserError(_('Only draft loans can be confirmed.'))
            if loan.book_id.status != 'available':
                raise UserError(
                    _('The book "%s" is not available.') % loan.book_id.title
                )
            loan.book_id.action_borrow()
            loan.state = 'active'

    def action_return_book(self):
        """Return the book and close the loan."""
        for loan in self:
            if loan.state not in ('active', 'overdue'):
                raise UserError(_('Only active or overdue loans can be returned.'))
            loan.book_id.action_return()
            loan.actual_return_date = fields.Date.today()
            loan.state = 'returned'

    def action_mark_overdue(self):
        """Manually flag a loan as overdue."""
        for loan in self:
            if loan.state == 'active':
                loan.state = 'overdue'

    def action_reset_draft(self):
        """Reset to draft (manager only)."""
        for loan in self:
            loan.state = 'draft'
