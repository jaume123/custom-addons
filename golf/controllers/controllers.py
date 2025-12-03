# -*- coding: utf-8 -*-
# from odoo import http


# class Golf(http.Controller):
#     @http.route('/golf/golf/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/golf/golf/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('golf.listing', {
#             'root': '/golf/golf',
#             'objects': http.request.env['golf.golf'].search([]),
#         })

#     @http.route('/golf/golf/objects/<model("golf.golf"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('golf.object', {
#             'object': obj
#         })
