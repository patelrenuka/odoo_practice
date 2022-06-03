import odoorpc

odoo = odoorpc.ODOO('localhost', port=8069)
print(odoo.db.list())

odoo.login('newprodb', 'admin', 'admin')

user = odoo.env.user
print("User Name....",user.name)            # name of the user connected
print("Company Name....",user.company_id.name) 

if 'customer.details' in odoo.env:
    custsomer_lead = odoo.env['customer.details'].search([])
    # for lead in custsomer_lead:
    #     print("data....",lead)
    #     rec = odoo.env['customer.details'].browse(lead)
    #     print(".......data......",rec.customer_name)
    #     rec.write({'phone_no':'1241234'})

    rec_delete = odoo.env['customer.details'].search([('customer_name','=','kritika')])
    print(".....data",rec_delete)
    customer_record_delete = odoo.env['customer.details'].browse(rec_delete)
    customer_record_delete.unlink()