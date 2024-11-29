from django import forms

        
class Base64ImageForm(forms.Form):
    title = forms.CharField(max_length=100)
    image = forms.ImageField()
 