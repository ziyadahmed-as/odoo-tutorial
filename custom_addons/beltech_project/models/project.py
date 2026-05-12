from odoo import models, fields

class BelTechProject(models.Model):
    _name = 'beltech.project'
    _description = 'BelTech Project'

    name = fields.Char(string='Project Title', required=True)
    description = fields.Text(string='Project Description')
    manager_id = fields.Many2one('res.users', string='Project Manager')
    budget = fields.Float(string='Budget')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
