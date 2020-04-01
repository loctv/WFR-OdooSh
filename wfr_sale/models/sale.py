# -*- coding: utf-8 -*-

from odoo import models, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _recalculate_price(self):
        for order in self:
            if order.state not in ["done", "sale"]:
                for line in order.order_line:
                    line.product_id_change()
