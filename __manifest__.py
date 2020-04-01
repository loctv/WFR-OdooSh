# -*- coding: utf-8 -*-
{
    'name': "WFR Recalculated Price",

    'summary': """Recalculated Sale Price""",

    'description': """
        [2218651]
        recalculate pricelist on quotation
        """,

    'author': 'Odoo',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OEEL-1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'product'],

    # always loaded
    'data': [
        'data/actions.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
    'application': False,
}
