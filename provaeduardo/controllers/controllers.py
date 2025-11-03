# -*- coding: utf-8 -*-
# from odoo import http


# class Provaeduardo(http.Controller):
#     @http.route('/provaeduardo/provaeduardo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/provaeduardo/provaeduardo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('provaeduardo.listing', {
#             'root': '/provaeduardo/provaeduardo',
#             'objects': http.request.env['provaeduardo.provaeduardo'].search([]),
#         })

#     @http.route('/provaeduardo/provaeduardo/objects/<model("provaeduardo.provaeduardo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('provaeduardo.object', {
#             'object': obj
#         })
