from odoo import models, fields


class Marca(models.Model):
    _name = 'modelo_coche.marca'
    _description = 'Marca'

    name = fields.Char(string='Nombre', required=True)
    fecha_fundacion = fields.Date(string='Fecha de fundación')
    pais_origen = fields.Char(string='País de origen')
    n_fabricas = fields.Integer(string='Número de fábricas')

    # 1 Marca → N Modelos
    modeloCoche_ids = fields.One2many(
        'modelo_coche.modelo_coche',
        'marca_id',
        string='Modelos de coche',
    )


class ModeloCoche(models.Model):
    _name = 'modelo_coche.modelo_coche'
    _description = 'Modelo de coche'

    name = fields.Char(string='Modelo', required=True)
    anio_fabricacion = fields.Integer(string='Año de fabricación')
    N_puertas = fields.Integer(string='Número de puertas')
    color = fields.Char(string='Color')
    cv = fields.Float(string='CV')
    Deposito_litros = fields.Float(string='Capacidad del depósito (litros)')

    # N Modelos → 1 Marca
    marca_id = fields.Many2one(
        'modelo_coche.marca',
        string='Marca',
    )

    # 1 Modelo → N Versiones
    version_ids = fields.One2many(
        'modelo_coche.version',
        'modelo_coche_id',
        string='Versiones',
    )


class Version(models.Model):
    _name = 'modelo_coche.version'
    _description = 'Versión del coche'

    name = fields.Char(string='Versión', required=True)
    equipamiento = fields.Text(string='Equipamiento')
    precio = fields.Float(string='Precio')

    # N Versiones → 1 Modelo
    modelo_coche_id = fields.Many2one(
        'modelo_coche.modelo_coche',
        string='Modelo de coche',
    )
