# -*- coding: utf-8 -*-

from calendar import weekday
from email.policy import default
from locale import currency
from random import Random
import random
from turtle import right
from odoo import models, fields,api
from datetime import datetime,date
from lxml import etree
from odoo.exceptions import UserError
from odoo import _


class Partner(models.Model):
    _inherit = "res.partner"

    def hello_hook(self):
        print("hello hook")
        for contact in self.search([]):
            print(contact.display_name)
            

class Address(models.Model):
    _name = "address"
    _rec_name= "street"
    # _order = "name,id desc"
    # in database created date automatically so this record is not show in database so used log access attribute
    # _log_access = False
    

    street = fields.Char("Street")
    street_one = fields.Char("Street1")
    city = fields.Char("City")
    state = fields.Char("State")
    country = fields.Char("Country")
    zip_code = fields.Char("Zip_Code")

class log_access_sttribute_class(models.Model):
    _name = "log.access.attribute.class"
    _log_access = False

    name = fields.Char(string="Name")

class school_student(models.Model):
    _name = 'school_student.school_student'
    _inherit = "address"
    _description = 'school_student.school_student'
    # in database created date automatically so this record is not shiw in database so used log access attribute
    # _log_access = False
    _order = "student_sequence"
    name = fields.Char(default="mahima")
    school_id = fields.Many2one("school.profile",string="school",
                                # domain="[('school_type','=','private'),('virtual_class','=',True)]" 

                                # right side sub fields odoo doesn't support bellow domain
                                # domain="[('currency_id','=',currency_id)]"
                                
                                # left side sub fields you can access like this way
                                # domain="[('currency_id.name','=',EUR)]"
                                
                                )
    state = fields.Selection([('draft',"Draft"),
                               ('progress','Progress'),
                               ('paid','Paid'),
                               ('done','Done')], string="State")
    student_image = fields.Image("Student Image")
    bdate = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", readonly=True)
    description= fields.Html(string="Description")
    roll_number = fields.Char(string="Student Roll Number")
    is_virtual_school = fields.Boolean(related="school_id.virtual_class",string="Is Virtual Class",store=True)
    hobby_list = fields.Many2many("hobby", "school_hobby_rel","student_id",
                                  "hobby_id", string="Hobby List",
                                  )
    currency_id = fields.Many2one("res.currency",string="Currency")
    student_fees = fields.Monetary(string="Students Fees")
    total_fees = fields.Float(string="Total Fees")
    ref_id = fields.Reference([('school.profile','School'),('school_student.school_student','name'),('account.move','Invice')],string="Reference Field")

    _sql_constraints = [('unique_name','unique(name)','Please provide other student name.Given name already exitss.'),
                        ('total_fees_check', 'check(total_fees >100)', 'minimum 101 amount allow.')
                        ]
    # add drag drop features
    student_sequence = fields.Integer("Student Sequence", default=10)

    def buttonClickEvent(self):
        raise UserError(_("You click this Button....."))

    def specialcommand6(self):
        ids =[1,3,4]
        self.write({'hobby_list':[(6,0,ids)]})

    # bellow onchange define used to first school id selected then currency is select to currency option is show to school id related data but schoolid is not selected then currency is empty

    @api.onchange('school_id')
    def _onchange_school_profile(self):
        currency_id = 0
        if self.school_id:
            currency_id = self.school_id.currency_id.id
        return {"domain":{'currency_id':[('id','=', currency_id)]}}


    @api.model 
    def _change_roll_number(self):
        for stud in self.search([('roll_number','=',False)]):
            stud.roll_number = "STU"+str(stud.id)

    @api.constrains('bdate')
    def _check_age(self):
        for rec in self:
            if rec.bdate:
                today = date.today()
                rec.age =(today.year - rec.bdate.year - ((today.month,today.day) < (rec.bdate.month,rec.bdate.day)))

    def wiz_open(self):

        return {'type':'ir.actions.act_window',
                'res_model':'student.fees.update.wizard',
                'view_mode':'form',
                'target':'new'}

    def custom_button_method(self):
        # redirect to another page
        return {

            'type':'ir.actions.act_url',
            # 'url':'https://www.google.com',
            # 'url':'http://localhost:8069/web#action=88&model=school_student.school_student&view_type=pivot&cids=1&menu_id=75'
            'url':'/web#action=88&model=school_student.school_student&view_type=pivot&cids=1&menu_id=75'
            # 'target':'self'
        }
        # print("Hello this is custom method colled by you....",self)
        # self.total_fees = random.randint(1,1000)

    def custom_method(self):
        self.ensure_one()
        print(self.name)
        print(self.school_id.name)
    
    # @api.model
    # def fields_view_get(self,view_id=None,view_type='form',toolbar=False,submenu=False):
        
    #     res= super(school_student,self).fields_view_get(view_id=view_id,view_type=view_type,toolbar=toolbar,submenu=submenu)
    #     if view_type =="form":
    #         doc = etree.XML(res['arch'])
    #         name_field = doc.xpath("//field[@name='name']")
    #         if name_field:
    #             name_field[0].addnext(etree.Element('label',{'string':'Hello this is custom label from fields_view_get_method'}))
    #             res['arch'] = etree.tostring(doc,encoding='unicode')
            
    #         if view_type == 'tree':
    #             doc = etree.XML(res['arch'])
    #             school_field = doc.xpath("//field[@name='school_id']")
    #             if school_field:
    #                 school_field[0].addnext(etree.Element('field',{'string':'Total Fees','name':'total_fees'}))
    #             res['arch'] = etree.tostring(doc,encoding='unicode')

    #     return res            
           
           
        

    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

class SchoolProfile(models.Model):
    _inherit =  "school.profile"
    school_list = fields.One2many("school_student.school_student","school_id",string="school_list")   
    # school_number = fields.Char("School Code")


    @api.model
    def name_search(self,name, args=None, operator='ilike', limit=100):
        args = args or []
        # print("Name",name)
        # print("Args",args)
        # print("Operators",operator)
        # print("limit",limit)
        if name:
            records=self.search(['|','|',('name', operator, name),('email', operator, name),('school_type', operator, name)])
            return records.name_get()
        # return self.search([('name',operator,name)]+args, limit=limit).name_get()  or
        return super(SchoolProfile,self).name_search(name=name,args=args,operator=operator,limit=limit)

        # orrr

    # @api.model
    # def _name_search(self,name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     args = args or []
    #     domain = []
    #     args = args or []
    #     print("Name",name)
    #     print("Args",args)
    #     print("Operators",operator)
    #     print("limit",limit)
    #     if name:
    #         domain =['|','|',('name', operator, name),('email', operator, name),('school_type', operator, name)]
    #     school_ids = self.search(domain+args, limit=limit)
    #     return school_ids.name_get()



class hobbies(models.Model):
    _name = "hobby"

    name = fields.Char("Hobby")

class SchoolStudent(models.Model):
    _inherit = 'school_student.school_student'

    parent_name=fields.Char("Parent Name")

class Car(models.Model):
    _name ="car"

    name = fields.Char("Car Name")
    price = fields.Float("Cost")

class CarEngine(models.Model):
    _name = "car.engine"
    _inherits = {"car":"car_id"}

    # {"key_is_modelname":"value_is_fieldnameofmany2one"}

    name = fields.Char("Car Engine Name")
    car_id = fields.Many2one("car", string="Car" ) 

