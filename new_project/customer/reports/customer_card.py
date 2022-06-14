from odoo import api, models,_

class CustomerCardReport(models.AbstractModel):
    _name = 'report.customer.customer_report'
    _description = 'Customer Card Report'

    @api.model
    def _get_report_values(self, docids,data=None):
        print(docids)
        docs = self.env['customer.details'].browse(docids[0])
        cust_list=[]
        for app in docs:
            vals={
                'customer_name':app.customer_name,
                'age':app.age,
                'bank_id':app.bank_id
            }
            cust_list.append(vals) 
            print(cust_list)
        return {
            'doc_model':'customer.details',
            'data':data,
            'docs':docs,
            'cust_list':cust_list,
        }