from django import forms

class MensajeForm(forms.Form):
    nombre = forms.CharField(label='Tu nombre', max_length=100)
    mensaje = forms.CharField(widget=forms.Textarea, label='Tu mensaje')
