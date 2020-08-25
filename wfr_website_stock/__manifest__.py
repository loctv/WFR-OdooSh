# -- coding: utf-8 --
{
    'name': 'WFR Website Stock Display',

    'summary': 'WFR: Inventory Availability in Website',

    'description': """
    task id: 2308569

    Inventory Availability in Website

    """,
    'author': 'Odoo',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OEEL-1',

    # any module necessary for this one to work correctly
    'depends': ['website_sale_stock'],

    # always loaded
    'data': [
    'views/assets.xml'
    ],
    'application': False,
}
