# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime


class jugador(models.Model):
    _name = 'golfv2.jugador'
    _description = 'golfv2.jugador'
    
    name = fields.Char(string='Nombre Jugador', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', required=True)
    edad = fields.Integer(string='Edad', compute='_compute_edad')
    nombre_Equipo = fields.Char(string='Nombre del Equipo', required=True)
    tipo_jugador = fields.Selection(
        [('amateur', 'Amateur'), ('profesional', 'Profesional')],
        required=True, default='amateur'
    )
    tipo_palo = fields.Selection(
        [('driver', 'Driver'), ('madera', 'Madera'),
         ('hibridos', 'Híbridos'), ('hierro', 'Hierro'),
         ('wedge', 'Wedge'), ('putter', 'Putter')],
        required=True, default='driver'
    )

    # ONE TO MANY (muchos registros en partido)
    partidos_ids = fields.One2many(
        'golfv2.partido',
        'jugador_id',
        string='Partidos del Jugador'
    )

    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for record in self:
            if record.fecha_nacimiento:
                today = datetime.date.today()
                birth = record.fecha_nacimiento
                edad = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
                record.edad = edad
            else:
                record.edad = 0


class hoyo(models.Model):
    _name = 'golfv2.hoyo'
    _description = 'golfv2.hoyo'

    name = fields.Char(string="Nombre del hoyo", required=True)
    numero_hoyo = fields.Integer(required=True)
    par = fields.Integer(required=True)
    distancia = fields.Integer(required=True)
    dificultad = fields.Selection(
        [('facil', 'Fácil'), ('medio', 'Medio'), ('dificil', 'Difícil')],
        required=True, default='medio'
    )

    # ONE TO MANY
    partidos_ids = fields.One2many(
        'golfv2.partido',
        'hoyo_id',
        string='Partidos de este Hoyo'
    )


class partido(models.Model):
    _name = 'golfv2.partido'
    _description = 'golfv2.partido'

    # Este registro ES la tabla intermedia
    # Puedes añadir cualquier campo adicional

    name = fields.Char(string="Nombre del partido", required=True)
    fecha_partido = fields.Date(required=True)
    lugar = fields.Char(required=True)

    # MUCHOS → UNO con jugador
    jugador_id = fields.Many2one(
        'golfv2.jugador',
        string='Jugador',
        required=True
    )

    # MUCHOS → UNO con hoyo
    hoyo_id = fields.Many2one(
        'golfv2.hoyo',
        string='Hoyo',
        required=True
    )
