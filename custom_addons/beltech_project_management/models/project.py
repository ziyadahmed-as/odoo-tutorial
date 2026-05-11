from odoo import models, fields

class BeltechProject(models.Model):
    _name = 'beltech.project'
    _description = 'BelTech Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Project Name', required=True, tracking=True)
    manager_id = fields.Many2one('res.users', string='Project Manager', tracking=True)
    budget = fields.Float(string='Budget', tracking=True)
    deadline = fields.Date(string='Deadline', tracking=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)
    description = fields.Text(string='Description')

    def action_in_progress(self):
        self.status = 'in_progress'

    def action_completed(self):
        self.status = 'completed'

    def action_cancelled(self):
        self.status = 'cancelled'

    def action_draft(self):
        self.status = 'draft'
