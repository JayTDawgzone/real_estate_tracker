from django.db import models
from datetime import datetime

class Manager(models.Model):
  name = models.CharField(max_length=200)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  description = models.TextField(blank=True)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  company_name = models.CharField(max_length=50)
  address = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=2)
  zip = models.CharField(max_length=10)
  is_mvp = models.BooleanField(default=False)
  def __str__(self):
    return self.name
