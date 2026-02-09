from odoo import api, fields, models


from odoo import models, fields, api

class SchoolLesson(models.Model):
    _name = 'school.lesson'
    _description = 'School Lesson'
    _inherit = ['mail.thread']
    _rec_name = 'subject'



    level = fields.Many2one('school.level',required=True, tracking=True,string='Class')
    subject = fields.Many2one(   'school.subject', required=True, tracking=True ,string='Subject' )
    teacher = fields.Many2one('school.employee',string='Teacher',domain="[('subject', '=', subject)]"
    )
    #teacher = fields.Many2one('school.employee',string='Teacher')
   # student = fields.Many2many(string="Students", related="subject.student")


