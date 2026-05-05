from odoo import models, fields, api

class EducationCourse(models.Model):
    _name = 'education.course'
    _description = 'Educational Course'
    _inherit = ['website.published.mixin']

    name = fields.Char(string='Course Title', required=True)
    description = fields.Html(string='Description')
    level = fields.Selection([
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ], string='Level', default='beginner')
    requirements = fields.Text(string='Requirements')
    instructor_id = fields.Many2one('education.instructor', string='Instructor')
    image = fields.Binary(string='Course Cover')
    price = fields.Float(string='Price', default=0.0)
    duration = fields.Char(string='Duration (e.g. 10 hours)')
    active = fields.Boolean(default=True)
    enrollment_ids = fields.One2many('education.enrollment', 'course_id', string='Enrollments')
    student_ids = fields.Many2many('res.users', string='Students', compute='_compute_student_ids', store=True)

    @api.depends('enrollment_ids.student_id')
    def _compute_student_ids(self):
        for course in self:
            course.student_ids = course.enrollment_ids.mapped('student_id')

    def _compute_website_url(self):
        super(EducationCourse, self)._compute_website_url()
        for course in self:
            course.website_url = "/course/%s" % course.id
