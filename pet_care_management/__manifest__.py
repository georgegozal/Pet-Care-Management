{
    "name": "Pet Care Management",
    "author": "Giorgi Gozalishvili",
    "license": "LGPL-3",
    "version": "17.0.1.1",
    'category': 'Pet Care Management',
    'depends': [
        'mail'
    ],
    "data": [
        "security/ir.model.access.csv",
        'data/sequences.xml',
        'views/groups.xml',
        'views/base.xml',
        'views/pets.xml',
        'views/pet_owners.xml',
        'views/appointments.xml',
        'views/health_card.xml',
        # 'views/vaccination.xml'
    ],
    'qweb': [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}