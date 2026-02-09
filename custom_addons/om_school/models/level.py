from odoo import models, fields

class SchoolClass(models.Model):
    _name = 'school.level'
    _description = 'School Class'
    _inherit = ['mail.thread']

    name = fields.Char(required=True)
    code = fields.Char()
    class_teacher= fields.Many2one('school.employee')

    def action_generate_lessons(self):
        self.ensure_one()
        self.env['school.lesson'].generate_lessons(self.id)
