/** @odoo-module **/
import { _t } from "@web/core/l10n/translation";
import { useService } from "@web/core/utils/hooks";
import { Dialog } from "@web/core/dialog/dialog";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { Component, useState } from "@odoo/owl";

export class ProductStockAddPopup extends Component {
    static template = "pos_stock_update.ProductStockAddPopup";
    static components = { Dialog };
    static defaultProps = {
        confirmText: _t("Ok"),
        closePopup: _t("Cancel"),
        cancelText: _t("Discard"),
        reserveText : _t("Add"),
        requestText : _t("Request"),
        array: [],
        title: _t("Create ?"),
        body: "",
        startingValue: '',
        priceValue: 0,
    };
    static props = {
        title: { type: String, optional: true },
        product: Object,
        warehouses: Array,
        reserve: Number,
        close: Function,
    };
     async load_products(){
            var x =  await this.props.product;
            this.state.products = x;
        }

        async load_warehouses(){
            var x =  await this.props.warehouses;
            this.state.warehouses = x;
        }
         setup() {
            super.setup();
            this.pos = usePos();
            this.orm = useService("orm");
            this.notification = useService("notification");
            this.dialog = useService("dialog");
            this.state = useState({
                    products: [],
                    warehouse: this.pos.config,
                    warehouses: [],
                    typeValue: this.props.startingValue,
                    productValue: this.props.startingValue,
                    priceValue: this.props.priceValue,
                    productRef: this.props.startingValue,
                    pass: '',
                    title: "Request stock for a Product",
                });
            this.load_products()
            this.load_warehouses()
        }
     async confirm(data, reserve,self) {
    if (self.state.priceValue <= 0){
        self.pos.showScreen('ProductScreen');
       self.notification.add(_t('Please check given quantity!!!'), {
            type: 'danger',
            title: _t('Quantity Alert!'),
        });
       return;
    }
    const res = await self.orm.call("stock.picking", "create_from_pos", [[], [{'warehouse_name': self.pos.config.id}, self.props.product.id, self.state.priceValue, self.state.wareValue, self.state.note,self.state.pass], reserve], {}
    ).then(function(result) {
        data: result;
        if(result){
                    self.pos.showScreen('ProductScreen');
                     self.notification.add(_t('Transfer  ' + result.result +' Created Successfully!!!!'), {
                        type: 'success',
                        title: _t('Successfully'),
                         });
                     }
                return;

    });
    self.cancel();
    }
    cancel() {
       this.props.close();
    }
}
