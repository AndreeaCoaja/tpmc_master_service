from OperationClass import Operation


class MessagingOperation(Operation):

    def __init__(self, recepient_email_adress, subject, text):
        self.recepient_email_adress = recepient_email_adress
        self.subject = subject
        self.text = text

# When the operation is executed the email is sent via the email category API service
    def execute(self):
        messaging.send_email(self.recepient_email_adress, self.subject, self.text)
