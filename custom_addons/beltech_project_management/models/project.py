from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class BeltechProject(models.Model):
    _name = 'beltech.project'
    _description = 'BelTech Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'sequence, id'

    name = fields.Char(string='Project Name', required=True, tracking=True)
    code = fields.Char(string='Project Code', readonly=True, copy=False, default=lambda self: _('New'))
    sequence = fields.Integer(default=10)
    color = fields.Integer(string='Color Index')
    
    manager_id = fields.Many2one('res.users', string='Project Manager', tracking=True, default=lambda self: self.env.user)
    budget = fields.Float(string='Budget', tracking=True)
    deadline = fields.Date(string='Deadline', tracking=True)
    
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)
    
    description = fields.Text(string='Description')
    
    # Relationships
    task_ids = fields.One2many('beltech.project.task', 'project_id', string='Tasks')
    task_count = fields.Integer(compute='_compute_task_count', string='Task Count')
    
    # Computed Fields
    progress = fields.Float(compute='_compute_progress', string='Progress (%)', store=True)

    @api.depends('task_ids', 'task_ids.status')
    def _compute_progress(self):
        for record in self:
            if not record.task_ids:
                record.progress = 0.0
            else:
                completed_tasks = len(record.task_ids.filtered(lambda t: t.status == 'done'))
                record.progress = (completed_tasks / len(record.task_ids)) * 100

    def _compute_task_count(self):
        for record in self:
            record.task_count = len(record.task_ids)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('code', _('New')) == _('New'):
                vals['code'] = self.env['ir.sequence'].next_by_code('beltech.project') or _('New')
        return super().create(vals_list)

    @api.constrains('budget')
    def _check_budget(self):
        for record in self:
            if record.budget < 0:
                raise ValidationError(_("The project budget cannot be negative."))

    # Actions
    def action_in_progress(self):
        self.status = 'in_progress'

    def action_completed(self):
        self.status = 'completed'

    def action_cancelled(self):
        self.status = 'cancelled'

    def action_draft(self):
        self.status = 'draft'

class BeltechProjectTask(models.Model):
    _name = 'beltech.project.task'
    _description = 'BelTech Project Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Task Title', required=True, tracking=True)
    project_id = fields.Many2one('beltech.project', string='Project', ondelete='cascade')
    assigned_to = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user)
    deadline = fields.Date(string='Deadline')
    
    status = fields.Selection([
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='todo', tracking=True)
    
    description = fields.Text(string='Description')
