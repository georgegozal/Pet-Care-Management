from odoo import api, fields, models

class Pets(models.Model):
    _name = "pet.pet"
    _description = "Pets"
    _order = 'id desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    owner = fields.Many2one(
        'res.partner',
        string="Pets"
    )
