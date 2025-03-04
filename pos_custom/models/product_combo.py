from odoo import models, fields

class ProductsCombo(models.Model):
    _name = 'product.combo'
    _description = 'Product Combo'

    combo_name = fields.Char(string='Combo Name')
    combo_id = fields.Many2one('product.template',string='Combo ID')

