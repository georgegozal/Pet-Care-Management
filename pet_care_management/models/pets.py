from odoo import api, fields, models, _

class Pets(models.Model):
    _name = "pet.pet"
    _description = "Pets"
    _order = 'id desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    reference = fields.Char(
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('New'))
    name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Float(string="Age", digits=(16, 1), tracking=True)
    owner = fields.Many2one(
        'res.partner',
        string="Owner"
    )

    @api.model
    def create(self, vals):
        if 'reference' not in vals or vals['reference'] == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('pet.pet') or _('New')
        return super(Pets, self).create(vals)
