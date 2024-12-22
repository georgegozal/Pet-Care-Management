from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError, AccessError


class PetOwners(models.Model):
    _inherit = ['res.partner']
    _description = "Pet Owners"
    _order = 'id desc'

    reference = fields.Char(
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('New'))
    codice_fiscale = fields.Char(
        string="Codice Fiscale",
        size=16,
        copy=False,
        track_visibility="onchange",
        unique=True
    )
    pets = fields.One2many(
        'pc.pet',
        'owner',
        string="Pets"
    )

    @api.constrains('codice_fiscale')
    def _check_codice_fiscale_unique(self):
        print("Test")
        for rec in self:
            exists = self.search([('codice_fiscale', '=', rec.codice_fiscale), ('id', '!=', rec.id)], limit=1)
            if exists:
                raise ValidationError("The Codice Fiscale must be unique.")

    @api.model
    def create(self, vals):
        if 'reference' not in vals or vals['reference'] == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('res.partner') or _('New')
        return super(PetOwners, self).create(vals)
