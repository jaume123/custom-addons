# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime 

class jugador(models.Model):
     _name = 'golf.jugador'
     _description = 'golf.jugador'
     
     name = fields.Char(string='Nombre Jugador', required=True)
     fecha_nacimiento = fields.Date(string='Fecha de Nacimiento',required=True)
     edad = fields.Integer(string='Edad',compute = '_compute_edad')
     nombre_Equipo = fields.Char(string='Nombre del Equipo', required=True)
     tipo_jugador = fields.Selection(
         [('amateur', 'Amateur'), ('profesional', 'Profesional')],
         string='Tipo de Jugador',
         required=True,
         default='amateur'
     )
     tipo_palo = fields.Selection(
         [('driver', 'Driver'), ('madera', 'Madera'), ('hibridos', 'Híbridos'),
          ('hierro', 'Hierro'), ('wedge', 'Wedge'), ('putter', 'Putter')],
         string='Tipo de Palo',
         required=True,
         default='driver'
     )
     caddies_ids = fields.Many2many('golf.caddie', string='caddie')

     @api.depends('fecha_nacimiento')
     def _compute_edad(self):
         for record in self:
             if record.fecha_nacimiento:
                 today = datetime.date.today()
                 birth_date = record.fecha_nacimiento
                 edad = today.year - birth_date.year
                 # Restar 1 si aún no ha cumplido años este año
                 if (today.month, today.day) < (birth_date.month, birth_date.day):
                     edad -= 1
                 record.edad = edad
             else:
                 record.edad = 0
class caddie(models.Model):
    _name = 'golf.caddie'
    _description = 'golf.caddie'

    name = fields.Char(string = 'Nombre del caddie',required = True)
    tipo_bolsa = fields.Selection(
        [('tourbag','TourBag'), ('cartbag','CartBag'),
         ('stanbag','StandBag'), ('pencilbag','PencilBag')],
         string = 'Tipo de bolsa',
         required = True,
         default ='cartbag'
        )
    guantes_antideslizantes = fields.Boolean(string ='Guantes antideslizantes')
    kit_primerosAuxilios = fields.Boolean(string ='Kit de primeros auxilios')    
    tipo_gps = fields.Selection(
        [ ('gps','GPS'),('yardometro','Yardometro')],
         string = 'Tipo GPS',
         required=True, 
         default ='gps'
         )
    jugadores_ids = fields.Many2many('golf.jugador',string = "Jugadores")
    
                            