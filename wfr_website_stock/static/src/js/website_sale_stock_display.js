odoo.define('wfr_website_stock.load', function (require) {
    'use strict';
    var ajax = require('web.ajax');
    var core = require('web.core');
    var QWeb = core.qweb;
    
    ajax.loadXML(
        '/wfr_website_stock/static/src/xml/website_sale_stock_display.xml',
         QWeb
    ).then(function() {
        $('.oe_website_sale').find('input[name="add_qty"]').trigger('change');
    });
});
