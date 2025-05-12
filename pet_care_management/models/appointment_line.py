from odoo import models, fields

class PetAppointmentLine(models.Model):
    _name = 'pet.appointment.line'
    _description = 'Appointment Service Line'

    appointment_id = fields.Many2one('pet.appointment', required=True, ondelete='cascade')
    product_id = fields.Many2one(
        'product.product',
        required=True,
        domain=lambda self: [('categ_id', '=', self.env.ref('pet_care_management.product_category_pet_services').id)]
    )
    quantity = fields.Float(default=1.0)
    price_unit = fields.Float(related='product_id.list_price', readonly=True)
