# -*- coding: utf-8 -*-
from odoo import models, fields

class StockPicking(models.Model):
    _inherit = "stock.picking"

    document_ids = fields.One2many(string='Documents', comodel_name='ir.attachment', inverse_name='picking_id',
                                   store=True)

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    picking_id = fields.Many2one(string='Picking', comodel_name='stock.picking')
