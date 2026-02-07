from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'


    guardian_name=fields.Many2one('school.guardian',String='Payment Initiator')
    student_name = fields.Many2one('school.student', string="Student")