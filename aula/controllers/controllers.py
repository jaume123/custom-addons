# -*- coding: utf-8 -*-
# from odoo import http


# class Aula(http.Controller):
#     @http.route('/aula/aula/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aula/aula/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aula.listing', {
#             'root': '/aula/aula',
#             'objects': http.request.env['aula.aula'].search([]),
#         })

#     @http.route('/aula/aula/objects/<model("aula.aula"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aula.object', {
#             'object': obj
#         })
