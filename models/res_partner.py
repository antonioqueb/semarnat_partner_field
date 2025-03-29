from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    semarnat_permit = fields.Char(string="Permiso SEMARNAT", help="Número de permiso ambiental para operar con residuos peligrosos.")
