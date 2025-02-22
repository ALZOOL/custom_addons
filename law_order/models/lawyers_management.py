from odoo import models, fields


class lawyersManagement(models.Model):
    _name = 'lawyers'
    _description = 'Lawyers Management'


    lawyer_id = fields.Many2one('res.users', string='Lawyer')
    price = fields.Monetary(currency_field='currency_id', string='Price')
    currency_id = fields.Many2one('res.currency', string='Currency', related='company_id.currency_id')
    company_id = fields.Many2one('res.company', string='Company', related='lawyer_id.company_id')

    def action_open_change_state_wizard(self):
        action = self.env['ir.actions.actions']._for_xml_id('law_order.change_state_wizard_action')
        action['context'] = {'default_lawyers_id': self.id}
        return action










    # name = fields.Char(string='Name')
    #new_field = fields.Char(string='New Field')
    #customer_id = fields.Many2one('customers',string='Customer Many2one')
    # customer_ids = fields.Many2many('customers',string='Customer Many2many')
    # customer_idss = fields.One2many('customers',string='Customer One2many') in one2many we must create another link on other model we want to make it realated to


