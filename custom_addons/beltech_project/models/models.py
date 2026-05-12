# from odoo import models, fields, api


# class beltech_project(models.Model):
#     _name = 'beltech_project.beltech_project'
#     _description = 'beltech_project.beltech_project'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

