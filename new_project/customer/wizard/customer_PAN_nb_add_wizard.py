from odoo import models, fields,api,_

class Pan_number_wizard(models.TransientModel):
    _name = 'pan_number.wizard'
    _description ='added pan number'

    pan_number = fields.Integer(string="PAN number")
    customer_name = fields.Char(string="Name" ,help="This is Customer Name",size=14)

    def action_create_pan(self):
        print("Buttons Is Clicked......")
