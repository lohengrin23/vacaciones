from django.contrib import admin


#from someotherapp.models import someothermodel
from .forms import SignUpForm
from .models import SignUp
class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
	
	#class Meta:
		#model = SignUp

admin.site.register(SignUp, SignUpAdmin)