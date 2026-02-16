import random
from odoo import models, fields

class course(models.Model):
    _name = 'open_academy.course'
    _description = 'open_academy.course'

    title = fields.Char(required=True)
    description = fields.Char()
    responsible_user = fields.Many2one('res.users')
    sessions = fields.One2many('open_academy.session', 'course_id')

    _constraint_unique = models.Constraint(
        'unique(title)',
        'The title of the course must be unique.'
    )

    _constraint_check = models.Constraint(
        'check(title != description)',
        "The title of the course should not be the same as its description."
    )