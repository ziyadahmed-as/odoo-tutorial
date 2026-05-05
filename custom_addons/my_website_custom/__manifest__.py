{
    'name': 'My Website Custom',
    'version': '1.0',
    'summary': 'Educational Platform Customization',
    'description': 'Custom module for an educational organization website.',
    'category': 'Website',
    'author': 'Ziyad Ahmed',
    'depends': ['website', 'portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/course_templates.xml',
        'views/instructor_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'my_website_custom/static/src/css/style.css',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}