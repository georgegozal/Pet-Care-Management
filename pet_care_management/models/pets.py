from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError, AccessError
import logging

_logger = logging.getLogger(__name__)


class Pets(models.Model):
    _name = "pet.pet"
    _description = "Pets"
    _order = 'id desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    reference = fields.Char(
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: 'New'
    )
    name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Float(string="Age", digits=(3, 1), tracking=True)
    owner = fields.Many2one(
        'res.partner',
        string="Owner"
    )
    image = fields.Binary("Image Binary", attachment=True)

    pet_type = fields.Many2one('pet.type', string="Pet Type")
    breed = fields.Char(string="Breed", tracking=True)
    sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ],string='Sex')

    appointments = fields.One2many(
        comodel_name='pet.appointment',
        inverse_name='pet',
        string='Appointments'
    )

    passport = fields.One2many(
        comodel_name='pet.passport',
        inverse_name='pet',
        string='Health Card',
        help="Health card (passport) records for this pet."
    )
    readonly_values = fields.Boolean(compute='_compute_readonly_values')

    def _compute_readonly_values(self):
        for rec in self:
            if self.env.user.has_group('pet_care_management.group_pet_manager'):
                rec.readonly_values = True
            else:
                rec.readonly_values = False

    @api.model
    def create(self, vals):
        if 'reference' not in vals or vals['reference'] == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code('pet.pet') or 'New'
        return super(Pets, self).create(vals)

    @api.depends('reference', 'name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f'{rec.reference} - {rec.name}'
            # rec.display_name = f'{rec.name} . {rec.owner.name}'
            _logger.info(f"\33[35;1m Display name computed for record {rec.id}: {rec.display_name} \33[0m")

    def action_appointments(self):
        create_appointment = self.env.context.get('create_appointment')
        return {
            'type': 'ir.actions.act_window',
            'name': 'Create Appointments' if create_appointment else 'See Appointments',
            'res_model': 'pet.appointment',
            'domain': [('pet', '=', self.id)],
            'context': {
                'default_pet': self.id,
                'pet_readonly': True,
                'tree_create': 0
            },
            'view_type': 'form' if create_appointment else 'tree',
            'view_mode': 'form' if create_appointment else 'tree',
            'target': 'new',
        }

    def get_appointments_report(self):
        return self.env.ref(
            'pet_care_management.report_pet_appointments'
        ).with_context(dict(discard_logo_check=True)).report_action(self)


class PetType(models.Model):
    _name = 'pet.type'

    name = fields.Char(string="Pet Type", unique=True)
    pets = fields.One2many('pet.pet', 'pet_type', string="Pets")

    @api.model
    def create(self, vals):
        name = vals.get("name")
        if name:
            exists = self.search([('name', '=', name.lower()), ('id', '!=', self.id)], limit=1)
            if not exists:
                vals["name"] = name.lower()
                return super(PetType, self).create(vals)
        raise UserError(f"Pet Type < {name} > Already Exsists!")