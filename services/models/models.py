# -*- coding: utf-8 -*-

from odoo import models, fields, api

class services(models.Model):
    _name = 'services.services'

    name = fields.Char(string="Nom du service", require=True)
    code = fields.Char(string="Code du service")
    description = fields.Text(string="Description du service")
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    #description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100