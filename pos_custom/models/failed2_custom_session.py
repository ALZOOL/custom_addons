from odoo import models, fields


class CustomSession(models.Model):
    _name = 'custom_session'
    _inherit = 'pos.session'
    _description = 'Custom Point Of Sales Session'


    pos_config_id = fields.Many2one('pos.config', string='Point of Sale', required=True)
    def get_session_data(self):
        orders_data = []
        for order in self.order_ids:
            for line in order.lines:
                orders_data.append({
                    'order_name': order.name,
                    'product_category': line.product_id.categ_id.name,
                    'product_name': line.product_id.name,
                    'product_code': line.product_id.default_code,
                    'quantity': line.qty,
                    'price_unit': line.price_unit,
                })

        payments_data = {
            'cash': 0.0,
            'bank': 0.0,
            'knet': 0.0,
        }

        for statement in self.statement_ids:
            journal_type = statement.journal_id.type
            if journal_type in payments_data:
                payments_data[journal_type] += statement.amount

        session_data = {
            'session_name': self.name,
            'start_time': self.start_at,
            'end_time': self.stop_at,
            'total_sales': self.total_payments_amount,
            'orders': orders_data,
            'payments': payments_data,
        }
        return session_data

    def print_session_report(self):
        session_data = self.get_session_data()

        # هنا يمكنك تخصيص طريقة عرض التقرير كما تفضل
        report_content = f"""
        POS Session Report
        ===================
        Session Name: {session_data['session_name']}
        Start Time: {session_data['start_time']}
        End Time: {session_data['end_time']}
        Total Sales: {session_data['total_sales']}

        Payments:
        Cash: {session_data['payments']['cash']}
        Bank: {session_data['payments']['bank']}
        K-NET: {session_data['payments']['knet']}

        Orders:
        """
        for order in session_data['orders']:
            report_content += f"""
            Order Name: {order['order_name']}
            Product Category: {order['product_category']}
            Product Name: {order['product_name']}
            Product Code: {order['product_code']}
            Quantity: {order['quantity']}
            Price Unit: {order['price_unit']}
            """

        return report_content