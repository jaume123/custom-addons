# -*- coding: utf-8 -*-
# from odoo import http


# class ParqueBomberos(http.Controller):
#     @http.route('/parque_bomberos/parque_bomberos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parque_bomberos/parque_bomberos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('parque_bomberos.listing', {
#             'root': '/parque_bomberos/parque_bomberos',
#             'objects': http.request.env['parque_bomberos.parque_bomberos'].search([]),
#         })

#     @http.route('/parque_bomberos/parque_bomberos/objects/<model("parque_bomberos.parque_bomberos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parque_bomberos.object', {
#             'object': obj
#         })
