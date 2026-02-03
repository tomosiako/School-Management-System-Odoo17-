from odoo import api, fields, models

class SchoolMeeting(models.Model):
    _name = 'school.meeting'
    _inherit = ['mail.thread']
    _description = 'School Meeting'
    _rec_name = 'employee_id'

    reference = fields.Char(string='Reference', default='New')
    employee_id = fields.Many2one('school.employee', sytring="Employee")
    date_meeting = fields.Date(string="Date")
    note = fields.Text(string="Note")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('school.meeting')
            return super().create(vals_list)