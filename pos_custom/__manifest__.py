# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'postest',
    'category': 'Accounting/Accounting',
    'summary': 'Manage POS and customers',
    'version': '1.0',
    'depends': ['base','point_of_sale'],
    'data': [
        'views/custom_session_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
