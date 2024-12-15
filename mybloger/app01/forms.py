from django import forms
from app01.models import user_image

        
from django import forms
from.models import user_image

class UserImageForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    image = forms.ImageField(label='上传图片')
    image_json = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = user_image
        fields = ['name', 'author', 'time', 'image', 'image_json']


class UserImageForm2(forms.Form):
    folder = forms.FileField(widget=forms.FileInput(attrs={'webkitdirectory': True, 'directory': True}))