    
from django import forms
from.models import label, Annotation

class LabelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LabelForm, self).__init__(*args, **kwargs)
        self.fields['color'].widget.attrs['class'] = 'color-picker'

    class Meta:
        model = label
        fields = ['name', 'color']

class AnnotationForm(forms.ModelForm):
    label = forms.ModelChoiceField(queryset=label.objects.all())
    def __init__(self, *args, **kwargs):
        super(AnnotationForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['readonly'] = True
        self.fields['x1'].widget.attrs['readonly'] = True
        self.fields['y1'].widget.attrs['readonly'] = True
        self.fields['x2'].widget.attrs['readonly'] = True
        self.fields['y2'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super(AnnotationForm, self).clean()
        x1 = cleaned_data.get('x1')
        y1 = cleaned_data.get('y1')
        x2 = cleaned_data.get('x2')
        y2 = cleaned_data.get('y2')
        if x1 > x2 or y1 > y2:
            raise forms.ValidationError('x1, y1, x2, y2 should be in order')
        return cleaned_data

    class Meta:
        model = Annotation
        fields = ['label', 'image', 'x1', 'y1', 'x2', 'y2'] 
