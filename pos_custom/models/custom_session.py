from odoo import models

class PosSessionInherit(models.Model):
    _inherit = 'pos.session'

    def print_custom_session_report(self):
        return self.env.ref('pos_custom.custom_session_report_template').report_action(self)