from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError, AccessError


class Pets(models.Model):
    _name = "pc.pet"
    _description = "Pets"
    _order = 'id desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    reference = fields.Char(
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('New'))
    name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Float(string="Age", digits=(3, 1), tracking=True)
    owner = fields.Many2one(
        'res.partner',
        string="Owner"
    )
    image = fields.Binary("Image Binary", attachment=True)

    pet_type = fields.Many2one('pc.pet.type', string="Pet Type")
    breed = fields.Char(string="Breed", tracking=True)
    sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ],string='Sex')

    @api.model
    def create(self, vals):
        if 'reference' not in vals or vals['reference'] == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('pc.pet') or _('New')
        return super(Pets, self).create(vals)


class PetType(models.Model):
    _name = 'pc.pet.type'

    name = fields.Char(string="Pet Type", unique=True)
    pets = fields.One2many('pc.pet', 'pet_type', string="Pets")

    @api.model
    def create(self, vals):
        name = vals.get("name")
        if name:
            exists = self.search([('name', '=', name.lower()), ('id', '!=', self.id)], limit=1)
            if not exists:
                vals["name"] = name.lower()
                return super(PetType, self).create(vals)
        raise UserError(f"Pet Type < {name} > Already Exsists!")