# -*- coding: utf-8 -*-

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    hide_website_price = fields.Boolean(help='hide website price', string="Hide Website Price")
    hide_cart = fields.Boolean(help='hide add to cart/wishlist/compare/quantity', string="Hide Cart")
    pricing_number = fields.Char(string="Call For Pricing Number")
