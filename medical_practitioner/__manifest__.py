# -*- coding: utf-8 -*-
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

{
    'name': 'Medical Practitioner',
    'version': '11.0.1',
    'summary': 'Defines medical practioners',
    'author': 'HOSPY TEAM',
    'license': 'GPL-3',
    'category': 'Medical',
    'depends': [
        'medical',
        'hr',
    ],
    'data': [
        'data/ir_sequence.xml',
        'data/medical_role.xml',
        'data/medical_specialty.xml',
        'security/ir.model.access.csv',
        'views/medical_practitioner.xml',
        'views/medical_role.xml',
        'views/medical_menu.xml',
        'views/medical_specialty.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
