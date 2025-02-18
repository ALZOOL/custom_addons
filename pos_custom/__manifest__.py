# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'postest',
    'category': 'Accounting/Accounting',
    'summary': 'Manage POS and customers',
    'version': '1.0',
    'depends': ['base','point_of_sale'],
    'data': [
        'views/postest_views.xml',
        'views/custom_session_views.xml',
        'reports/custom_session_report.xml',
        'wizard/change_state_wizard_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
