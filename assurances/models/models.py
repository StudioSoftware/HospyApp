# -*- coding: utf-8 -*-

from odoo import models, fields, api


class assurances(models.Model):
    _name = 'assurances.assurances'

    name = fields.Char(
        string="Nom assurance",
        required=True
    )
    code = fields.Char(
        string="Code"
    )
    RCCM = fields.Char(
        string="RCCM",
        help="Registre de commernce de l'assurance à ajouter"
    )
    phone1 = fields.Integer(
        string="N° Téléphone",
        required=True
    )
    phone2 = fields.Integer(
        string="Autre téléphone"
    )
    email = fields.Char(
        'Adresse email',
        required=True
    )
    image = fields.Binary()
    responsable = fields.Char(
        'Responsable',
        required=True
    )
    poste = fields.Char('Poste occupé')
    region = fields.Selection(
        [
            ('centre', 'Centre'),
            ('littoral', 'Littoral'),
            ('ouest', 'Ouest'),
            ('nord', 'Nord')
        ],
        string="Région",
        required=True,
    )
    date = fields.Date(
        string="Date ajout"
    )

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', "Ce nom existe deja dans la plateforme")
    ]
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100
