from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    semarnat_permit = fields.Char(string="Permiso SEMARNAT", help="Número de permiso ambiental para operar con residuos peligrosos.")
    semarnat_expiration = fields.Date(
    string="Fecha de expiración del permiso",
    help="Fecha en que expira el permiso SEMARNAT. Este campo es opcional."
)