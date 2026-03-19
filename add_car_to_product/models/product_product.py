from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    name = fields.Char(related=False, compute='_compute_custom_name', store=True, readonly=False)
    is_autoparts = fields.Boolean(related='product_tmpl_id.is_autoparts', string="Is autoparts", store=True)
    compatible_vehicle_ids = fields.Many2many('fleet.vehicle.model', string="Compatible Vehicles")
    for_all_models = fields.Boolean(string="For all models")
    oem = fields.Char(string="OEM")
    ovoko_part_id = fields.Char(string="Ovoko Part ID")

    @api.depends(
        'product_tmpl_id.name',
        'is_autoparts',
        'compatible_vehicle_ids',
        'compatible_vehicle_ids.brand_id',
        'compatible_vehicle_ids.name',
        'compatible_vehicle_ids.model_type',
        'compatible_vehicle_ids.years_str',
    )
    def _compute_custom_name(self):
        for product in self:
            product_name = product.product_tmpl_id.name or ""

            if product.is_autoparts and product.compatible_vehicle_ids:
                variant = product.compatible_vehicle_ids[0]

                brand_name = variant.brand_id.name if variant.brand_id else ""
                model_name = variant.name or ""
                model_type = variant.model_type or ""
                model_years = variant.years_str or ""

                product.name = (
                    f"{product_name} {brand_name} {model_name} {model_type} {model_years}"
                )
            else:
                product.name = product_name
