# -*- coding: utf-8 -*-
{
    'name': "Landed Cost",

    'summary': """Modified Landed Cost""",

    'description': """
        [2251525]
        """,

    'author': 'Odoo',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OEEL-1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        'views/product_pricelist_views.xml',
        'data/actions.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
    'application': False,
}
