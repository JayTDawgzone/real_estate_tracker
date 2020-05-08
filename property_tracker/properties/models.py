from django.db import models
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

class Property(models.Model):
    author = models.ForeignKey('auth.User')
    nickname = models.CharField(max_length=200)
    apn = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    notes = models.TextField()
    create_date = models.DateTimeField(default=datetime.datetime.now)
    published_date = models.DateTimeField(blank=True,null=True)


    def publish(self):
        self.published_date = datetime.datetime.now()
        self.save()

    def get_absolute_url(self):
        return reverse('property_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.nickname
