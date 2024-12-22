from odoo import api, fields, models


class PetOwners(models.Model):
    _inherit = "res.partner"
    _description = "Pet Owners"


    pets = fields.One2many(
        'pet.pet',
        'owner',
        string="Pets"
    )
