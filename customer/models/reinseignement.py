from odoo import fields, api, models
from datetime import datetime


class Renseignement(models.Model):
    _name = 'customer.renseignement'

    date = fields.Date(
        string="Date consultation",
        required=True,
        readonly=True,
        default=datetime.now()
    )
    motif = fields.Html(
        string="Details de la consultation",
    )