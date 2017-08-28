from django import forms


class TilForm(forms.Form):
    subject = forms.CharField(label='Title', max_length=160)
    post = forms.CharField(label='What did I learn today?',
                           widget=forms.Textarea, max_length=800)
