from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import Widget
from .models import Image
 
class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('tite','url','description')
        widgets = {
            'url':forms.HiddenInput
        }

        def clean_url(self):
            url = self.cleand_data['url']
            valid_extensions = ['jpg','jpeg']
            extensions = url.rsplit('.',1)[1].lower()