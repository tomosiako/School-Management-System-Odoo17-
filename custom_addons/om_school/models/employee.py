from odoo import api, fields, models,_
from odoo.exceptions import ValidationError,UserError

class SchoolEmployee(models.Model):
    _name = 'school.employee'
    _inherit = ['mail.thread']
    _description = 'Employee Master'

    name = fields.Char(string="Name",required=True,tracking =True)
    date_of_birth = fields.Date(string="DOB", tracking=True ,groups="om_school.group_school_management")
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender",tracking=True)
    id_number = fields.Char(string="ID Number",required=True,tracking=True)
    phone_number = fields.Char(string="Phone Number", required=True,tracking=True)
    is_teacher = fields.Boolean(string='Teacher')
    subject = fields.Many2many('school.subject', string="Subjects Taught")

    # def unlink(self):
    #     # can perform anything here
    #     for rec in self:
    #         domain = [('employee_id','=', rec.id)]
    #         appointments= self.env['school.meeting'].search(domain)
    #         if appointments:
    #             raise UserError(_("You can not delete the employee now. \nA meeting exists under this name: %s" % rec.name))
    #     return super().unlink()



    @api.ondelete(at_uninstall=False)  #this code serves the same purpose as the above code
    def _check_employee_meeting(self):
        for rec in self:
            domain = [('employee_id', '=', rec.id)]
            appointments = self.env['school.meeting'].search(domain)
            if appointments:
                raise UserError(
                    _("You can not delete the employee now. \nA meeting exists under this name: %s" % rec.name))
