# from odoo import http


# class TempProject(http.Controller):
#     @http.route('/beltech_project/beltech_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/beltech_project/beltech_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('beltech_project.listing', {
#             'root': '/beltech_project/beltech_project',
#             'objects': http.request.env['beltech_project.beltech_project'].search([]),
#         })

#     @http.route('/beltech_project/beltech_project/objects/<model("beltech_project.beltech_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('beltech_project.object', {
#             'object': obj
#         })

