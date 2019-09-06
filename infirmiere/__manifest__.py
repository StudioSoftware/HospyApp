# -*- coding: utf-8 -*-
{
    'name': "infirmiere",

    'summary': """
        Gestion des infirmiere sous 11, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Gestion des patients à l'hopital coeur et vie
    """,

    'author': "mvondoyannick",
    'website': "http://www.odoo-cm-team.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'coeur & vie',
    'version': '0.1.2.1a',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "installable": True,
    "application": True,
}