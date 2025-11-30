import random
from odoo import models, fields

class course(models.Model):
    _name = 'open_academy.course'
    _description = 'open_academy.course'

    title = fields.Char(required=True)
    description = fields.Char()
    responsible_user = fields.Many2one('res.users')
    sessions = fields.One2many('open_academy.session', 'course_id')