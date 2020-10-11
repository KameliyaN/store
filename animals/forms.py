from django import forms


class AnimalForm(forms.ModelForm):
    name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    breed = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea())
    image_url = forms.URLField(required=True)

