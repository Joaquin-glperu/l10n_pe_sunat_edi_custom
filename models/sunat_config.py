from odoo import models, fields

class SunatConfig(models.Model):
    _name = 'sunat.config'
    _description = 'SUNAT API Configuration'

    name = fields.Char(string='Configuration Name', required=True)
    sunat_ruc = fields.Char(string='RUC', required=True)
    sunat_user = fields.Char(string='SOL Username', required=True)
    sunat_password = fields.Char(string='SOL Password', required=True)
    sunat_api_url = fields.Char(string='API URL', default='https://api.sunat.gob.pe/v1/contribuyente/gem')
    environment = fields.Selection([
        ('production', 'Production'),
        ('beta', 'Beta / Test'),
    ], string='Environment', default='beta')
