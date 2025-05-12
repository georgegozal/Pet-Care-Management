{
    "name": "Pet Care Management",
    "author": "Giorgi Gozalishvili",
    "license": "LGPL-3",
    "version": "17.0.1.1",
    'category': 'Pet Care Management',
    'depends': [
        'mail',
        'product',
        'sale',
        'account',
    ],
    "data": [
        'security/groups.xml',
        'security/ir.model.access.csv',

        'cron/cron_check_appointments.xml',
        'data/sequences.xml',
        'data/products.xml',

        'wizard/appointments.xml',

        'views/base.xml',
        'views/pets.xml',
        'views/pet_owners.xml',
        'views/appointments.xml',
        'views/health_card.xml',
        # 'views/vaccination.xml'

        'report/appointment_reports_template.xml',
        'report/appointment_reports.xml',
    ],
    'qweb': [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}