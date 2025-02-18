from odoo import models, fields, api


class customersManagement(models.Model):
    _name = 'customers'
    _description = 'Customers Management'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age ')

    #lawyer_id = fields.One2many('lawyers') this is the link with other model for One2many realation
