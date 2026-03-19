{
    'name': "POS Stock Update",

    'summary': "Add stock to products from the POS interface with backend receipt creation.",

    'description': """Add stock to products from the POS interface with backend receipt creation""",
    'author': "Suganya Loganathan",
    'category': 'Point of Sale',
    'version': '18.0.1.0.0',
    'depends': ['base', 'point_of_sale', 'stock'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_stock_add/static/src/js/product_stock_add_popup.js',
            'pos_stock_add/static/src/xml/product_stock_add_popup.xml',
            'pos_stock_add/static/src/js/productinfo_popup_inherit.js',
            'pos_stock_add/static/src/xml/productinfo_popup_inherit.xml',
        ]},
    'images': ['static/description/banner.png'],
    'license': "LGPL-3",
    'installable': True,
    'application': True,
    'auto_install': False,
}
