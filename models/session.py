from odoo import models, fields, api

class session(models.Model):
    _name = 'open_academy.session'
    _description = 'open_academy.session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Integer()
    seats = fields.Integer()