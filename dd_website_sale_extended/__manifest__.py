# -*- coding: utf-8 -*-
{
    'name': "website delivery date extended",

    'summary': """
                Add delivery date to website extra checkout
        """,
    'version': '13.0.1.0',
    'description': """
        Add delivery date to website extra checkout
    """,
    'author': "INNOVATION SARL",
    'website': "https://www.innovations-groups.com",
    'category': 'website',
    "support": "",

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale',],

    # always loaded
    'data': [
                "views/payment_extended.xml",    
                "views/assets.xml",    
             ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'images': ['static/description/dd_main.jpeg', 'static/description/dd_second.jpeg'],
    'price': 5,
    'currency': 'USD',
    'license': 'OPL-1',
    'live_test_url': '',
    'installable': True,
    'auto_install': False,
    'application': False,
}
