odoo.define('pos_custom_aychi_srikesh.multiprint', function (require) {
"use strict";

var multi = require('pos_line_priority_srikesh.multiprint');
var core = require('web.core');
var models = require('point_of_sale.models');
var Printer = require('point_of_sale.Printer').Printer;
var QWeb = core.qweb;

var _super_order = models.Order.prototype;
models.Order = models.Order.extend({

    computeChanges: function(categories){
        var order = _super_order.computeChanges.call(this,categories)
        var json        = this.export_as_JSON();
        order['customer_count'] = json.customer_count;
        return order
    },

});

});
