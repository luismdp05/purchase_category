# -*- coding: utf-8 -*-
{
    'name': 'Purchase Category',
    'version': '17.0.1.0.0',
    'summary': 'Extend purchase orders with categorization and access control',
    'description': 'Add a categorization field to purchase orders and control visibility based on user status and permissions.',
    'author': 'luismdp05',
    'website': '',
    'category': 'Purchase',
    'depends': ['base', 'purchase'],
    "data": [
        "security/purchase_security.xml",
        "security/ir.model.access.csv",
        "views/purchase_category_views.xml",
        "views/purchase_order_views.xml",
        "views/res_users_views.xml"
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
