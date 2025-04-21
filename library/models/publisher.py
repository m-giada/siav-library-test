from django.db import models

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    business_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, default='')
    phone_number = models.CharField(max_length=20, blank=True, default='')

    def __str__(self):
        return self.business_name