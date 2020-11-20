odoo.define('product_default_code.custom_product', function(require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.WebsiteSale.include({
        _onChangeCombination: function (ev, $parent, combination){
            var $default_code = $('.product_default_code');
            $default_code.text(combination.default_code);
            this._super.apply(this, arguments);
        }
    });
});
