from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    jobtitle=models.CharField(max_length=30)
    companyname=models.CharField(max_length=30)
    jobdescription=models.TextField()
    location=models.CharField(max_length=20)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    jobtype=models.CharField(max_length=20)
    postedby=models.ForeignKey(User,on_delete=models.CASCADE)