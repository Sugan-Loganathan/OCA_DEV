{
    'name': 'Website Sale - Hide Price & Cart(Public User)',
    'version': '18.0.1.0.0',
    'category': 'Website/Website',
    'summary': 'Control product price and cart for eCommerce feature visibility for Public Users',
    'description': """
    Website Product Visibility and Access Control
    ==============================================

    This module provides configurable controls for restricting product pricing
    and eCommerce features for public users.

    Features:
    ---------
    * Hide product prices for public/portal users.
    * Restrict the Add to Cart functionality for public users.
    * Restrict the Wishlist functionality for public users.
    * Configure these restrictions from the Company settings.
    * Apply the configured restrictions automatically on the website.
    * Allow administrators to control website product visibility and purchasing
      options based on company-level configuration.

    Configuration:
    --------------
    Go to:
    Settings → Companies → Select Company

    Configure the required product visibility and eCommerce access options
    from the company settings.
    """,
    'author': "Suganya Loganathan",
    'category': 'Website',
    'depends': [
        'website_sale',
        'base',
        'website_sale_wishlist'
    ],
    'data': [
        'views/res_company_views.xml',
        'views/website_hide_price.xml',
    ],
    "assets": {
        "web.assets_frontend": [
            "website_sale_hide_price_cart_wishlist/static/src/css/style.css",
        ]
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
