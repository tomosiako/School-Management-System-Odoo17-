from odoo import api, fields, models

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'Subject Master'

    name = fields.Char(string="Subject",required=True,tracking=True)
    subject_code = fields.Char(string="Code",tracking=True)
