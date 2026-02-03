from odoo import api, fields, models

class SchoolEmployee(models.Model):
    _name = 'school.employee'
    _description = 'Employee Master'

    name = fields.Char(string="Name",required=True)
    date_of_birth = fields.Date(string="DOB")
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")
    id_number = fields.Char(string="ID Number",required=True)
    phone_number = fields.Char(string="Phone Number", required=True)