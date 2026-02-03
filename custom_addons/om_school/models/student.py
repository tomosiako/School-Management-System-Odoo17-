from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread']
    _description = 'Student Master'

    name = fields.Char(string="Name",required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB", tracking =True)
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender", tracking=True)