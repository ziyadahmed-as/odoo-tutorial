{
    'name': "BelTech Project Management",
    'version': '1.0',
    'summary': "Simple internal system to manage projects, project managers, budgets, and statuses.",
    'description': """
        A custom Odoo module from scratch to understand the core foundations of Odoo development.
        Allows users to:
        - Create and manage projects
        - Assign project managers
        - Track project status
        - Store project budget information
        - View projects using list and form interfaces
    """,
    'author': "BelTech Solutions",
    'category': 'Project',
    'depends': ['base'],
    'data': [
        'security/project_security.xml',
        'security/ir.model.access.csv',
        'views/project_views.xml',
        'views/project_menus.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
