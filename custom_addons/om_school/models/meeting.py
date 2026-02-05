from odoo import api, fields, models

class SchoolMeeting(models.Model):
    _name = 'school.meeting'
    _inherit = ['mail.thread']
    _description = 'School Meeting'
    _rec_names_search = ['reference','employee_id']
    _rec_name = 'employee_id'

    reference = fields.Char(string='Reference', default='New')
    employee_id = fields.Many2one('school.employee', sytring="Employee")
    date_meeting = fields.Date(string="Date")
    time = fields.Datetime(string="Scheduled Date")
    note = fields.Text(string="Note")
    state = fields.Selection([
        ('draft','Draft'),('confirmed','Confirmed'),('ongoing','Ongoing'),
        ('done','Done'),('canceled','Cancelled')
    ],default="draft",tracking = True)
    members = fields.Many2many('school.employee', string="Meeting Member")


    # computed field testing variable

    a = fields.Integer(string="Quantity")
    b = fields.Integer(string="price")
    #b = fields.Float(string="Price")

    total_quantity = fields.Float(compute='_compute_total_quantity',string='Total Quantity',stored=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('school.meeting')
            return super().create(vals_list)

    def _compute_total_quantity(self):
        for rec in self:
           total_qty =0
           total_qty=rec.a+rec.b
           rec.total_quantity =total_qty

    def action_confirm(self):
        for rec in self:
            rec.state="confirmed"


    def action_ongoing(self):
        for rec in self:
            rec.state = "ongoing"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_cancel(self):
        for rec in self:
            rec.state = "canceled"