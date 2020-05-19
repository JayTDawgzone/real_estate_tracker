from django import forms
from listings.models import Listing, Maintenance


class MaintenanceForm(forms.ModelForm):

    class Meta():
        model = Maintenance
        fields = ('maintenance_notes', 'title')
        widgets = {
            'maintenance_notes': forms.Textarea(attrs={'class':'editable medium-editor-textarea propertycontent'})
        }
