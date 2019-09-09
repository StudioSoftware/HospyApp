# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests


class customer(models.Model):
    _name = 'customer.customer'

    name = fields.Char(
        string="Nom",
        required=True
    )
    prenom = fields.Char(
        string="Prénom",
    )
    age = fields.Integer(
        string="Age"
    )
    genre = fields.Selection(
        [
            ('masculin', 'Masculin'),
            ('feminin', 'Féminin')
        ],
        required=True,
        string="Genre",
        default="masculin",
        help="Genre du patient"
    )
    phone = fields.Char(
        string="Téléphone",
        required=True,
        help="Numéro de téléphone du patient"
    )
    statut = fields.Selection(
        [
            ('marie', 'Marié'),
            ('celibataire', 'Célibataire'),
            ('divorce', 'Divorcé'),
            ('veuf', 'Veuf')
        ],
        string="Statut matrimonial",
        required=True
    )
    quartier = fields.Char(
        string="Quartier"
    )

    @api.model
    def create(self, vals):
        if vals.get('phone'):
            temp = vals.get('phone')
            url = 'https://www.agis-as.com/epolice/index.php?telephone=' + temp + '&message=Némero enregistré'
            requests.request('GET', url)

        #set recording
        super(customer, self).create(vals)

        return

    # @api.multi
    # def start_consultation(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'view_type': 'tree',
    #         'view_mode': 'tree, form',
    #         'res_model': 'customer.renseignement',
    #         'views': 'renseignement',
    #     }

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100
