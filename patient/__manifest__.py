# -*- coding: utf-8 -*-
{
    'name': "patient",

    'summary': """
      Gestion de Patient""",

    'description': """
        Ce module est une extension de l'application HOSPY APP qui gere le Patient de son admission
        jusqu'a la sortie
    """,

    'author': "HOSPY TEAM",
    'website': "htpps://www.HOSPYTEAM.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Medical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'base_locale_uom_default',
        ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/Patient_views.xml',
        'views/Patient_menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}