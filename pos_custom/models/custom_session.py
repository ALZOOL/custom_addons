from odoo import models, fields, api

class POSCustomSession(models.Model):
    _name = 'custom_session'
    _inherit = 'pos.session'
    _description = 'Custom Point Of Sales Session'

    #has_refundable_lines = fields.Boolean(string="Has Refundable Lines", compute='_compute_has_refundable_lines')
    #def _compute_has_refundable_lines(self):
     #   for session in self:
      #      session.has_refundable_lines = any(line.qty > 0 for line in session.order_ids.mapped('lines'))
    def generate_pdf_report(self):
        # استدعاء التقرير باستخدام QWeb
        return self.env.ref('point_of_sale.report_pos_session').report_action(self)

    #def action_pos_order_invoice(self):
     #   # استدعاء الدالة من الموديل الموروث
      #  result = super(POSCustomSession, self).action_pos_order_invoice()
       # # يمكنك إضافة كود إضافي هنا إذا لزم الأمر
        #return result

    #def refund(self):
     #   # هنا يجب تعريف الإجراء الخاص بالاسترداد (refund)
      #  # يمكنك كتابة الكود المناسب لإجراء الاسترداد
       # pass