from odoo import models, fields

class ProductComboLine(models.Model):
    _name = 'product.combo.line'
    _description = 'Product Combo Line'

    combo_line_id = fields.Many2one('product.combo', string='Product Name')
