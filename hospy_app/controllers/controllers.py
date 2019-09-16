# -*- coding: utf-8 -*-
from odoo import http

# class HospyApp(http.Controller):
#     @http.route('/hospy_app/hospy_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospy_app/hospy_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospy_app.listing', {
#             'root': '/hospy_app/hospy_app',
#             'objects': http.request.env['hospy_app.hospy_app'].search([]),
#         })

#     @http.route('/hospy_app/hospy_app/objects/<model("hospy_app.hospy_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospy_app.object', {
#             'object': obj
#         })