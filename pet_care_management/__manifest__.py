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
        'security/ir.model.access.csv',
        'security/groups.xml',

        'cron/cron_check_appointments.xml',
        'data/sequences.xml',

        'views/base.xml',
        'views/pets.xml',
        'views/pet_owners.xml',
        'views/appointments.xml',
        'views/health_card.xml',
        # 'views/vaccination.xml'
        'views/appointment_reports_template.xml',

        'report/appointment_reports.xml',
    ],
    'qweb': [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}