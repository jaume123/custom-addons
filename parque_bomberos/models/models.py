from odoo import models, fields, api 
from datetime import datetime, date, timedelta




class puesto(models.Model):
    _name = 'parque_bomberos.puesto'
    _description = 'parque_bomberos.puesto'
    
    name = fields.Char(string = 'Nombre puesto')
    salario = fields.Float(string = 'Salario')
    dias_laborales = fields.Integer(string = 'Dias laborales')
    cargo = fields.Selection(
        [('capitan','Capitan'), ('teniente','Teniente'),
         ('general','General'), ('coronel','Coronel')],
         string = 'Tipo de carga ',
         required = True,
         default ='capitan'
        )
    bombero_ids = fields.One2many('parque_bomberos.bombero','puesto_id',string ='bombero')

class bombero(models.Model):
    _name = 'parque_bomberos.bombero'
    _description  = 'parque_bomberos.bombero'

    name = fields.Char(string='Nombre')
    apellido1 = fields.Char(string='Primer Apellido')
    apellido2 = fields.Char(string='Segundo Apellido')
    nombre_completo = fields.Char(string='Nombre Completo', compute='_compute_nombre_completo', store=True)
    edad = fields.Integer(string = 'Edad',compute = "_calculo_edad")
    fecha_nacimiento = fields.Date(string = 'Fecha de nacimiento',required=True)
    tablaintermedia_ids = fields.One2many('parque_bomberos.tablaintermedia','bombero_ids',string="Camion que pertenece")
    activo = fields.Boolean(string ='En Servicio ?')
    especialidad = fields.Selection([
        ('rescate', 'Rescate'),
        ('incendios', 'Incendios'),
        ('medico', 'Medico'),
        ('quimicos', 'Quimicos'),
    ], string='Especialidad')
    puesto_id = fields.Many2one('parque_bomberos.puesto',string='Puesto que ejerce')

    @api.depends('name', 'apellido1', 'apellido2')
    def _compute_nombre_completo(self):
        for record in self:
            # Construye el nombre completo concatenando los campos que tengan valor
            partes = []
            if record.name:
                partes.append(record.name)
            if record.apellido1:
                partes.append(record.apellido1)
            if record.apellido2:
                partes.append(record.apellido2)
            record.nombre_completo = ' '.join(partes)

    @api.depends("fecha_nacimiento")
    def _calculo_edad(self):
        for record in self:
            if record.fecha_nacimiento:
                hoy = date.today()
                nacimiento = record.fecha_nacimiento
                edad = hoy.year - nacimiento.year
                # Ajuste si todavía no ha cumplido años este año
                if nacimiento.month > hoy.month or (nacimiento.month == hoy.month and nacimiento.day > hoy.day):
                    edad -= 1
                record.edad = edad
            else:
                record.edad = 0
            

class camion(models.Model): 
    _name = 'parque_bomberos.camion'
    _description = 'parque_bomberos.camion'
    
    name = fields.Char(string = 'Nombre Camion')
    matricula = fields.Char(string ='Matricula Camion')
    fecha_compra = fields.Date(string='Fecha de compra')
    activo = fields.Boolean(string='En servicio ? ')
    tablaintermedia_ids = fields.One2many('parque_bomberos.tablaintermedia','camion_ids',string ='Bomberos en el camion')
    tipo_ruedas = fields.Selection([
        ('tierra', 'Tierra'),
        ('agua', 'Agua'),
        ('todoterreno', 'TodoTerreno'),
    ], string='Tipo de ruedas')
    color = fields.Char(string = 'Color de camion')
    manguera_extensible = fields.Boolean(string = 'Manguera Extensible?')
    parque_id = fields.Many2one('parque_bomberos.parque', string='Parque al que pertenece')

    
    
class parqueBomberos(models.Model):
    _name = 'parque_bomberos.parque'
    _description = 'parque_bomberos.parque'
    
    name = fields.Char(string = 'Nombre Parque')
    direccion = fields.Char(string = 'Direccion Parque')
    ubicacion = fields.Char(string = 'Ubicacion Parque')
    activo = fields.Boolean(string = 'Parque en servicio ?')
    numerodepartamento = fields.Integer(string='Numero de departamento')
    
    camion_ids = fields.One2many('parque_bomberos.camion', 'parque_id', string='Camiones')


class tablaintermedia(models.Model):
     _name = 'parque_bomberos.tablaintermedia'
     _description = 'Tabla Intermedia de Bomberos y Camiones'

     name = fields.Char(string ="Nombre del anexo")
     descripcion = fields.Char(string = "Descripcion del anexo")
     bombero_ids = fields.Many2one('parque_bomberos.bombero',string = "bomberos")
     camion_ids = fields.Many2one('parque_bomberos.camion',string = "camiones")