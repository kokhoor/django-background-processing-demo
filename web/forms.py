from django import forms

class ContactUs(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=False)
    email = forms.CharField(label='Email Address', max_length=128, required=False)
    subject = forms.CharField(label='Subject', max_length=128, required=False)
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'rows': 5}), required=False)
