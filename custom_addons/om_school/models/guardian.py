from odoo import api, fields, models

class SchoolGuardian(models.Model):
    _name = 'school.guardian'
    _inherit = ['mail.thread']
    _description = 'Guardian Master'

    name = fields.Char(string="Name",required=True, tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender", tracking=True)
    phone = fields.Char(string="Phone",required=True,tracking=True)
    id_number = fields.Char(string="ID Number", required=True,tracking =True)