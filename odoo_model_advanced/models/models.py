# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from datetime import datetime


class Car(models.Model):
    _name = 'odoo_model_advanced.car'
    _description = 'Coche'

    name = fields.Char(string='Modelo')
    number_plate = fields.Char(string='Matrícula')
    cv = fields.Float(string='CV')
    colour = fields.Char(string='Color')
    fuel_litres = fields.Float(string='Litros')
    coche_nuevo = fields.Boolean(string = 'Coche Nuevo', default =True)
    tipo_coche = fields.Selection([
        ('Coche Trabajo', 'Coche de Trabajo'),
        ('Coche Personal', 'Coche Personal'),
        ('Coche de alquiler', 'Coche de Alquiler'),
    ],string = 'Tipo de Coche', default='Coche Personal')
    description = fields.Text(string='Descripción', default='Descripción del coche')
    image = fields.Image(string='Imagen del coche')
    fecha_compra = fields.Date(string='Fecha de compra')



