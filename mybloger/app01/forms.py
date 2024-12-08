from django import forms
from app01.models import  Product

        
from django import forms
from.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']
    
    
 