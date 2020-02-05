odoo.define('theme_laze.horizontal_slider', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
var VariantMixin = require('sale.VariantMixin');

VariantMixin._onChangeProductImage = function (ev) {
    $('.thumbnails-slides').not('.slick-initialized').slick({
        dots: false,
        infinite: false,
        speed: 300,
        slidesToShow: 5,
        slidesToScroll: 1,
        centerPadding: '10px',
        nextArrow: '<button type="button" class="next ti-angle-right"></button>',
        prevArrow: '<button type="button" class="prev ti-angle-left"></button>'
    });

    if ($("a.img-gallery-tag") && $("a.img-gallery-tag").length > 0) {
        $("a.img-gallery-tag").magnificPopup({
            type: "image",
            gallery: {
                enabled: true,
            }
        });
    }
    if ($("a.video-gallery-tag") && $("a.video-gallery-tag").length > 0) {
        $("a.video-gallery-tag").magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false
        });
    }
    //$('.thumbnails-slides').attr('data-slider_look', '2');
};

publicWidget.registry.WebsiteSale.include({
    _updateProductImage: function ($productContainer, displayImage, productId, productTemplateId, newCarousel, isCombinationPossible) {
        this._super.apply(this, arguments);
        VariantMixin._onChangeProductImage.apply(this, arguments);
    }
});

return VariantMixin;

});