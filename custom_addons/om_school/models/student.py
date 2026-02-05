from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread']
    _description = 'Student Master'

    name = fields.Char(string="Name",required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB", tracking =True)
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender", tracking=True)
    guardian = fields.Many2one('school.guardian',String="Guardian")
    reference = fields.Char(string='Reference', default='New')
    # tag_ids = fields.Many2many(
    #     'student.tag','student_teg_rel','student_id','tag_id',string="Tags")               #defining the table column manual but the below line lets odoo do it automatically
    tag_ids = fields.Many2many('student.tag', string="Tags")
    subject = fields.Many2many('school.subject', string="Subjects Undertaken")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('school.student')
            return super().create(vals_list)