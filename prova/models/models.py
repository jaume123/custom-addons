# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Prova(models.Model):
	_name = 'prova.prova'
	_description = 'prova.prova'

	name = fields.Char(string="Name")
	value = fields.Integer(string="Value")
	value2 = fields.Float(string="Value2", compute="_value_pc", store=True)
	description = fields.Text(string="Description")

	@api.depends('value')
	def _value_pc(self):
		for record in self:
			record.value2 = float(record.value) / 100 if record.value is not None else 0.0
