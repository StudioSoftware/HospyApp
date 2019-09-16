# -*- coding: utf-8 -*-
{
    'name': "HOSPY APP",

    'summary': """
        Application de Gestion des Hopitaux""",

    'description': """
        C'est logiciel complet pour la gestion des hopitaux
    """,

    'author': "HOSPY TEAM",
    'website': "https://www.HOSPYTEAM.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'medical',
    'version': '0.1',

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
}