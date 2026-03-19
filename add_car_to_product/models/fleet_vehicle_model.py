from odoo import models, fields, api


class FleetVehicleModel(models.Model):
    _inherit = 'fleet.vehicle.model'

    model_year_from = fields.Integer(string="Year from")
    model_year_to = fields.Integer(string="Year to")
    model_type = fields.Char(string="Model type")
    volume_id = fields.Many2one('engine.volume', string="Volume")
    ovoko_car_id = fields.Char(string="Ovoko Car ID")

    year_from_str = fields.Char(string="Year from", compute="_compute_year_from_str", store=True)
    year_to_str = fields.Char(string="Year to", compute="_compute_year_to_str", store=True)

    years_str = fields.Char(string="Years", compute="_compute_years_str")

    @api.depends('model_year_from')
    def _compute_year_from_str(self):
        for rec in self:
            rec.year_from_str = str(rec.model_year_from) if rec.model_year_from else ""

    @api.depends('model_year_to')
    def _compute_year_to_str(self):
        for rec in self:
            rec.year_to_str = str(rec.model_year_to) if rec.model_year_to else ""

    @api.depends('year_from_str', 'year_to_str')
    def _compute_years_str(self):
        for rec in self:
            years = []

            if rec.year_from_str:
                years.append(rec.year_from_str)
            if rec.year_to_str:
                years.append(rec.year_to_str)

            rec.years_str = " - ".join(years) if years else ""
