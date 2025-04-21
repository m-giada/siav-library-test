from django import forms

from library.models import Publisher


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['business_name', 'address', 'phone_number']