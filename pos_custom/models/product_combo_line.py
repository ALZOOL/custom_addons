from odoo import models, fields

class ProductComboLine(models.Model):
    _name = 'product.combo.line'
    _description = 'Product Combo Line'

    combo_line_name = fields.Char(string='Product', required='True')
    combo_line_id = fields.Many2one('product.combo', string='Product Name')
    combo_line_required = fields.Boolean(string='Required', default=True)
    combo_line_max_item = fields.Integer(string='Max Items')
    combo_line_min_item = fields.Integer(string='Min Items')
    line_extra_price = fields.Float(string='Extra Proce')
