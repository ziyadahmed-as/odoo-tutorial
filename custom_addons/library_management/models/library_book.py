# -*- coding: utf-8 -*-
from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    isbn = fields.Char(string='ISBN')
    publication_date = fields.Date(string='Publication Date')
    genre = fields.Selection([
        ('Programming', 'Programming'),
        ('AI', 'AI'),
        ('Framwork', 'Framwork'),
        ('Networking', 'Networking'),
        ('Database', 'Database')
    ], string='Genre')
    status = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost')
    ], string='Status', default='available')

