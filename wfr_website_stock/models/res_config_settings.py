# -- coding: utf-8 --

from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    inventory_availability = fields.Selection(selection_add=[
        ('always_no_lock',
         'Sell regardless of inventory and show inventory on website'),
    ])
