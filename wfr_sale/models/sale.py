# -*- coding: utf-8 -*-

from odoo import models, api, _


def create_list_html(array):
    '''Convert an array of string to a html list.
        :param array: A list of strings
        :return: an empty string if not array, an html list otherwise.
    '''
    if not array:
        return ''
    msg = ''
    for item in array:
        msg += '<li>' + item + '</li>'
    return '<ul>' + msg + '</ul>'


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    def _recalculate_price(self):
        for order in self:
            if order.state not in ["done", "sale"] and order.order_line:
                tracking = []
                for line in order.order_line:
                    prev_price_unit = line.price_unit
                    line.product_id_change()
                    post_price_unit = line.price_unit
                    line_msg = _("[SOL{}] {} Unit Price {} <span>&#8594;</span> {}").format(line.id, line.product_id.name, prev_price_unit, post_price_unit)
                    tracking.append(line_msg)
                tracking_msg = _("Unit Price Recalculated:") + create_list_html(tracking)
                order.message_post(body=tracking_msg)
                
