from django.db import models

# Create your models here.
class contact_details(models.Model):
    Full_name=models.CharField(max_length=200, null=False,blank=False)
    email=models.EmailField(max_length=200, null=False, blank=False)
    mobile_number=models.CharField(max_length=10,null=False, blank=False)
    email_subject=models.CharField(max_length=500,null=False, blank=False)
    descsription=models.CharField(max_length=500,blank=False,null=False)

    def __str__(self):
        return self.Full_name
