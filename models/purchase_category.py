# -*- coding: utf-8 -*-

from odoo import models, fields


class PurchaseCategory(models.Model):
    _name = 'purchase.category'
    _description = 'Purchase Category'

    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')
