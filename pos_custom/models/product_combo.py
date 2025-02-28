from odoo import models, fields

class ProductsCombo(models.Model):
    _name = 'product.combo'
    _description = "Point Of Sale Products Combos"

    name = fields.Char(string="Product Name", required=True)
    combo_active = fields.Boolean(string="is Combo", default=True)


