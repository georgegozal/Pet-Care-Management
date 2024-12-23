from odoo import models, fields, api
from odoo.exceptions import UserError


class PetAppointment(models.Model):
    _name = 'pet.appointment'
    _description = 'Pet Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    reference = fields.Char(
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: 'New'
    )
    pet = fields.Many2one(
        'pet.pet',
        string="Pet",
        required=True
    )
    owner = fields.Many2one(
        'res.partner',
        string="Owner",
        related="pet.owner"
    )
    appointment_date = fields.Datetime(string="Appointment Date & Time", required=True)
    appointment_type = fields.Selection([
        ('vet_checkup', 'Vet Check-up'),
        ('grooming', 'Grooming'),
        ('vaccination', 'Vaccination'),
        ('other', 'Other')
    ], string="Appointment Type", required=True)
    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')],
        string="Status",
        tracking=True
    )

    # def default_get(self, fields):
    #     res = super(PetAppointment, self).default_get(fields)
    #     res['state'] = 'scheduled'
    #     return res

    @api.model
    def create(self, vals):
        appointment_date = vals['appointment_date']
        existing_appointment = self.search([
            ('pet', '=', vals.get('pet')),
            ('appointment_date', '=', appointment_date)
        ])
        if existing_appointment:
            raise UserError("This pet already has an appointment scheduled at this time.")
        vals['reference'] = self.env['ir.sequence'].next_by_code('pet.appointment') or 'New'
        vals['state'] = 'scheduled'
        return super().create(vals)

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'
