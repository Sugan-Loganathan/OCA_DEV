/** @odoo-module */

import { ProductInfoPopup } from "@point_of_sale/app/screens/product_screen/product_info_popup/product_info_popup";
import { useService } from "@web/core/utils/hooks";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";
import { ProductStockAddPopup } from "./product_stock_add_popup";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { TextInputPopup } from "@point_of_sale/app/utils/input_popups/text_input_popup";
import { ConnectionLostError, rpc } from "@web/core/network/rpc";
 import { Component, onWillStart } from "@odoo/owl";
 import {
    makeAwaitable,
    ask,
    makeActionAwaitable,
} from "@point_of_sale/app/store/make_awaitable_dialog";

patch(ProductInfoPopup.prototype, {
    setup() {
        super.setup();
        this.pos = usePos();
        this.dialog = useService("dialog");
        this.orm = useService("orm");
        this.popover = useService("popover");
        },

    async open_req(reserve) {
        if (reserve) {
        if(reserve == 1){
            this.fetchProductCacheData();
      }
    }
    },
     mounted() {
            if (this.error) {
                this.cancel();
                if (this.error.message instanceof ConnectionLostError) {
                    this.popover.add('TextInputPopup', {
                        title: _t('Network Error'),
                        body: _t('Cannot access product information screen if offline.'),
                    });
                } else {
                    throw this.error;
                }
            }
        },
async fetchProductCacheData() {
    const response = await this.orm.call(
        "stock.picking",
        "get_warehouses",
        [],
        {}
    );

    const warehouses = response.result;

    this.dialog.add(ProductStockAddPopup, {
        title: _t('Add stock for ' + this.props.product.display_name),
        product: this.props.product,
        warehouses: warehouses,
        reserve: 1,
        });
    this.cancel();
    },
    cancel() {
       this.props.close();
    },
});
