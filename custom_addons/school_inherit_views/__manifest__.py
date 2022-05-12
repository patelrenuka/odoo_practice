# -*- coding: utf-8 -*-
{
    'name': "School Inherit Views",

    'summary': """
        Creating different view inheritance tests cases.""",

    'description': """
        Creating different view inheritance tests cases.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','school','school_student'],

    # always loaded
    'data': [
        "views/student_extend_view.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
       
    ],
}