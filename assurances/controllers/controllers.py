# -*- coding: utf-8 -*-
from odoo import http

# class Assurances(http.Controller):
#     @http.route('/assurances/assurances/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/assurances/assurances/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('assurances.listing', {
#             'root': '/assurances/assurances',
#             'objects': http.request.env['assurances.assurances'].search([]),
#         })

#     @http.route('/assurances/assurances/objects/<model("assurances.assurances"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('assurances.object', {
#             'object': obj
#         })