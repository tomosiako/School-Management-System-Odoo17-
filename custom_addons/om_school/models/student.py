from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student Master'

    name = fields.Char(string="Name",required=True)
    date_of_birth = fields.Date(string="DOB")
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")