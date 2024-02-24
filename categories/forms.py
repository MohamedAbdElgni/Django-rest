from django import forms


from django import forms
from .models import Category 

class CategoryForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mt-2'}), label='Name')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mt-2'}), label='Description')
    img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control mt-2'}), label='Image')
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        if len(name) < 4:
            raise forms.ValidationError('Name must be at least 4 characters long')
        elif len(name) > 100:
            raise forms.ValidationError('Name must be at most 100 characters long')
        
        
        if Category.objects.filter(name=name).exists():
            raise forms.ValidationError('Category already exists')
        
        return name
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        
        if len(description) < 10:
            raise forms.ValidationError('Description must be at least 10 characters long')
        
        return description

    
class UpdateCategory(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mt-2'}), label='Name')
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mt-2'}), label='Description')
    img = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control mt-2'}), label='Image'
    )
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4:
            raise forms.ValidationError('Name must be at least 4 characters long')
        elif len(name) > 100:
            raise forms.ValidationError('Name must be at most 100 characters long')
        return name
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError('Description must be at least 10 characters long')
        return description
    
    def clean_img(self):
        img = self.cleaned_data.get('img')
        if img == None:
            raise forms.ValidationError('Image must be selected')
        return img
