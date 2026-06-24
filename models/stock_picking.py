from odoo import models, fields, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    partner_id = fields.Many2one(tracking=True)
    scheduled_date = fields.Datetime(tracking=True)
    origin = fields.Char(string='Source Document', tracking=True)

    invoice_count = fields.Integer(
        string='Invoice Count',
        compute='_compute_invoice_count',
        store=False
    )

    def _get_related_sale_orders(self):
        return self.env['sale.order'].search([
            ('name', 'in', self.mapped('origin'))
        ])

    def _get_related_invoices(self):
        sale_orders = self._get_related_sale_orders()
        return sale_orders.invoice_ids.filtered(
            lambda move: move.move_type in ('out_invoice', 'out_refund')
        )

    def _compute_invoice_count(self):
        for picking in self:
            picking.invoice_count = len(picking._get_related_invoices())

    def action_view_invoices(self):
        self.ensure_one()
        invoices = self._get_related_invoices()
        draft_invoices = invoices.filtered(lambda move: move.state == 'draft')
        if draft_invoices:
            draft_invoices.action_post()

        action = self.env['ir.actions.actions']._for_xml_id('account.action_move_out_invoice_type')
        action['domain'] = [('id', 'in', invoices.ids)]

        if len(invoices) == 1:
            action['views'] = [(self.env.ref('account.view_move_form').id, 'form')]
            action['res_id'] = invoices.id

        return action

    def button_validate(self):
        result = super().button_validate()
        for picking in self.filtered(lambda picking: picking.state == 'done' and picking._get_related_sale_orders()):
            if not picking.invoice_count:
                picking.action_create_invoice()
        return result

    def action_create_invoice(self):
        self.ensure_one()
        if self.state != 'done':
            raise UserError(_('Transfer must be done before creating invoice.'))

        sale_orders = self._get_related_sale_orders()
        if not sale_orders:
            raise UserError(_('No related sales order found.'))

        for sale_order in sale_orders:
            if sale_order.state not in ['sale', 'done']:
                raise UserError(_('Sales order must be confirmed.'))

        invoices = sale_orders._create_invoices()
        if not invoices:
            raise UserError(_('Could not create invoice. Check product invoicing policies.'))

        return False
