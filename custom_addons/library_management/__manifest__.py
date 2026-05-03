# -*- coding: utf-8 -*-
{
    'name': 'Library Management',
    'summary': 'Manage books and loans for a library',
    'description': """
        Library Management Module
        =========================
        A custom Odoo module to manage:
        - Library Books (with status tracking)
        - Book Loans (borrow / return workflow)

        Two security groups are defined:
        - Library User   : read books, create own loan requests
        - Library Manager: full CRUD on books and loans
    """,
    'author': 'My Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Library',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',

    # Dependencies
    'depends': ['base'],

    # Data files loaded in this order
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_loan_views.xml',
        'views/menus.xml',
    ],

    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
