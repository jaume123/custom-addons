from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Cliente(models.Model):
    _name = 'cestacompra.cliente'
    _description = 'Cliente'

    name = fields.Char(required=True)
    apellido = fields.Char(required=True)
    email = fields.Char()
    telefono = fields.Char()
    direccion = fields.Char()
    activo = fields.Boolean(default=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    country_id = fields.Many2one('res.country', string='País')
    cesta_ids = fields.One2many(
        'cestacompra.cesta_compra',
        'cliente_id',
        string='Cestas'
    )


class CestaCompra(models.Model):
    _name = 'cestacompra.cesta_compra'
    _description = 'Cesta de la compra'

    name = fields.Char(required=True)
    cliente_id = fields.Many2one(
        'cestacompra.cliente',
        required=True,
        string='Cliente'
    )
    fecha_creacion = fields.Datetime(
        string='Fecha de Creación',
        default=fields.Datetime.now
    )
    estado = fields.Selection(
        [
            ('borrador', 'Borrador'),
            ('confirmada', 'Confirmada')
        ],
        default='borrador'
    )
    observaciones = fields.Text(string='Observaciones')

    linea_ids = fields.One2many(
        'cestacompra.linea_cesta',
        'cesta_id',
        string='Líneas de la cesta'
    )

    total = fields.Float(
        compute='_compute_total',
        store=True
    )

    @api.depends('linea_ids.subtotal')
    def _compute_total(self):
        for cesta in self:
            cesta.total = sum(cesta.linea_ids.mapped('subtotal'))

    def action_confirmar(self):
        for cesta in self:
            if not cesta.linea_ids:
                raise ValidationError("La cesta está vacía.")
            cesta.estado = 'confirmada'
              # Retornar acción para abrir la cesta confirmada (vista formulario)
        return {
            'name': 'Cesta Confirmada',
            'type': 'ir.actions.act_window',
            'res_model': 'cestacompra.cesta_compra',
            'view_mode': 'form',
            'res_id': cesta.id,
            'target': 'current',
        }


class Producto(models.Model):
    _name = 'cestacompra.producto'
    _description = 'Producto'

    name = fields.Char(required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(required=True)
    stock = fields.Integer(default=0)
    tipo_producto = fields.Selection(
        [('tipo1', 'Tipo 1'), ('tipo2', 'Tipo 2')],
        string='Tipo de producto'
    )
    linea_cesta_ids = fields.One2many(
        'cestacompra.linea_cesta',
        'producto_id',
        string='Líneas de cesta'
    )


class LineaCesta(models.Model):
    _name = 'cestacompra.linea_cesta'
    _description = 'Línea de cesta'

    cesta_id = fields.Many2one(
        'cestacompra.cesta_compra',
        required=True,
        string='Cesta'
    )
    producto_id = fields.Many2one(
        'cestacompra.producto',
        required=True,
        string='Producto'
    )
    cantidad = fields.Integer(default=1)
    precio_unitario = fields.Float(string='Precio Unitario')
    subtotal = fields.Float(
        compute='_compute_subtotal',
        store=True
    )

    @api.depends('cantidad', 'precio_unitario')
    def _compute_subtotal(self):
        for linea in self:
            linea.subtotal = linea.cantidad * linea.precio_unitario

    @api.onchange('producto_id')
    def _onchange_producto(self):
        if self.producto_id:
            self.precio_unitario = self.producto_id.precio

    @api.model
    def create(self, vals):
        producto = self.env['cestacompra.producto'].browse(vals['producto_id'])
        cantidad = vals.get('cantidad', 0)

        if cantidad > producto.stock:
            raise ValidationError(
                f"Stock insuficiente. Disponible: {producto.stock}"
            )

        producto.stock -= cantidad
        return super().create(vals)

    def write(self, vals):
        for linea in self:
            if 'cantidad' in vals:
                nueva = vals['cantidad']
                diferencia = nueva - linea.cantidad

                if diferencia > 0 and diferencia > linea.producto_id.stock:
                    raise ValidationError(
                        f"Stock insuficiente. Disponible: {linea.producto_id.stock}"
                    )

                linea.producto_id.stock -= diferencia

        return super().write(vals)

    def unlink(self):
        for linea in self:
            linea.producto_id.stock += linea.cantidad
        return super().unlink()
