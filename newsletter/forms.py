from django import forms

from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField(required = False)
	email = forms.EmailField()
	message = forms.CharField()


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']
		###exclude = ['full_name']

		def clean_email(self):
	
			email = self.cleanned_data.get('email')
			email_base, provider = email.split("@")
			domain, extension = provider.split('.')
            #it could be repeated
			if not extension == "edu":
				raise forms.ValidationError("please use a valid .edu address")
			return email

		def clean_full_name(self):
			full_name = self.cleaned_data.get('full_name')
			#write validation code
			return full_name