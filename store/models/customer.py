from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone = models.CharField(default='+880', max_length=14)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    def getCustomer_by_email(email):
        return Customer.objects.get(email=email)
