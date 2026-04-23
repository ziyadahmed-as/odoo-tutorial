from odoo import http

class MyWebsite(http.Controller):

    @http.route('/my-page', type='http', auth='public', website=True)
    def my_page(self):
        return http.request.render('my_website_custom.my_page_template')