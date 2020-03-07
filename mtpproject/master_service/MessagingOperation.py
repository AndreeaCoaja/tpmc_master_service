from OperationClass import Operation
class MessagingOperation(Operation):

    def __init__(self, recepientEMailAdress, subject, text):
        self.recepientEMailAdress = recepientEMailAdress
        self.subject = subject
        self.text = text

    def execute(self):
        messaging.sentEMail(self.recepientEMailAdress, self.subject, self.text)

