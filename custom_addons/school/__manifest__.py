{
    'name':'School',
    'version':'1.1',
    'summary':"School Management System",
    'sequence':1,
    'description':"This is school management system software supported in odoo v15",
    'category':'school',
    'website':'https://www.odoo.com/app/school',
    'depends':['base'],
    'data':[
        "data/school_data.xml",
        "security/security_access_data.xml",
        "security/ir.model.access.csv",
        "views/school_view.xml",
       
       

    ],
    # 'demo':["demo/school_demo_data.xml",

    # ]

    
}