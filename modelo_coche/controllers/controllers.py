# -*- coding: utf-8 -*-
# from odoo import http


# class ModeloCoche(http.Controller):
#     @http.route('/modelo_coche/modelo_coche/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modelo_coche/modelo_coche/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modelo_coche.listing', {
#             'root': '/modelo_coche/modelo_coche',
#             'objects': http.request.env['modelo_coche.modelo_coche'].search([]),
#         })

#     @http.route('/modelo_coche/modelo_coche/objects/<model("modelo_coche.modelo_coche"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modelo_coche.object', {
#             'object': obj
#         })
