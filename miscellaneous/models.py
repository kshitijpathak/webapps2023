from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=5000)

    def __str__(self):
        details = ''
        details += f'Name        : {self.name}\n'
        details += f'Email   : {self.email}\n'
        details += f'Subject     : {self.subject}\n'
        details += f'Message     : {self.message}\n'
        return details