# -*- coding: utf-8 -*-
{
    'name': "Customer",

    'summary': """
        Customer Information""",

    'description': """
       Customer Information
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','bank'],

    # always loaded
    'data': [
        "view/customer_view.xml",
        "security/ir.model.access.csv",
        "view/inherit_bank_view.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}
