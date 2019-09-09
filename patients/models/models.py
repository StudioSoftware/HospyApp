# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Patients(models.Model):
    _name = 'hospy.patients'

    name = fields.Char(
        string="Nom",
        string=True
    )
    second_name = fields.Char(string="Prénom")
    naissance = fields.Date(
        string="Date naissance",
        required=True
    )
    genre = fields.Selection(
        [
            ('masculin', 'Masculin'),
            ('feminin', 'Feminin')
        ]
    )
    phone = fields.Integer(
        string="N° Téléphone",
        required=True
    )
