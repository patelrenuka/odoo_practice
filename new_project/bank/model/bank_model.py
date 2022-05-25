from odoo import models, fields,api,_
import random 

class bank_Details(models.Model):
    _name = "bank_details"
    inherit =['mail.thread','mail.activity.mixin']
    # _rec_name = "branch"
    _order = "id"

    name = fields.Char(string="Bank Name")
    branch = fields.Char(string="Branch Name")
    IFSC = fields.Char(string="Ifsc Code")
    account_no = fields.Integer(string="Account Number")
    bank_address = fields.Char(string="Address")
    phone_no = fields.Integer(string="Phone_Number")
    bank_types = fields.Selection([('private','private bank'),('government','government bank')], string="Bank Types")
    priority = fields.Selection([('0','Normal'),
                                ('1','Low'),
                                ('2','High'),
                                ('3','Very High')
                                ],string="Priority")
    progress = fields.Integer(string="Progress",compute="_compute_progress")
    _sql_constraints = [('unique_name','unique(name)','Please provide other name,Given name already exitss.')]




    # @api.depends('priority')
    # def _compute_progress(self):
    #     for rec in self:
    #         if rec.priority =="1":
    #             progress=25
    #         elif rec.priority =="2":
    #             progress=50
    #         elif rec.priority =="3":
    #             progress=100
    #         else:
    #             progress=0
    #         rec.progress=progress
    #   dynamically value  bellow

    @api.depends('priority')
    def _compute_progress(self):
        for rec in self:
            if rec.priority =="1":
                progress=random.randrange(0,25)
            elif rec.priority =="2":
                progress=random.randrange(25,99)
            elif rec.priority =="3":
                progress=100
            else:
                progress=0
            rec.progress=progress
            
    


