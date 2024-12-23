from odoo import models, fields, api
from odoo.exceptions import UserError


class PetHealthCard(models.Model):
    _name = 'pet.passport'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    reference = fields.Char(
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: 'New'
    )

    pet = fields.Many2one(
        comodel_name='pet.pet',
        inverse_name='passport',
        string="Pet",
        required=True
    )

    image = fields.Binary("Image Binary", attachment=True, related='pet.image')
    owner = fields.Many2one(
        'res.partner',
        string="Owner",
        related="pet.owner"
    )
    vaccinations = fields.One2many(
        'pet.vaccination',
        'passport',
        string="Vaccinations"
    )
    age = fields.Float(string='Age', related='pet.age')
    pet_type = fields.Many2one(
        comodel_name='pet.type',
        string="Pet Type",
        related='pet.pet_type'
    )
    breed = fields.Char(string='Breed', related='pet.breed')
    sex = fields.Selection(string='Sex', related='pet.sex')
    microchip_id = fields.Char(string='Microchip ID')
    allergies = fields.Text(string='Alergies')
    note = fields.Text(string='Aditional Notes')

    @api.model
    def create(self, vals):
        vals['reference'] = self.env['ir.sequence'].next_by_code('pet.passport') or 'New'
        return super().create(vals)


class PetVaccination(models.Model):
    _name = 'pet.vaccination'

    passport = fields.Many2one(
        'pet.passport',
        string='Health Card'
    )
    name = fields.Char(string='Vacine Name', required=True)
    vaccination_type = fields.Selection(
        [
            ('rabies', 'Rabies'),
            ('distemper', 'Distemper'),
            ('parvo', 'Parvovirus'),
            ('hepatitis', 'Hepatitis'),
            ('lepto', 'Leptospirosis'),
            ('other', 'Other'),
        ],
        string="Vaccination Type",
        required=True
    )
    vaccination_date = fields.Date(string="Vaccination Date")
    next_due_date = fields.Date(string="Next Due Date")
    note = fields.Text(string="Notes")

    @api.model
    def default_get(self, fields_list):
        res = super(PetVaccination, self).default_get(fields_list)
        if not res.get("vaccination_date"):
            res['vaccination_date'] = fields.Date.today()
        return res
