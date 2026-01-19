# -*- coding: utf-8 -*-
# from odoo import http


# class Futbol(http.Controller):
#     @http.route('/futbol/futbol/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/futbol/futbol/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('futbol.listing', {
#             'root': '/futbol/futbol',
#             'objects': http.request.env['futbol.futbol'].search([]),
#         })

#     @http.route('/futbol/futbol/objects/<model("futbol.futbol"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('futbol.object', {
#             'object': obj
#         })
