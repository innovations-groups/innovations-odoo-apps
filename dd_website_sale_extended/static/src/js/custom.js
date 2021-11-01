odoo.define('wt_website_sale_extended.delivery_date', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
var rpc = require('web.rpc');
var ajax = require('web.ajax');

publicWidget.registry.wt_website_sale_delivery_date = publicWidget.Widget.extend({
    selector: '#delivery_date_div',
    events: {
        'change input#delivery_date': '_onchangedeldate',
        },

        _onchangedeldate: function (ev) {
            var date = $(ev.currentTarget).val()
                this._rpc({
                    route: "/set/delivery/date",
                    params: {
                        delivery_date: date
                    },
            })
        },

    });
});
