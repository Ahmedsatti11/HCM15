# -*- coding: utf-8 -*-
{
    'name': 'NCSS Appraisal',
    'version': '15.0.1',
    'summary': 'NCSS Appraisal',
    'category': 'hr',
    'author': 'Magdy,TeleNoc',
    'description': """
    NCSS Appraisal
    """,
    'depends': ['base', 'mail', 'hr_appraisal'],
    'demo': [
        'demo/demo.xml'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/hr_employee_appraisal.xml',
        'views/hr_appraisal.xml',
    ]
}
