# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Equipo(models.Model):
    _name = 'futbol.equipo'
    _description = 'futbol.equipo'
    _order = 'puntos desc, name'

    name = fields.Char(string="Nombre del equipo")
    fecha_creacion = fields.Date(string="Fecha de creación")
    estadio = fields.Char(string="Estadio del equipo")
    entrenador = fields.Char(string="Nombre del entrenador del equipo")

    partidos_local_ids = fields.One2many(
        'futbol.partido',
        'equipo_local_id',
        string="Partidos como local"
    )
    partidos_visitante_ids = fields.One2many(
        'futbol.partido',
        'equipo_visitante_id',
        string="Partidos como visitante"
    )
    jugador_ids = fields.One2many(
        'futbol.jugador',
        'equipo_id',
        string="Jugadores"
    )

    puntos = fields.Integer(
        string="Puntos",
        compute='_compute_puntos',
        store=True
    )

    @api.depends(
        'partidos_local_ids.finalizado',
        'partidos_local_ids.goles_local',
        'partidos_local_ids.goles_visitante',
        'partidos_visitante_ids.finalizado',
        'partidos_visitante_ids.goles_local',
        'partidos_visitante_ids.goles_visitante'
    )
    def _compute_puntos(self):
        for equipo in self:
            puntos_total = 0

            # Partidos como local
            for p in equipo.partidos_local_ids:
                if not p.finalizado:
                    continue
                if (p.goles_local or 0) > (p.goles_visitante or 0):
                    puntos_total += 3
                elif (p.goles_local or 0) < (p.goles_visitante or 0):
                    puntos_total += 1
                else:
                    puntos_total += 1

            # Partidos como visitante
            for p in equipo.partidos_visitante_ids:
                if not p.finalizado:
                    continue
                if (p.goles_visitante or 0) > (p.goles_local or 0):
                    puntos_total += 3
                elif (p.goles_visitante or 0) < (p.goles_local or 0):
                    puntos_total += 1
                else:
                    puntos_total += 1

            equipo.puntos = puntos_total


class Partido(models.Model):
    _name = 'futbol.partido'
    _description = 'futbol.partido'

    name = fields.Char()
    fecha_partido = fields.Date(string="Fecha del partido")
    resultado = fields.Char(string="Resultado del partido")
    goles_local = fields.Integer(string="Goles del equipo local")
    goles_visitante = fields.Integer(string="Goles del equipo visitante")

    equipo_local_id = fields.Many2one(
        'futbol.equipo',
        string="Equipo local"
    )
    equipo_visitante_id = fields.Many2one(
        'futbol.equipo',
        string="Equipo visitante"
    )

    finalizado = fields.Boolean(
        string="¿Partido finalizado?",
        default=False
    )


class Jugador(models.Model):
    _name = 'futbol.jugador'
    _description = 'futbol.jugador'

    name = fields.Char(string="Nombre del jugador")
    edad = fields.Integer(string="Edad del jugador")
    posicion = fields.Char(string="Posición del jugador")
    equipo_id = fields.Many2one(
        'futbol.equipo',
        string="Equipo al que pertenece"
    )
    numero_camiseta = fields.Integer(string="Número de camiseta")
    fecha_firma = fields.Date(string="Fecha de firma del contrato")
    nacionalidad = fields.Char(string="Nacionalidad del jugador")
