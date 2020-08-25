# -- coding: utf-8 --

from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    inventory_availability = fields.Selection(selection_add=[
        ('always_no_lock',
         'Sell regardless of inventory and show inventory on website'),
    ])