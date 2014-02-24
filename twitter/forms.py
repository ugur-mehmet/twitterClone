from django import forms

class SignupForm(forms.Form):
	email = forms.EmailField()
	name = forms.CharField(max_length=150)
	surname = forms.CharField(max_length=150)
	password = forms.CharField(max_length=100)