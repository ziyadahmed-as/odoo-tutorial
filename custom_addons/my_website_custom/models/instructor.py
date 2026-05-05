from odoo import models, fields

class EducationInstructor(models.Model):
    _name = 'education.instructor'
    _description = 'Educational Instructor'

    name = fields.Char(string='Name', required=True)
    bio = fields.Text(string='Biography')
    image = fields.Binary(string='Image')
    course_ids = fields.One2many('education.course', 'instructor_id', string='Courses')
    social_twitter = fields.Char(string='Twitter')
    social_linkedin = fields.Char(string='LinkedIn')
