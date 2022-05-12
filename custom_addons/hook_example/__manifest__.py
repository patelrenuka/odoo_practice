# -*- coding: utf-8 -*-
{
    'name': "Hook Examples",

    'summary': """
        Odoo provides 4 types of hook here is the examples.""",

    'description': """
        Odoo hook tutorials
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorials',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [
        
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
                    #  "Method name"
    'pre_init_hook':'_weblearns_pre_init_hook',
    'post_init_hook':'_weblearns_post_init_hook',
    'uninstall_hook':'_weblearns_uninstall_hook',
    'post_load':'_weblearns_post_load_hook'
}
