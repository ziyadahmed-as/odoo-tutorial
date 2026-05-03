# -*- coding: utf-8 -*-
from odoo import models, fields

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Book Loan'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner/User', required=True)
    loan_date = fields.Date(string='Loan Date', default=fields.Date.today)
    return_date = fields.Date(string='Return Date')
