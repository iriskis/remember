from django import forms
import datetime

class RememberForm(forms.Form):
    title = forms.CharField(max_length=100)
    comment = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(initial=datetime.date.today)