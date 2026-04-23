from odoo import http
from odoo.http import request

class EducationWebsite(http.Controller):

    @http.route('/courses', type='http', auth='public', website=True)
    def courses_list(self, **kwargs):
        courses = request.env['education.course'].search([('website_published', '=', True)])
        return request.render('my_website_custom.courses_list_template', {
            'courses': courses,
        })

    @http.route('/course/<model("education.course"):course>', type='http', auth='public', website=True)
    def course_detail(self, course, **kwargs):
        return request.render('my_website_custom.course_detail_template', {
            'course': course,
        })

    @http.route('/instructors', type='http', auth='public', website=True)
    def instructors_list(self, **kwargs):
        instructors = request.env['education.instructor'].search([])
        return request.render('my_website_custom.instructors_list_template', {
            'instructors': instructors,
        })