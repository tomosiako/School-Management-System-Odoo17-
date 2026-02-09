from odoo import api, fields, models


from odoo import models, fields, api

class SchoolLesson(models.Model):
    _name = 'school.activity'
    _description = 'School Activity'
    _inherit = ['mail.thread']



    name= fields.Char(required=True, tracking=True,string='Activity Name')
    date = fields.Date(    required=True, tracking=True ,string='Date' )
    description = fields.Char(string='Activity Description')
    start_time= fields.Datetime(string='Start Time',required=True)
    end_time = fields.Datetime(string="Stop Time")


