from odoo import models, fields, api

class Clase(models.Model):
    _name = 'aula.clase'
    _description = 'Aula - Clase'

    name = fields.Char(string='Nombre')
    num_alumnos = fields.Integer(string='Número de alumnos')
    tutor = fields.Char(string='Tutor')
    asignaturas = fields.Selection([
        ('matematicas', 'Matemáticas'),
        ('lengua', 'Lengua'),
        ('ciencias', 'Ciencias'),
        ('historia', 'Historia'),
        ('ingles', 'Inglés'),
    ], string='Asignatura')
    capacidad_sillas = fields.Integer(string='Capacidad de sillas')
    nro_ordenadores = fields.Integer(string='Número de ordenadores')
    ordenador_ids = fields.One2many(
        'aula.ordenador',
        'clase_id',
        string='Ordenadores',
    )

class Ordenador(models.Model):
    _name = 'aula.ordenador'
    _description = 'Aula - Ordenador'

    name = fields.Char(string='Nombre')
    marca = fields.Char(string='Marca')
    modelo = fields.Char(string='Modelo')
    anio_fabricacion = fields.Date(string='Año de fabricación')
    usb_ports = fields.Integer(string='Número de puertos USB')
    tipo_ordenador = fields.Selection([
        ('portatil', 'Portátil'),
        ('sobremesa', 'Sobremesa'),
        ('all_in_one', 'All-in-One'),
    ], string='Tipo de ordenador')

    clase_id = fields.Many2one(
        'aula.clase',
        string='Clase',
        ondelete='set null',
    )
    alumno_ids = fields.One2many(
        'aula.alumno',
        'ordenador_id',
        string='Alumnos',
    )
    componentes_ids = fields.One2many(
        'aula.componentes',
        'ordenador_id',
        string='Componentes',
    )

class Componentes(models.Model):
    _name = 'aula.componentes'
    _description = 'Aula - Componentes'

    name = fields.Char(string='Nombre Componente')
    tipo_componente = fields.Selection([
        ('procesador', 'Procesador'),
        ('memoria_ram', 'Memoria RAM'),
        ('disco_duro', 'Disco Duro'),
        ('tarjeta_grafica', 'Tarjeta Gráfica'),
        ('placa_base', 'Placa Base'),
    ], string='Tipo de Componente')
    unidades = fields.Integer(string='Unidades')
    precio = fields.Float(string='Precio')
    ordenador_id = fields.Many2one(
        'aula.ordenador',
        string='Ordenador',
        ondelete='cascade',
    )

class Alumno(models.Model):
    _name = 'aula.alumno'
    _description = 'Aula - Alumno'

    name = fields.Char(string='Nombre')
    surname = fields.Char(string='Apellido')
    age = fields.Integer(string='Edad')
    direccion = fields.Char(string='Dirección')
    mayor_edad = fields.Boolean(string='Mayor de Edad')
    ordenador_id = fields.Many2one(
        'aula.ordenador',
        string='Ordenador',
        ondelete='set null',
    )
