from odoo import models, fields, api


class testPartnersManagement(models.Model):
    _name = 'test_partners'
    _description = 'Test Partners Management'

    part_id = fields.Many2one('res.partner', string='Partner')


