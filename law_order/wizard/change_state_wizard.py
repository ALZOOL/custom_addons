from odoo import fields, models


class ChangeState(models.TransientModel):
    _name = 'change.state'

    lawyer_id = fields.Many2one('lawyers')
    state = fields.Selection([
            ('draft', 'Draft'),
            ('pending', 'Pending'),
    ], default='draft')
    reason = fields.Char()

    def action_confirm(self):
        print("inside confirm action")