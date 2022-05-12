from odoo import api,models,fields

class StudentFeesUpdateWizard(models.TransientModel):
    _name = "student.fees.update.wizard"

    total_fees = fields.Float(string="Fees")

    def update_student_fees(self):
        print("Yeah successfully click on update_student_fees method.......")

        self.env['school_student.school_student'].browse(self._context.get("active_ids")).update({'total_fees':self.total_fees})
        return True


class StudentFeesUpdateExtendWizard(models.TransientModel):
    _inherit = "student.fees.update.wizard"

    parent_name = fields.Char(string="Parent Name")
    # without super statement
    # def update_student_fees(self):
    #     print("This is enherited def update_student_fees(self):method........")

    #     return True

    # with super statement

    def update_student_fees(self):
        print("This is enherited def update_student_fees(self):method........")

        return super(StudentFeesUpdateExtendWizard,self).update_student_fees()