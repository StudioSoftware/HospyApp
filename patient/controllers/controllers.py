# -*- coding: utf-8 -*-
from odoo import http

# class Patient(http.Controller):
#     @http.route('/patient/patient/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/patient/patient/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('patient.listing', {
#             'root': '/patient/patient',
#             'objects': http.request.env['patient.patient'].search([]),
#         })

#     @http.route('/patient/patient/objects/<model("patient.patient"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('patient.object', {
#             'object': obj
#         })