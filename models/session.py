from odoo import models, fields, api

class session(models.Model):
    _name = 'open_academy.session'
    _description = 'open_academy.session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    active = fields.Boolean(default=True)
    duration = fields.Integer()
    seats = fields.Integer()
    instructor = fields.Many2one(
        'res.partner',
        domain="""
            ['|',
                ('instructor', '=', True),
                ('category_id', 'child_of', ref('open_academy.cat_teacher'))
            ]
            """,
    )
    course_id = fields.Many2one('open_academy.course')
    attendees = fields.Many2many('res.partner')