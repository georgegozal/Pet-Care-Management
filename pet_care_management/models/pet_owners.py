from pprint import pprint

from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError, AccessError


class PetOwners(models.Model):
    _inherit = ['res.partner']
    _description = "Pet Owners"
    _order = 'id desc'

    reference = fields.Char(
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: 'New'
    )
    codice_fiscale = fields.Char(
        string="Codice Fiscale",
        size=16,
        copy=False,
        track_visibility="onchange",
        unique=True
    )
    pets = fields.One2many(
        'pet.pet',
        'owner',
        string="Pets"
    )
    is_client = fields.Boolean(string='Is Client', default=False)

    @api.constrains('codice_fiscale')
    def _check_codice_fiscale_unique(self):
        for rec in self:
            exists = self.search([('codice_fiscale', '=', rec.codice_fiscale), ('id', '!=', rec.id)], limit=1)
            if exists:
                raise ValidationError("The Codice Fiscale must be unique.")

    @api.model
    def create(self, vals):
        pprint(vals)
        if vals.get('is_client'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('res.partner') or 'New'
        return super(PetOwners, self).create(vals)
