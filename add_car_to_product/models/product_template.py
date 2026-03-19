from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_autoparts = fields.Boolean(string="Is autopart")
