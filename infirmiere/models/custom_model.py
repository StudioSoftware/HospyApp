from odoo import models, fields

class CustomeModel(models.Model):
	_name = 'infirmiere.infirmiere'

	name = fields.Char(string='Name')