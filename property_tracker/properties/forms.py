from django import forms
from properties.models import Property

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
    ('1', 'SFH'),
    ('2', 'Duplex'),
    ('3', 'Apartment'),
    ('4', 'Condo'),
    ('5', 'Mobile Home'),
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
    ('NO', 'No')
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
class PropertyForm(forms.ModelForm):

    class Meta():
        model = Property
        fields = ('nickname', 'type', 'status',
                'apn', 'address','address2',
                 'city', 'state', 'zip', 'square_feet',
                 'bedrooms', 'stories',
                 'parking', 'year_built',
                 'roof_type',
                 'roof_year', 'heating', 'ac', 'water_heater',
                 'neighborhood', 'school_district', 'notes',)
        widgets = {
            'nickname': forms.TextInput(attrs={'class':'textinputclass'}),
            'notes': forms.Textarea(attrs={'class':'editable medium-editor-textarea propertycontent'})
        }
