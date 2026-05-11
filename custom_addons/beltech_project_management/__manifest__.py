{
    'name': 'BelTech Project Management',
    'version': '1.0',
    'summary': 'Manage projects, budgets, and managers for BelTech Solutions.',
    'description': """
        A custom Odoo module for BelTech Solutions to manage:
        - Project tracking and statuses
        - Budget management
        - Manager assignments
        - Deadlines and departments
    """,
    'author': 'Ziyad Ahmed',
    'category': 'Project Management',
    'depends': ['base', 'mail', 'hr'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/project_data.xml',
        'views/project_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
