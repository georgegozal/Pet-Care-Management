from odoo import fields, models, api
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)


class  CheckPetAppointment(models.Model):
    _inherit = 'pet.appointment'

    @api.model
    def cron_check_appointment_date(self):
        next_day = datetime.now().day + 1
        appointments = self.search([]).filtered(
            lambda a: a.appointment_date.day == next_day
        )
        if appointments:
            _logger.info(f"\33[35;1m Display Next Day Appointments {appointments.read(['reference'])} \33[0m")
            for appointment in appointments:
                # TODO: Here we can implement sending email or sending sms functionality
                # self.send_mail()
                pass
