from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = 'student.tag'
    _description = 'Student Tag'

    name = fields.Char(string="Name",required=True, tracking=True)
    sequence = fields.Integer(default=10)