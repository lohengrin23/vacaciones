from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm



def home(request):
	title = 'welcome'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		#"abc": 123,
		"form": form
	}


	#if request.user.is_authenticated():
		#title = "My title %s" %(request.user)
	#add a form
	#if request.method == "POST":
		#print request.POST
	
	if form.is_valid():
		#form.save()
		instance = form.save(commit = False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "full_name"
			instance.full_name = full_name
		#if not instance.full_name:
			#instance.full_name = "jesus"
		instance.save()
		context ={
		"title": "thank you"
		}
		#print instance.email
		#print instance.timestamp
	
	return render(request,"home.html", context )


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		###for key, value in form.cleaned_data.iteritems():
			###print key,value
			##print form.cleaned_data.get(key)
		subject = 'site contact form'
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		full_name = form.cleaned_data.get("full_name")
		send_mail(subject, 
			contact_message, 
			from_email, 
			[to_email], 
			fail_silently=False)
		#print email, message
		print form.cleaned_data


	context = {
		"form": form,

	}
	return render(request, "forms.html", context)