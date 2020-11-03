# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
from odoo.exceptions import UserError

class SupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'

    duty = fields.Float(string='Duty/Brokerage %', digits=(12, 2))
    freight = fields.Float(string='Freight %', digits=(12, 2))
    estimated_landed_cost = fields.Float(string='Estimated Landed Cost', compute='_compute_estimated_landed_cost')
    currency_rate = fields.Float(string='Currency Rate', related='currency_id.rate')

    @api.depends('price', 'duty', 'freight', 'currency_rate')
    def _compute_estimated_landed_cost(self):
        for record in self:
            try:
                record.estimated_landed_cost = record.price / record.currency_rate * record.duty * record.freight
            except:
                record.estimated_landed_cost = record.estimated_landed_cost or 0.0

    def _overwrite_product_cost(self):
        if self.env.user.has_group('purchase.group_purchase_manager'):
            for record in self:
                if record.product_id:
                    record.product_id.standard_price = record.estimated_landed_cost
                else:
                    record.product_tmpl_id.standard_price = record.estimated_landed_cost
        else:
            raise UserError(_("Only managers can overwrite product costs."))
