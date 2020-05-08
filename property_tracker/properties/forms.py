from django import forms
from properties.models import Property


class PropertyForm(forms.ModelForm):

    class Meta():
        model = Property
        fields = ('author', 'nickname', 'apn', 'address',
                'address2', 'city', 'state', 'zip', 'notes',)
        widgets = {
            'nickname': forms.TextInput(attrs={'class':'textinputclass'}),
            'notes': forms.Textarea(attrs={'class':'editable medium-editor-textarea propertycontent'})
        }
