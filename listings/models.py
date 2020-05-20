from django.db import models
from datetime import datetime
from managers.models import Manager
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator

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
    ('2', 'Vacant'),
    ('3', 'For Sale'),
    ('4', 'Under Construction'),
    ('5', 'Buying'),
    ('6', 'In Escrow'),
    ('7', 'Sold'),
)

EXPENSETYPE = (
    ('1', 'Electric'),
    ('2', 'Gas'),
    ('3', 'Water'),
    ('4', 'Garbage'),
    ('5', 'HOA'),
    ('5', 'Sewer'),
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
    ('1', 'Current'),
    ('2', 'Late'),
    ('3', '3-Day Notice'),
    ('4', 'Vacant'),
    ('5', 'Evicting'),
)

YESNO = (
    ('YES', 'Yes'),
    ('NO', 'No')
)

OPENCLOSED = (
    ('OPEN', 'Open'),
    ('CLOSED', 'Closed')
)

RESPONSIBILITY = (
    ('1', 'Owner Pays'),
    ('2', 'Tenant Pays')
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
  manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING, related_name='property_manager')
  title = models.CharField(max_length=200)
  APN = models.CharField(max_length=200, blank=True)
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
  target_rent = models.IntegerField()
  asking_price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1, default=1)
  stories = models.DecimalField(max_digits=2, decimal_places=1, default=1)
  garage = models.IntegerField(default=0)
  parking = models.CharField(max_length=3, choices=YESNO, default=2)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
  year_built = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,10}$')], blank=True)
  roof_type = models.CharField(max_length=1, choices=ROOFS, blank=True)
  roof_year = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,10}$')], blank=True)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateField(default=datetime.now, blank=True)
  purchase_date = models.DateField(default=datetime.now, blank=True)
  purchase_amt = models.IntegerField(blank=True, null=True)
  purchase_escrow_agent = models.CharField(max_length=200, blank=True)
  purchase_escrow_number = models.CharField(max_length=200, blank=True)
  sold_date = models.DateField(blank=True, null=True)
  sold_amt = models.IntegerField(blank=True, null=True)
  sale_escrow_agent = models.CharField(max_length=200, blank=True)
  sale_escrow_number = models.CharField(max_length=200, blank=True)
  percent_ownership = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])
  assessed_value = models.IntegerField(blank=True, null=True)
  property_tax = models.IntegerField(blank=True, null=True)
  property_tax_county = models.CharField(max_length=200, blank=True)
  current_value = models.IntegerField(blank=True, null=True)
  owner = models.CharField(max_length=200, blank=True)
  owned_equity = models.IntegerField(blank=True, null=True)
  partner = models.CharField(max_length=100, blank=True)


  class Meta:
      verbose_name = "Property"
      verbose_name_plural = "Properties"

  def __str__(self):
    return self.title


class Maintenance(models.Model):
    listing = models.ForeignKey(Listing, default=None, on_delete=models.DO_NOTHING, related_name='maintenance')
    title = models.CharField(max_length=200, default='title')
    repair_date = models.DateField(default=datetime.now, blank=True)
    cost = models.IntegerField(default=0)
    repair_status = models.CharField(max_length=10, choices=OPENCLOSED, default=1)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    maintenance_notes = models.TextField()
    maintenance_document  = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True)

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
    lease_start = models.DateField(default=datetime.now, blank=True)
    lease_end = models.DateField(default=datetime.now, blank=True)
    rental_notes = models.TextField(blank=True)
    tenant_name = models.CharField(max_length=50, blank=True)
    tenant_phone = models.CharField(max_length=10, blank=True)
    tenant_phone2 = models.CharField(max_length=10, blank=True)
    tenant_email = models.CharField(max_length=50, blank=True)
    lease_agreement  = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True)

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
    effective_start_date = models.DateField(default=datetime.now, blank=True)
    effective_end_date = models.DateField(default=datetime.now, blank=True)
    annual_pmt = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    insurance_notes = models.TextField(blank=True)
    insurance_policy  = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.listing.title + ": " + self.policy_number

    class Meta:
      verbose_name = "Insurance Policy"
      verbose_name_plural = "Insurance Policies"


class Expense(models.Model):
    listing = models.ForeignKey(Listing, default=None, on_delete=models.DO_NOTHING, related_name='expense')
    expense_type = models.CharField(max_length=20, choices=EXPENSETYPE, default='6')
    vendor_name = models.CharField(max_length=200, blank=True)
    autopay = models.CharField(max_length=20, choices=YESNO, default='1')
    responsibility = models.CharField(max_length=7, choices=RESPONSIBILITY, default='1')
    expense_notes = models.TextField(blank=True)
    expense_document  = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True)


    def __str__(self):
        return self.listing.title + ": " + self.vendor_name

class Mortgage(models.Model):
    listing = models.ForeignKey(Listing, default=None, on_delete=models.DO_NOTHING, related_name='mortgage')
    loan_number = models.CharField(max_length=200, blank=True)
    lender = models.CharField(max_length=200, blank=True)
    monthly_pmt = models.DecimalField(max_digits=20, decimal_places=2, blank=True)
    principal = models.DecimalField(max_digits=20, decimal_places=2, blank=True)
    interest = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    impound = models.BooleanField(default=True)
    mortgage_documents  = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.lender + " " + self.loan_number

## PROPERTY
