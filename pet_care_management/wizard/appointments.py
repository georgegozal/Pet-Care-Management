# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PetAppointmentWizard(models.TransientModel):
    _name = "pet.appointment.wizard"

    pet = fields.Many2one(
        comodel_name='pet.pet',
        string="Pet",
        required=True
    )

    appointment_date = fields.Datetime(string="Appointment Date & Time", required=True)
    appointment_type = fields.Selection([
        ('vet_checkup', 'Vet Check-up'),
        ('grooming', 'Grooming'),
        ('vaccination', 'Vaccination'),
        ('other', 'Other')
    ], string="Appointment Type", required=True)

    pet_employee = fields.Many2one(
        'res.users',
        string='Groomer/Doctor',
        domain=lambda self: [('groups_id', 'in', self._get_groups())]
    )

    def _get_groups(self):
        return  [
            self.env.ref('pet_care_management.group_pet_doctor').id,
            self.env.ref('pet_care_management.group_groomer').id
        ]

    def create_appointment_wizard(self):
        vals = {
            'pet': self.pet.id,
            'appointment_date': self.appointment_date,
            'appointment_type': self.appointment_type,
            'pet_employee': self.pet_employee.id
        }
        self.env['pet.appointment'].create(vals)
        return {'type': 'ir.actions.act_window_close'}
