from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class BeltechProject(models.Model):
    _name = 'beltech.project'
    _description = 'BelTech Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Project Name', required=True, tracking=True)
    color = fields.Integer(string='Color Index')
    manager_id = fields.Many2one('res.users', string='Project Manager', required=True, tracking=True, default=lambda self: self.env.user)
    budget = fields.Float(string='Budget', required=True, tracking=True)
    deadline = fields.Date(string='Deadline', required=True, tracking=True)
    department_id = fields.Many2one('hr.department', string='Department', tracking=True)
    description = fields.Html(string='Description')
    
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True)

    progress = fields.Integer(string='Progress (%)', compute='_compute_progress', store=True)
    task_ids = fields.One2many('beltech.project.task', 'project_id', string='Tasks')
    task_count = fields.Integer(string='Task Count', compute='_compute_task_count')

    @api.depends('task_ids')
    def _compute_task_count(self):
        for record in self:
            record.task_count = len(record.task_ids)

    @api.depends('status')
    def _compute_progress(self):
        for record in self:
            if record.status == 'draft':
                record.progress = 0
            elif record.status == 'in_progress':
                record.progress = 50
            elif record.status == 'completed':
                record.progress = 100
            else:
                record.progress = 0

    @api.constrains('budget')
    def _check_budget(self):
        for record in self:
            if record.budget <= 0:
                raise ValidationError(_("The budget must be a positive value."))

    def action_in_progress(self):
        self.status = 'in_progress'

    def action_done(self):
        self.status = 'completed'

    def action_cancel(self):
        self.status = 'cancelled'

    def action_draft(self):
        self.status = 'draft'

class BeltechProjectTask(models.Model):
    _name = 'beltech.project.task'
    _description = 'Project Task'

    name = fields.Char(string='Task Name', required=True)
    project_id = fields.Many2one('beltech.project', string='Project', ondelete='cascade')
    assigned_to = fields.Many2one('res.users', string='Assigned To')
    deadline = fields.Date(string='Deadline')
    status = fields.Selection([
        ('todo', 'To Do'),
        ('done', 'Done')
    ], default='todo')
