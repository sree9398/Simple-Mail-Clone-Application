
from django import forms

class EmailComposeForm(forms.Form):
    from_email = forms.EmailField(label="From Email")
    to_email = forms.EmailField(label="To Email")
    subject = forms.CharField(max_length=100, label="Subject")
    message = forms.CharField(widget=forms.Textarea, label="Message")
