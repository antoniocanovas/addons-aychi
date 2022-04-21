# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import base64

from odoo import fields, models, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class PosSession(models.Model):
    _inherit = 'pos.session'

    tips = fields.Monetary(string='Propinas', store=False, compute='get_pos_session_tips')

    def get_pos_session_tips(self):
        for record in self:
            if record.config_id.iface_tipproduct:
                if record.config_id.tip_product_id.id:
                    propina = 0
                    lines = self.env['pos.order.line'].search([('order_id.state', 'in', ['paid', 'done', 'invoiced']),
                                                               ('product_id', '=', record.config_id.tip_product_id.id),
                                                               ('order_id.session_id', '=', record.id)])
                    for li in lines:
                        propina += li.price_subtotal_incl
                    record.tips = propina
            else:
                record.tips = 0
