from odoo import fields, models


class ChangeState(models.TransientModel):
    _name = 'change.state'

    customer_id = fields.Many2one('postest')
    state = fields.Selection([
            ('draft', 'Draft'),
            ('pending', 'Pending'),
    ], default='draft')
    reason = fields.Char()

    def action_confirm(self):
        print("inside confirm action")