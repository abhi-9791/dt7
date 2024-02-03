from django import forms
from .models import Contact_Us

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact_Us
        fields = '__all__'