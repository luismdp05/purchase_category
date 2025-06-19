# -*- coding: utf-8 -*-

from odoo import models, fields


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    category_id = fields.Many2one(
        'purchase.category',
        string="Purchase Category",
        domain="[('id', 'in', allowed_category_ids)]"
    )

    def _compute_allowed_category_ids(self):
        for order in self:
            user = self.env.user
            order.allowed_category_ids = user.purchase_category_ids.ids

    allowed_category_ids = fields.Many2many(
        'purchase.category',
        compute='_compute_allowed_category_ids',
        string="Allowed categories",
    )