from odoo import api, fields, models

class SchoolEmployee(models.Model):
    _name = 'school.employee'
    _inherit = ['mail.thread']
    _description = 'Employee Master'

    name = fields.Char(string="Name",required=True,tracking =True)
    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender",tracking=True)
    id_number = fields.Char(string="ID Number",required=True,tracking=True)
    phone_number = fields.Char(string="Phone Number", required=True,tracking=True)