# -*- coding: utf-8 -*-

# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import models, fields


class MedicalRole(models.Model):
    _name = 'medical.role'
    _description = 'Practitioner Roles'

    name = fields.Char(
        required=True,
    )

    description = fields.Char(
        required=True,
    )

    active = fields.Boolean(
        default=True,
    )
