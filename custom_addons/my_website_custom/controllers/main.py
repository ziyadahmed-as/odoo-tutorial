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
        is_enrolled = False
        if request.session.uid:
            is_enrolled = request.env['education.enrollment'].sudo().search_count([
                ('course_id', '=', course.id),
                ('student_id', '=', request.env.user.id)
            ]) > 0
        
        return request.render('my_website_custom.course_detail_template', {
            'course': course,
            'is_enrolled': is_enrolled,
        })

    @http.route('/course/enroll/<model("education.course"):course>', type='http', auth='user', website=True)
    def course_enroll(self, course, **kwargs):
        enrollment = request.env['education.enrollment'].sudo().search([
            ('course_id', '=', course.id),
            ('student_id', '=', request.env.user.id)
        ], limit=1)
        
        if not enrollment:
            request.env['education.enrollment'].sudo().create({
                'course_id': course.id,
                'student_id': request.env.user.id,
            })
            return request.redirect('/course/%s?enrolled=1' % course.id)
        
        return request.redirect('/course/%s' % course.id)

    @http.route('/instructors', type='http', auth='public', website=True)
    def instructors_list(self, **kwargs):
        instructors = request.env['education.instructor'].search([])
        return request.render('my_website_custom.instructors_list_template', {
            'instructors': instructors,
        })