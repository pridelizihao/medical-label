from django import forms
from app01.models import  Product

        
from django import forms
from.models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    image_json = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Product
        fields = ['name', 'description', 'image',"image_json"]
    

    
    
 