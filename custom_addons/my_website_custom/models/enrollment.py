from odoo import models, fields, api

class EducationEnrollment(models.Model):
    _name = 'education.enrollment'
    _description = 'Course Enrollment'
    _order = 'enrollment_date desc'

    student_id = fields.Many2one('res.users', string='Student', required=True, default=lambda self: self.env.user)
    course_id = fields.Many2one('education.course', string='Course', required=True)
    enrollment_date = fields.Date(string='Enrollment Date', default=fields.Date.today())
    state = fields.Selection([
        ('draft', 'Draft'),
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='enrolled')

    _sql_constraints = [
        ('unique_student_course', 'unique(student_id, course_id)', 'The student is already enrolled in this course!')
    ]
