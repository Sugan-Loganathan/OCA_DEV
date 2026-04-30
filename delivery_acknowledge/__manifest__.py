{
    'name': "Delivery Acknowledge",
    'summary': "Delivery Acknowledge",
    'description': """Delivery acknowledgment signed by the customer at the time of product handover.
     Attached as confirmation of successful delivery.""",
    'author': "Suganya Loganathan",
    'category': 'Stock',
    'version': '19.0.1.0.0',
    'depends': ['base', 'stock'],
    'data': [
        "views/stock_picking_views_inherit.xml"
    ],
    'images': ['static/description/banner.png'],
    'license': "LGPL-3",
    'installable': True,
    'application': True,
    'auto_install': False,
}
