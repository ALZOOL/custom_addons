from odoo import models, fields

class ProductsCombo(models.Model):
    _inherit = 'product.template'

    combo_active = fields.Boolean(string="is Combo", default=True)


