# -*- coding: utf-8 -*-

from odoo import models, fields, api

class assure(models.Model):
	_name = 'hospy.assure'

	name = fields.Char(String='Nom Patient')

class infirmiere(models.Model):
    _name = 'infirmiere.infirmiere'

    name = fields.Char(string='Nom')
    second_name = fields.Char(string='Prenom')
    phone = fields.Integer(string='Numéro de téléphone')
    sexe = fields.Char(string='Sexe du patient')
    email = fields.Char(string='Adresse email')
    quartier = fields.Char(string='Quartier de résidence')
    date_naissance = fields.Char(string='Date de naissance')
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100 
