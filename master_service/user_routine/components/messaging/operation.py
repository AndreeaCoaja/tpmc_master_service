from master_service.api_category_conn import messaging
from ..base.operation import Operation


class MessagingOperation(Operation):

    def __init__(self, id, recepient_email_address, subject, text):
        super().__init__(id, "messaging")

        self.recepient_email_address = recepient_email_address
        self.subject = subject
        self.text = text

    # When the operation is executed the email is sent via the email category API service
    def execute(self):
        messaging.send_email(self.recepient_email_address, self.subject, self.text)
