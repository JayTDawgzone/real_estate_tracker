from django.db import models
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

# Create your models here.

TYPES = (
    ('SFH', 'SFH'),
    ('DUP', 'Duplex'),
    ('APT', 'Apartment'),
    ('CND', 'Condo'),
    ('MBH', 'Mobile Home'),
    ('CMR', 'Commercial Retail'),
    ('CMO', 'Commercial Office'),
    ('CMW', 'Commercial Warehouse'),
    ('CML', 'Commercial W/O Lot'),
)

STATUS = (
    ('1', 'Rented'),
    ('2', 'Available'),
    ('3', 'For Sale'),
    ('4', 'Under Construction'),
    ('5', 'Owner Occupied'),
)

BEDROOMS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

YESNO = (
    ('YES', 'Yes'),
    ('NO', 'NO')
)

STORIES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

ROOFS = (
    ('1', 'Asphalt'),
    ('2', 'Clay/Concrete'),
    ('3', 'Slate'),
    ('4', 'Metal'),
    ('5', 'Wood'),
)
class Property(models.Model):
    nickname = models.CharField(max_length=200)
    apn = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    neighborhood = models.CharField(max_length=200)
    school_district = models.CharField(max_length=200)
    square_feet = models.IntegerField(default=0)
    bedrooms = models.CharField(max_length=1, choices=BEDROOMS, default=1)
    garage = models.CharField(max_length=3, choices=YESNO, default=2)
    stories = models.CharField(max_length=1, choices=STORIES, default=1)
    parking = models.CharField(max_length=3, choices=YESNO, default=2)
    year_built = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,10}$')], default='1900')
    roof_type = models.CharField(max_length=1, choices=ROOFS, default='1')
    roof_year = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,10}$')], default='1900')
    heating = models.CharField(max_length=3, choices=YESNO, default=2)
    ac = models.CharField(max_length=3, choices=YESNO, default=2)
    water_heater = models.CharField(max_length=3, choices=YESNO, default=2)
    type = models.CharField(max_length=3, choices=TYPES, default='SFH')
    status = models.CharField(max_length=1, choices=STATUS, default='2')
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
