from odoo import models, fields


class EngineVolume(models.Model):
    _name = 'engine.volume'
    _description = 'Engine Volume'

    name = fields.Char(string="Volume", required=True)
