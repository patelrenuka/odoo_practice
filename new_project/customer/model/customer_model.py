from email.policy import default
import string
from attr import field
from pkg_resources import require
from odoo import models, fields,api
from datetime import date,datetime
from dateutil import relativedelta
import phonenumbers
from odoo.exceptions import ValidationError
import re

class customer(models.Model):
    _name = "customer.details"
 
    customer_bank_name = fields.Char(string="Bank Name", readonly=True,default="SBI")
    customer_name = fields.Char(string="Name" ,help="This is Customer Name",size=14)
    customer_email = fields.Char(string="Email",require=True)
    phone_no = fields.Char(string="Phone_No")
    customer_address = fields.Char(string="address")
    birth_date = fields.Date(string="Birth_Date")
    age = fields.Integer(string="Age", compute="compute_age", inverse="_inverse_compute_age",store=True)
    aadhar_no = fields.Integer(string="Aadhar_No" )
    status = fields.Boolean(help="customer can be activate or deactivate your account")
    bank_id = fields.Many2one('bank_details',string="Bank")
    # select_bank_category =fields.Selection([('private','private banks'),('government','government banks')], string="Bank Category")
                                                    # bank_type id ifield of bank module
    bank_types =fields.Selection(related="bank_id.bank_types", string="Bank Category")
    refrence =fields.Reference(selection=[('bank_details','name'),
                                        ('customer.details','customer')],string="record")
    IFSC = fields.Char(string="Ifsc Code", related="bank_id.IFSC")
    state = fields.Selection([('draft','Draft'),
                            ('in_process','In_Process'),
                            ('done','Done'),
                            ('cancel','Cancelled')
                            ], default="draft", string="Status")
    
    
    @api.onchange('bank_id')
    def onchange_bank_id(self):
        if self.bank_id:
            if self.bank_id.bank_types:
                self.bank_types = self.bank_id.bank_types

    @api.depends('birth_date')
    def compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birth_date:
                rec.age = today.year - rec.birth_date.year
            else:
                rec.age=1

    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.birth_date = today - relativedelta.relativedelta(years=rec.age)

    @api.constrains('customer_name')
    def check_name(self):
        for rec in self:
            if len(rec.customer_name) < 4:
                raise ValidationError('name should be Four Characters')

    # state activate
    def action_in_process(self):
        for rec in self:
            rec.state = 'in_process'

    def action_done(self):
        for rec in self:
            rec.state = 'done'


    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

