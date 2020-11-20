# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request
from odoo.addons.sale.controllers.variant import VariantController

class VariantController(VariantController):

    @http.route()
    def get_combination_info(self, product_template_id, product_id, combination, add_qty, pricelist_id, **kw):
        res = super(VariantController, self).get_combination_info(product_template_id, product_id, combination, add_qty, pricelist_id, **kw)
        product = request.env['product.product'].browse(int(res.get('product_id')))
        res.update({
            'default_code': product.default_code
        })
        return res
