# -*- coding: utf-8 -*-
# from odoo import http


# class Golfv2(http.Controller):
#     @http.route('/golfv2/golfv2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/golfv2/golfv2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('golfv2.listing', {
#             'root': '/golfv2/golfv2',
#             'objects': http.request.env['golfv2.golfv2'].search([]),
#         })

#     @http.route('/golfv2/golfv2/objects/<model("golfv2.golfv2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('golfv2.object', {
#             'object': obj
#         })
