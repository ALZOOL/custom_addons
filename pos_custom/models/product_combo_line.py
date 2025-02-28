from odoo import models, fields

class ProductComboLine(models.Model):
    _name = 'product.combo.line'
    _description = 'Product Combo Line'

    combo_id = fields.Many2one('product.combo', string='Combo')
    accounting_info = fields.Char(string='Accounting')
    combo_info = fields.Char(string='Combo')
