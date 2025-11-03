# -*- coding: utf-8 -*-
# from odoo import http


# class Coche(http.Controller):
#     @http.route('/coche/coche/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coche/coche/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('coche.listing', {
#             'root': '/coche/coche',
#             'objects': http.request.env['coche.coche'].search([]),
#         })

#     @http.route('/coche/coche/objects/<model("coche.coche"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coche.object', {
#             'object': obj
#         })
