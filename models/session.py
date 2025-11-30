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
    taken_seats_percent = fields.Float(
        compute="_compute_taken_seats",
        store=True
    )

    @api.depends('seats', 'attendees')
    def _compute_taken_seats(self):
        for record in self:
            if record.seats:
                record.taken_seats_percent = len(record.attendees) / record.seats * 100
            else:
                record.taken_seats_percent = 0