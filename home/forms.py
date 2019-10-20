from django import forms


class ContactForm(forms.Form):
    client_name = forms.CharField(max_length=20)
    client_email = forms.EmailField()
    client_phone = forms.IntegerField()
    client_message = forms.CharField(max_length=200)

