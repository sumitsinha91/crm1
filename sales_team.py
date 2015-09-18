# -*- coding: utf-8 -*-



from openerp import models, fields, api

class Course(models.Model):
     _name = "openacademy.course"
     
     title = fields.Char(string="Course Name", requried=True)
    #Reference= fields.Char(string="Reference", size=32, readonly=True, states={"draft":[("readonly",False)]})
     #week_year= fields.Char(string="week of year", size=24,readonly=True)
     #origin= fields.Char(string="Source Documents", readonly=True,help="Reference")
     details= fields.Char(string="Details", select=True)
     Report_name= fields.Char(string="Report Name",Requried=True,translate=True)
     number= fields.Char(string="Mobile Number", required=True, copy=False)
     password= fields.Char(string="Encrypted Password", invisible=True, copy=False)
     
     
     start_date = fields.Date()
     
     
     duration = fields.Float(digits=(6, 2), help="Duration in days")
     Balance= fields.Float(string="Balance",readonly=True)
     quantity= fields.Float(string="Subject Number", digits=(16,2), readonly=True)
     amount_currency= fields.Float(String="Amount Currency", help="The amount expressed")
     #purchase_value= fields.Float(string="Gross Value", required=True, readonly=True, states={"draft":[("readonly",False)]})
     planned_revenue= fields.Float(string="Course Fee", track_visibility="always")
     amount= fields.Float(string="Tax %", readonly=True, select=True)
     product= fields.Float(string="Amount ", copy=False)
     
     
     
     
   
     description1 = fields.Text(string="Title", requried=True)
     #description2 = fields.Text(string="Reference", size=32, readonly=True, states={"draft":[("readonly",False)]})
     #description2 = fields.Text(string="Week of year", size=24,readonly=True)
     #description3 = fields.Text(string="Source Documents", readonly=True,help="Reference")
     description4 = fields.Text(string="Details", required=True, select=True)
     description5 = fields.Text(string="Report Name",Requried=True,translate=True)
     description6 = fields.Text(string="Error Message", required=True)
     description7 = fields.Text(string="Encrypted Report Details", invisible=True, copy=False)
     
     

     
     title_Boolean = fields.Boolean(string="Check Box", requried=True)
     default_company= fields.Boolean(string="Default Active", readonly=True)
     active= fields.Boolean(string="Active", help="If the active field is set to False")
     #prorata=fields.Boolean(string="Prorata Temporis", readonly=True, states={'draft':[('readonly',False)]})
     
    
     

     
     
     seats = fields.Integer(string="Number of Seats",)
     number_opening= fields.Integer(string="Number of Units", help="Opening Unit Numbers")
     day_week= fields.Integer(string="Day of Week", size=24,readonly=True)
    # method_number= fields.Integer(string="Number of Depreciations", readonly=True, states={"draft":[("readonly",False)]})
     contact_number= fields.Integer(string="Contact Number", required=True, copy=False)
     name_company=fields.Integer(string="Number of Courses", required=True, select=True)
     
     
     

class Session(models.Model):
    _name = "openacademy.session"
    
    value = fields.Char(string="Title", requried=True)
    
    
    Matter = fields.Text()
    
    responsiable_id = fields.Many2one("res.partner", string= "Instructor")
    course_id = fields.Many2one("openacademy.course",
            ondelete="cascade",string="course",required=True)
    
    time = fields.Boolean(string="Time", requried=True)
    
    
    
    second = fields.Integer(string="second", requried=True)
    
    
    minutes = fields.Float(string="minutes", requried=True)
 
    
    