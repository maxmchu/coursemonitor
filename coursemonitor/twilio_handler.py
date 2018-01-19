# /usr/bin/env python

import os
import logging

from twilio.rest import Client

logger = logging.getLogger(__name__)

account_sid = os.environ.get("COURSEMONITOR_TWILIO_SID")
auth_token = os.environ.get("COURSEMONITOR_TWILIO_AUTH_TOKEN")
twilio_phone_number = os.environ.get("COURSEMONITOR_TWILIO_NUMBER")
own_phone_number = os.environ.get("COURSEMONITOR_OWN_NUMBER")



class TwilioHandler():

    def __init__(self):
        if not all([account_sid, auth_token, twilio_phone_number]):
            logger.error("Not all environment variables are configured!")
            return
        self.twilio_client = Client(account_sid, auth_token)

    def send_start_message(self, courseInfo):
        message = "CourseMonitor: {} term {}{} {} is now being monitored!".format(
            courseInfo.term, courseInfo.dept, courseInfo.course_num, courseInfo.section, courseInfo.status)
        sent_message = self.twilio_client.messages.create(
            own_phone_number,
            body=message,
            from_=twilio_phone_number
        )
        print("Message sent with sid {}", sent_message.sid)

    def send_update_message(self, courseInfo):
        message = "CourseMonitor: {} term {}{} {} is now {}!".format(
            courseInfo.term, courseInfo.dept, courseInfo.course_num, courseInfo.section, courseInfo.status)
        sent_message = self.twilio_client.messages.create(
            own_phone_number,
            body=message,
            from_=twilio_phone_number
        )
        print("Message sent with sid {}", sent_message.sid)