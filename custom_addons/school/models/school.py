from odoo import fields,models,api


class SchoolProfile(models.Model):
    _name = 'school.profile'
    # _rec_name = 'phone'
    _order = "school_seq"
    
    school_seq_name = fields.Char("School Code", readonly="1")
    name= fields.Char(string="School Name",help="this is school name",required=True)
    email= fields.Char(string="Email")
    phone= fields.Char("Phone")
    currency_id = fields.Many2one("res.currency",string="Currency")
    virtual_class= fields.Boolean(string="Virtual class support",
                                help="this is boolean flag which will"
                                "help you to see virtual class"
                                "support or not" )
    school_rank= fields.Integer(string="Rank")
    result= fields.Float(string="result", help="this is tool tip ",
                         default=1.1,digits=(2,3))
    address= fields.Text(string="Address", help="This is school perment address") 
    date= fields.Date(string="Establish Date")
    datetime= fields.Datetime(string="open datetime",default=fields.Datetime.now())
    school_type= fields.Selection([('public','public school'),('private','private school')], string="Type of string")
    document= fields.Binary(string="file upload")
    document_name= fields.Char(string="file name")
    school_image= fields.Image(string="Upload Ichool Image",max_width=100,max_height=100)
    
    _sql_constraints=[('name_unique','unique(name)','Please enter unique school name,Given school name already exit.')]

    school_seq = fields.Integer("School Sequence")
    
    # textarea widget

    school_description= fields.Html(string="Description")
    auto_rank = fields.Integer(compute="_auto_rank_populate",string="Auto Rank",store=True,help="Thos is auto populate date based on school type change")
    
    @api.depends('school_type')
    def _auto_rank_populate(self):
        for rec in self:
            if rec.school_type =="private":
                rec.auto_rank = 50
            elif rec.school_type == "public":
                rec.auto_rank = 100
            else:
                rec.auto_rank = 0

    def name_get(self):
        student_list = []
        for school in self:
            name = school.name
            if school.school_type:
                name +="({})".format(school.school_type)
            student_list.append((school.id,name))
        return student_list
    

    @api.model
    def create(self,vals):
        print("School Profile Value",vals)
        # sequence id dispaly then this bello one line write 
        vals['school_seq_name'] = self.env['ir.sequence'].next_by_code("school.profile")
        return super(SchoolProfile, self).create(vals)

    def write(self,vals):
        print("School Profile Value",vals)
        return super(SchoolProfile, self).write(vals)


        # First way to create child model for existing parent model .......(0,0,vals)
    def specialcommand(self):
        # student_obj =self.env['school_student.school_student']
        # stud_id = student_obj.create({'name':"newStudent two",'school_id':self.id})

        # # parent model and child model
        # school_id = self.create({"name":"crecket team2"})
        # student_obj.create({'name':"player 21",'school_id':school_id.id})
        # student_obj.create({'name':"player 22",'school_id':school_id.id})
        # student_obj.create({'name':"player 23",'school_id':school_id.id})
        # student_obj.create({'name':"player 24",'school_id':school_id.id})
        # student_obj.create({'name':"player 25",'school_id':school_id.id})

        # Using special command

        self.create({"name":"trisha","school_list":[(0,0,{'name':"stu1"}),(0,0,{'name':"fstu2"}),(0,0,{'name':"fstu3"}),(0,0,{'name':"fstu4"}),(0,0,{'name':"fstu5"})

                    ]})

        # Using write methode create child model using parent method

        # self.write({"school_list":[[0,0,{'name':'trishu'}]]})

        
    # Update- 1,ids,vals

    #no used this command
    def specialcommand1(self):
    #     for student in self.school_list:
    #         student.name = student.name + "" +str(student.id)
    #         student.total_fees = 3600
    #         student.student_fees = 1200
        
        # We can used this commandwhile doing update operation for parent and child model
        # vals = {'school_list':[]}
        # for student in self.school_list:
        #     vals['school_list'].append([1,student.id,{'name':student.name +"Name",'total_fees':400,"student_fees":4500}])
        # self.write(vals)
   
        # We can used this instead of special commands
        for student in self.school_list:
            student.write({'name':student.name + "12345",'total_fees':251,'student_fees':6500})

    
    # Delete record permanantaly-(2,id,0)
    def specialcommand2(self):
        self.write({'school_list':[(2,60,0),(2,61,0)]})      


    # Delect specific record but not permanantaly-(3,id,0)
    def specialcommand3(self):
        self.write({'school_list':[(3,53,False)]})  

    # Add existing records in relational field
    def specialcommand4(self):
        self.write({'school_list':[(4,73,0)]})

    # Delete all record but not permanantaly
    def specialcommand5(self):
        self.write({'school_list':[(5,0,0)]})


class SchoolStudentProfile(models.Model):
    _name = "school.student.profile.security.example"
    _description ="This is the demo of access right tutorial."

    name = fields.Char("Name")
    email = fields.Char("Email")
    phone = fields.Char("Phone")