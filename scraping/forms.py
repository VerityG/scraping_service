from django import forms
from scraping.models import City, Programming_language


class FindForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name='slug', required=False,
                                  widget=forms.Select(attrs={'class': 'form-control'}), label='Город')
    programming_language = forms.ModelChoiceField(queryset=Programming_language.objects.all(), to_field_name='slug',
                                                  required=False,widget=forms.Select(attrs={'class': 'form-control'}),
                                                  label='Специальность')
