# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
from odoo.exceptions import UserError

class SupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'

    x_studio_duty = fields.Float(string='Duty/Brokerage %', digits=(12, 2))
    x_studio_freight = fields.Float(string='Freight %', digits=(12, 2))
    x_studio_estimated_landed_cost = fields.Float(string='Estimated Landed Cost', compute='_compute_estimated_landed_cost')
    currency_rate = fields.Float(string='Currency Rate', related='currency_id.rate')

    @api.depends('price', 'x_studio_duty', 'x_studio_freight', 'currency_rate')
    def _compute_estimated_landed_cost(self):
        for record in self:
            try:
                record.x_studio_estimated_landed_cost = record.price / record.currency_rate * record.x_studio_duty * record.x_studio_freight
            except:
                record.x_studio_estimated_landed_cost = record.x_studio_estimated_landed_cost or 0.0

    def _overwrite_product_cost(self):
        if self.env.user.has_group('purchase.group_purchase_manager'):
            if len(set([record.name for record in self])) == 1:
                for record in self:
                    if record.product_id:
                        record.product_id.standard_price = record.product_id.standard_price + record.x_studio_estimated_landed_cost
                    else:
                        record.product_tmpl_id.standard_price = record.product_tmpl_id.standard_price + record.x_studio_estimated_landed_cost
            else:
                raise UserError(_("Cannot overwrite costs for multiple vendors at the same time."))
        else:
            raise UserError(_("Only managers can overwrite product costs."))
