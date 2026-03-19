from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.model
    # this function is to get all warehouses in the company and called in js file
    def get_warehouses(self):
            rec = self.env['stock.warehouse'].sudo().search([])
            warehouses = [{'id': warehouse.id, 'name': warehouse.name} for warehouse in rec]
            return {'result':warehouses}

            # create the stock.picking from pos based on js

    def create_from_pos(self, data, reserve=False):
        pos_id = self.env['pos.config'].sudo().browse(data[0].get('warehouse_name'))
        w_id = int(pos_id.picking_type_id.warehouse_id.id)
        if reserve:
            operation_type = self.env['stock.picking.type'].sudo().search(
                [('warehouse_id', '=', w_id), ('name', 'ilike', 'Receipt')], limit=1)
            location = self.env['stock.location'].sudo().search([('name', 'ilike', 'Vendor')], limit=1)
        else:
            warehouse = self.env['stock.warehouse'].browse(int(data[3]))
            operation_type = warehouse.int_type_id
            location = warehouse.lot_stock_id
        location_dest = self.env['stock.warehouse'].browse(w_id).lot_stock_id
        res = self.env['stock.picking'].create({'partner_id': 1, 'picking_type_id': operation_type.id,
                                                'location_id': location.id, 'location_dest_id': location_dest.id,
                                                'scheduled_date': fields.Datetime.now(), 'note': data[4],
                                                })
        product = self.env['product.product'].browse(int(data[1]))
        if data[5]:
            product.is_qty_updated = True
        self.env['stock.move'].create({'name': 'POS stock request',
                                       'product_uom': product.uom_id.id,
                                       'product_id': int(data[1]),
                                       'product_uom_qty': int(data[2]),
                                       'company_id': res.company_id.id,
                                       'location_id': location.id,
                                       'location_dest_id': location_dest.id,
                                       'date': fields.Date.today(),
                                       'picking_id': res.id
                                       }),
        if reserve:
            res.action_confirm()
            res.button_validate()
        if res:
            return {'result':res.name}