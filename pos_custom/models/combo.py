from odoo import models, fields

class Combo(models.Model):
    _inherit = 'product.template'

    combo_active = fields.Boolean(string="is Combo", default=True)
    combo_ids = fields.One2many('product.combo','combo_id', string='Combo ids')

