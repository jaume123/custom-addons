
from odoo import models, fields, api


class Marca(models.Model):
     _name = 'modelo_coche.marca'
     _description = 'Marca'

     name = fields.Char()
     fecha_fundacion = fields.Date()
     pais_origen = fields.Char()
     n_fabricas = fields.Integer()
     modeloCoche_ids = fields.One2many('modelo_coche.modelo_coche','marca_id', string='Modelos de Coche')



class ModeloCoche(models.Model):
    _name = 'modelo_coche.modelo_coche'
    _description = 'Modelo de coche'

    name = fields.Char(string='Modelo')
    año_fabricacion = fields.Integer(string='Año de Fabricación')
    N_puertas = fields.Integer(string='Número de Puertas')
    color = fields.Char(string='Color')
    cv = fields.Float(string='CV')
    Deposito_litros = fields.Float(string='Capacidad del Depósito (litros)')
    marca_id = fields.Many2one('modelo_coche.marca', string='Marca')
    