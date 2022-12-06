# -*- coding: utf-8 -*-
{
    'name': "Appraisal Report",
    'summary': """
        Appraisal report""",
    'author': "Nasreddin Omar",
    'website': "nasrom9@gmail.com",
    'category': 'Human Resources',
    'version': '1.0',
    'depends': ['base', 'ncss_appraisal'],
    'data': [
        'views/appraisal.xml',
        'report/appraisal_report.xml',
        'report/appraisal_report_template.xml',
    ],
    'installable': True,
    'application': False,
}
