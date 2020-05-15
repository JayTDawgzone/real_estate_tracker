from django.db import models
from datetime import datetime
from realtors.models import Realtor
from django.core.validators import RegexValidator

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

EXPENSETYPE = (
    ('1', 'Electric'),
    ('2', 'Gas'),
    ('3', 'Water'),
    ('4', 'Garbage'),
    ('5', 'HOA'),
    ('6', 'Other')
)

RECURRENCE = (
    ('1', 'Monthly'),
    ('2', 'Annually'),
    ('3', 'Quarterly'),
    ('4', 'One-Time'),
    ('5', 'Other')
)

RENTAL_STATUS = (
    ('1', 'Rented'),
    ('2', 'Available'),
    ('3', 'Available Soon'),
    ('4', 'Under Repair'),
)

YESNO = (
    ('YES', 'Yes'),
    ('NO', 'No')
)

OPENCLOSED = (
    ('OPEN', 'Open'),
    ('CLOSED', 'Closed')
)

ROOFS = (
    ('1', 'Asphalt'),
    ('2', 'Clay/Concrete'),
    ('3', 'Slate'),
    ('4', 'Metal'),
    ('5', 'Wood'),
)

BEDROOMS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, related_name='property_manager')
  title = models.CharField(max_length=200)
  APN = models.CharField(max_length=200, default='000-000-0000')
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  neighborhood = models.CharField(max_length=200, blank=True)
  school_district = models.CharField(max_length=200, blank=True)
  description = models.TextField(blank=True)
  type = models.CharField(max_length=3, choices=TYPES, default='SFH')
  status = models.CharField(max_length=1, choices=STATUS, default='2')
  ac = models.CharField(max_length=3, choices=YESNO, default=2)
  heating = models.CharField(max_length=3, choices=YESNO, default=2)
  water_heater = models.CharField(max_length=3, choices=YESNO, default=2)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1, default=1)
  stories = models.DecimalField(max_digits=2, decimal_places=1, default=1)
  garage = models.IntegerField(default=0)
  parking = models.CharField(max_length=3, choices=YESNO, default=2)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  year_built = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,10}$')], default='1900')
  roof_type = models.CharField(max_length=1, choices=ROOFS, default='1')
  roof_year = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,10}$')], default='1900')
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  purchase_date = models.DateTimeField(default=datetime.now, blank=True)
  purchase_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
  purchase_escrow_agent = models.CharField(max_length=200, blank=True)
  purchase_escrow_number = models.CharField(max_length=200, blank=True)
  sold_date = models.DateTimeField(default=datetime.now, blank=True)
  sold_amt = models.IntegerField()
  sale_escrow_agent = models.CharField(max_length=200, blank=True)
  sale_escrow_number = models.CharField(max_length=200, blank=True)
  pct_ownership = models.DecimalField(max_digits=3, decimal_places=2, default=0)
  assessed_value = models.IntegerField()
  property_tax = models.IntegerField()
  property_tax_county = models.CharField(max_length=200, blank=True)
  current_value = models.IntegerField()
  owned_equity = models.IntegerField()
  partner = models.CharField(max_length=100)


  class Meta:
      verbose_name = "Property"
      verbose_name_plural = "Properties"

  def __str__(self):
    return self.title


class Maintenance(models.Model):
    listing = models.ForeignKey(Listing, default=None, on_delete=models.DO_NOTHING, related_name='maintenance')
    title = models.CharField(max_length=200, default='title')
    repair_date = models.DateTimeField(default=datetime.now, blank=True)
    cost = models.IntegerField(default=0)
    repair_status = models.CharField(max_length=10, choices=OPENCLOSED, default=1)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    maintenance_notes = models.TextField()

    def __str__(self):
        return self.listing.title + ": " + self.title

    class Meta:
        verbose_name = "Maintenance Job"
        verbose_name_plural = "Maintenance Jobs"


class Rental(models.Model):
    listing = models.ForeignKey(Listing, default=None, on_delete=models.DO_NOTHING, related_name='rental')
    rental_status = models.CharField(max_length=1, choices=RENTAL_STATUS, default='2')
    lease_number = models.CharField(max_length=200)
    rental_price = models.IntegerField()
    security_deposit = models.IntegerField()
    other_fees = models.IntegerField()
    lease_start = models.DateTimeField(default=datetime.now, blank=True)
    lease_end = models.DateTimeField(default=datetime.now, blank=True)
    rental_notes = models.TextField(blank=True)
    tenant_name = models.CharField(max_length=50, blank=True)
    tenant_phone = models.CharField(max_length=10, blank=True)
    tenant_phone2 = models.CharField(max_length=10, blank=True)
    tenant_email = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.listing.title + ": " + self.lease_number

    class Meta:
      verbose_name = "Lease"
      verbose_name_plural = "Leases"



class Insurance(models.Model):
    listing = models.ForeignKey(Listing, default=None, on_delete=models.DO_NOTHING, related_name='insurance')
    insurance_company = models.CharField(max_length=200, blank=True)
    policy_number = models.CharField(max_length=200, blank=True)
    liability_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    replacement_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    effective_start_date = models.DateTimeField(default=datetime.now, blank=True)
    effective_end_date = models.DateTimeField(default=datetime.now, blank=True)
    monthly_pmt = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    insurance_notes = models.TextField(blank=True)

    def __str__(self):
        return self.listing.title + ": " + self.policy_number

    class Meta:
      verbose_name = "Insurance Policy"
      verbose_name_plural = "Insurance Policies"


class Expense(models.Model):
    listing = models.ForeignKey(Listing, default=None, on_delete=models.DO_NOTHING, related_name='expense')
    expense_type = models.CharField(max_length=20, choices=EXPENSETYPE, default='6')
    vendor_name = models.CharField(max_length=200, blank=True)
    amount = models.IntegerField()
    recurrence = models.CharField(max_length=20, choices=RECURRENCE, default='1')
    autopay = models.CharField(max_length=20, choices=YESNO, default='1')
    expense_notes = models.TextField(blank=True)

    def __str__(self):
        return self.listing.title + ": " + self.vendor_name

class Mortgage(models.Model):
    listing = models.ForeignKey(Listing, default=None, on_delete=models.DO_NOTHING, related_name='mortgage')
    loan_number = models.CharField(max_length=200, blank=True)
    lender = models.CharField(max_length=200, blank=True)
    monthly_pmt = models.IntegerField(default=0)
    mortgage_total = models.IntegerField(default=0)
    principal = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    interest = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    impound = models.BooleanField(default=True)

    def __str__(self):
        return self.lender + " " + self.loan_number
