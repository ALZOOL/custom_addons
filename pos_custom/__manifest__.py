# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'postest',
    'category': 'Accounting/Accounting',
    'summary': 'Manage POS and customers',
    'version': '1.0',
    'depends': ['base','point_of_sale','product'],
    'data': [
        'views/custom_session_views.xml',
        'views/product_combo_views.xml',
        'reports/custom_session_report.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
