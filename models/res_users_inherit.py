# -*- coding: utf-8 -*-

from odoo import models, fields


class ResUsersInherit(models.Model):
    _inherit = 'res.users'

    purchase_category_ids = fields.Many2many(
        'purchase.category',
        string='Allowed purchase categories'
    )
