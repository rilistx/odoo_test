from datetime import datetime

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleAutoparts(WebsiteSale):

    @http.route(['/shop', '/shop/page/<int:page>'], type='http', auth="public", website=True)
    def shop(self, **post):
        result = super(WebsiteSaleAutoparts, self).shop(**post)

        domain = [('is_published', '=', True)]

        if post.get('brand_id'):
            brand_id = int(post.get('brand_id'))
            domain.append(('product_variant_ids.compatible_vehicle_ids.brand_id', '=', brand_id))

        if post.get('model_id'):
            model_id = int(post.get('model_id'))
            domain.append(('product_variant_ids.compatible_vehicle_ids', 'in', [model_id]))

        if post.get('year'):
            try:
                year = int(post.get('year'))
                domain.append(('product_variant_ids.compatible_vehicle_ids.model_year_from', '<=', year))
                domain.append(('product_variant_ids.compatible_vehicle_ids.model_year_to', '>=', year))
            except (ValueError, TypeError):
                pass

        if post.get('volume_id'):
            try:
                volume_id = int(post.get('volume_id'))
                domain.append(('product_variant_ids.compatible_vehicle_ids.volume_id', 'in', [volume_id]))
            except (ValueError, TypeError):
                pass

        if len(domain) > 1:
            products = request.env['product.template'].sudo().search(domain)

            result.qcontext.update({
                'products': products,
                'search_count': len(products),
            })

        result.qcontext.update({
            'brands': request.env['fleet.vehicle.model.brand'].sudo().search([]),
            'years': reversed(range(1900, datetime.now().year + 1)),
            'volumes': request.env['engine.volume'].sudo().search([]),
        })

        return result

    @http.route('/shop/get_models', type='json', auth="public", website=True)
    def get_models_search(self, brand_id=None):
        if not brand_id:
            return []

        models = request.env['fleet.vehicle.model'].sudo().search_read(
            [('brand_id', '=', int(brand_id))],
            ['id', 'name'],
        )

        return models
