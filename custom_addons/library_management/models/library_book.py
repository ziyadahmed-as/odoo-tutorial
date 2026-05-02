# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'title asc'

    # ── Basic Fields ──────────────────────────────────────────────
    title = fields.Char(
        string='Title',
        required=True,
        tracking=True,
    )
    author = fields.Char(
        string='Author',
        required=True,
        tracking=True,
    )
    isbn = fields.Char(
        string='ISBN',
        copy=False,
    )
    publication_date = fields.Date(
        string='Publication Date',
    )
    genre = fields.Selection(
        selection=[
            ('fiction',     'Fiction'),
            ('non_fiction', 'Non-Fiction'),
            ('science',     'Science'),
            ('history',     'History'),
            ('biography',   'Biography'),
            ('children',    'Children'),
            ('other',       'Other'),
        ],
        string='Genre',
        default='other',
    )

    # ── Status ────────────────────────────────────────────────────
    status = fields.Selection(
        selection=[
            ('available', 'Available'),
            ('borrowed',  'Borrowed'),
            ('lost',      'Lost'),
        ],
        string='Status',
        default='available',
        required=True,
        tracking=True,
        copy=False,
    )

    # ── Computed ──────────────────────────────────────────────────
    loan_count = fields.Integer(
        string='Loan Count',
        compute='_compute_loan_count',
    )
    active_loan_id = fields.Many2one(
        comodel_name='library.loan',
        string='Active Loan',
        compute='_compute_active_loan',
    )

    # ── Compute Methods ───────────────────────────────────────────
    @api.depends('status')
    def _compute_loan_count(self):
        for book in self:
            book.loan_count = self.env['library.loan'].search_count(
                [('book_id', '=', book.id)]
            )

    @api.depends('status')
    def _compute_active_loan(self):
        for book in self:
            loan = self.env['library.loan'].search(
                [('book_id', '=', book.id), ('state', '=', 'active')],
                limit=1,
            )
            book.active_loan_id = loan

    # ── Status Action Buttons ─────────────────────────────────────
    def action_borrow(self):
        """Mark the book as Borrowed."""
        for book in self:
            if book.status != 'available':
                raise UserError(
                    _('Only available books can be borrowed. '
                      'Current status: %s') % book.status
                )
            book.status = 'borrowed'

    def action_return(self):
        """Mark the book as Available again."""
        for book in self:
            if book.status != 'borrowed':
                raise UserError(
                    _('Only borrowed books can be returned.')
                )
            book.status = 'available'

    def action_mark_lost(self):
        """Mark the book as Lost."""
        for book in self:
            book.status = 'lost'

    def action_view_loans(self):
        """Open all loans for this book."""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Loans for %s') % self.title,
            'res_model': 'library.loan',
            'view_mode': 'tree,form',
            'domain': [('book_id', '=', self.id)],
            'context': {'default_book_id': self.id},
        }
