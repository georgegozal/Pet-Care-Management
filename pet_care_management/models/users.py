from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError, AccessError


class Users(models.Model):
    _inherit = "res.users"

    codice_fiscale = fields.Char(
        string="Codice Fiscale",
        size=16,
        copy=False,
        track_visibility="onchange",
        unique=True
    )

    @api.constrains('codice_fiscale')
    def _check_codice_fiscale_unique(self):
        print("Test")
        for rec in self:
            exists = self.search([('codice_fiscale', '=', rec.codice_fiscale), ('id', '!=', rec.id)], limit=1)
            if exists:
                raise ValidationError("The Codice Fiscale must be unique.")
