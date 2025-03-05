from odoo import models, fields

class ProductsCombo(models.Model):
    _name = 'product.combo'
    _description = 'Product Combo'

    combo_name = fields.Char(string='Name', required='True')
    combo_id = fields.Many2one('product.template',string='Combo ID')
    required = fields.Boolean(string='Required', default=True)
    max_item = fields.Integer(string='Max Items')
    combo_line_ids = fields.One2many('product.combo.line','combo_line_id', string='Product')


