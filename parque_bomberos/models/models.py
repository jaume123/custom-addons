from odoo import models, fields, api 
from datetime import datetime, date, timedelta

class bombero(models.Model):
    _name = 'parque_bomberos.bombero'
    _description  = 'parque_bomberos.bombero'

    name = fields.Char(string='Nombre')
    edad = fields.Integer(string = 'Edad',compute = "_calculo_edad")
    fecha_nacimiento = fields.Date(string = 'Fecha de nacimiento',required=True)
    camion_id = fields.Many2one('parque_bomberos.camion',string ="Camion assignado")
    activo = fields.Boolean(string ='En Servicio ?')


    @api.depends("fecha_nacimiento")
    def _calculo_edad(self):
        for record in self:
            hoy = date.today()
            nacimiento = record.fecha_nacimiento
            edad = hoy.year - nacimiento.year
            # Ajuste si todavía no ha cumplido años este año
            if nacimiento.month > hoy.month or (nacimiento.month == hoy.month and nacimiento.day > hoy.day):
                edad -= 1
            record.edad = edad
            

class camion(models.Model):
    _name = 'parque_bomberos.camion'
    _description = 'parque_bomberos.camion'
    
    name = fields.Char(string = 'Nombre Camion')
    matricula = fields.Char(string ='Matricula Camion')
    activo = fields.Boolean(string='En servicio ? ')
    bomberos_ids = fields.One2many('parque_bomberos.bombero','camion_id',string ='Bomberos en el camion')
    tipo_ruedas = fields.Selection([
        ('tierra', 'Tierra'),
        ('agua', 'Agua'),
        ('todoterreno', 'TodoTerreno'),
    ], string='Tipo de ruedas')
    color = fields.Char(string = 'Color de camion')
    manguera_extensible = fields.Boolean(string = 'Manguera Extensible?')