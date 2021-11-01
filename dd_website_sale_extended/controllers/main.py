# -*- coding: utf-8 -*-
import json
import logging
from odoo import fields, http, tools, SUPERUSER_ID, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http
from odoo.http import request, route

_logger = logging.getLogger(__name__)


class WebsiteSaleCustom(WebsiteSale):
    @http.route(['/set/delivery/date'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def set_delivery_date(self, delivery_date=None):
        order = request.website.sale_get_order()
        order.write({
            'commitment_date': delivery_date,
        })
