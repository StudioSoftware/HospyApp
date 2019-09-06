# -*- coding: utf-8 -*-
from odoo import http

class Infirmiere(http.Controller):
    @http.route('/infirmiere/infirmiere/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/infirmiere/infirmiere/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('infirmiere.listing', {
            'root': '/infirmiere/infirmiere',
            'objects': http.request.env['infirmiere.infirmiere'].search([]),
        })

    @http.route('/infirmiere/infirmiere/objects/<model("infirmiere.infirmiere"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('infirmiere.object', {
            'object': obj
        })