from django.db import models
from datetime import datetime
# Create your models here.
class FIbranch(models.Model):
    finame=models.CharField(max_length=25)
    location = models.CharField(max_length=100)
    is_active =models.BooleanField(default=True)

    def __str__(self):
        return (self.finame)
class Cases(models.Model):
    caseid=models.CharField(max_length=25)
    applicantname=models.CharField(max_length=100)
    finame=models.ForeignKey(FIbranch,on_delete=models.CASCADE)
    applicant_mobile_number=models.PositiveBigIntegerField()
    created_at = models.DateTimeField(default=datetime.now())
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return(self.caseid)
