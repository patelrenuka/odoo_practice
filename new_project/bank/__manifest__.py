# -*- coding: utf-8 -*-
{
    'name': "Bank",

    'summary': """
        Bank Details""",

    'description': """
       Bank Details
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
  # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
       "data/bank_data.xml",
       "view/bank_view.xml",
       "security/ir.model.access.csv",
       "security/security_access_bdata.xml",
       "reports/inherit_report_customer.xml"
    
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}
