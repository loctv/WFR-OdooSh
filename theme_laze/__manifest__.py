# -*- coding: utf-8 -*-

{
    'name': 'Theme Laze',
    'category': 'Theme/Ecommerce',
    'summary': """Multipurpose Premium Responsive Odoo Theme - Fashion, Furniture, Sports, Jewellery, Corporate""",
    'version': '1.0',
    'sequence': 1000,
    'author': 'Atharva System',
    'license' : 'OPL-1',
    'support': 'support@atharvasystem.com',
    'website' : 'https://www.atharvasystem.com',
    'description': """
    Theme Laze is one of the most powerful, amazing and flexible theme on Odoo store. 
    Multipurpose Premium Responsive Odoo Themes - Fashion, Furniture, Sports, Jewellery, Corporate.
Creative theme,
Ecommerce theme,
Entertainment theme,
Personal theme,
Services theme,
Technology theme,
Business theme,
Multipurpose odoo theme,
Multi-purpose theme,
Theme Laze, 
Odoo new themes,
Laze Theme, 
Bootstrap4 odoo themes,
eCommerce Businesses,
        """,
    'depends': ['website_theme_install','atharva_theme_general'],
    'data': [
        'views/customize_theme_templates.xml',
        'views/assets.xml',
        'views/snippets.xml',
    ],
    'live_test_url': 'http://theme-laze.atharvasystem.com/',
    'images': ['static/description/laze_banner.png','static/description/laze_banner_screenshot.gif'],
    'price': 185.00,
    'currency': 'EUR',
    'application': True,
}
