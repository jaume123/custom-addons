# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libro(models.Model):
     _name = 'modulo1.libro'
     _description = 'modulo1.libro'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()