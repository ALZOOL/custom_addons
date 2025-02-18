# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'law',
    'category': 'Accounting/Accounting',
    'summary': 'Manage lawyer and customers',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/lawyers_views.xml',
        'views/customers_views.xml',
        'reports/lawyer_report.xml',
        'wizard/change_state_wizard_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
