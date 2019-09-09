# -*- coding: utf-8 -*-

import random
import requests
from odoo import models, fields, api


class services(models.Model):
    _name = 'services.services'
    # _inherit = "hr.employee"

    name = fields.Char(
        string="Nom du service", required=True
    )
    # photo = fields.Binary(
    #     string="Logo du service",
    #     required=True
    # )
    # selection = fields.Selection(
    #     [
    #         ('A', 'a'),
    #         ('B', 'b'),
    #         ('C', 'c')
    #     ]
    # )
    code = fields.Char(
        string="Code du service",
        help="Code du service",
        readeonly=True
    )
    # service_id = fields.Many2one('infirmiere.infirmiere', string="Infirmiere ")
    # dates = fields.Date(
    #     string="Date",
    #     required=True
    # )
    description = fields.Text(string="Description du service")
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', "Ce nom doit etre unique"),
    ]

    # reecriture de la methode create
    @api.multi
    def create(self, vals):
        url = 'https://www.agis-as.com/epolice/index.php?telephone=691451189&message=Vous etes maitenant dans le ' \
              'systeme hospy soft '
        requests.request("GET", url)
        vals = dict(
            {
                'name': self.name,
                'code': 'COEUR_VIE_'+str(random.random()),
                'description': 'Aucune description fournis'
            }
        )

        # self.code = "CEOUR_VIE_"+str(random.random())
        res = super(services, self).create(vals)
        return res

    @api.one
    def set_name(self):
        self.name = self.name.upper()
        print(self.name)
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2: = float(self.value) / 100
