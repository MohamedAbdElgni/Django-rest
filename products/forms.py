
from django import forms

from .models import *

from categories.models import *

class AddProductForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mt-2'}), label='Name')
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control mt-2'}), label='Price')
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mt-2'}), label='Description')
    img = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control mt-2'}), label='Image')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'form-control mt-2'}), label='Category')
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4:
            raise forms.ValidationError('Name must be at least 4 characters long')
        elif len(name) > 100:
            raise forms.ValidationError('Name must be at most 100 characters long')
        return name
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('Price must be a positive number')
        return price
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError('Description must be at least 10 characters long')
        return description
    

class UpdateProductForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mt-2'}), label='Name')
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control mt-2'}), label='Price')
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mt-2'}), label='Description')
    img = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control mt-2'}), label='Image')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'form-control mt-2'}), label='Category')
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4:
            raise forms.ValidationError('Name must be at least 4 characters long')
        elif len(name) > 100:
            raise forms.ValidationError('Name must be at most 100 characters long')
        return name
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('Price must be a positive number')
        return price
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError('Description must be at least 10 characters long')
        return description
    
    