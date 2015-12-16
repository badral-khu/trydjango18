from .forms import ContactForm, SignUpForm
from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .models import SignUp 
def home(request):
	title = 'Sign Up Now'
	# if request.user.is_authenticated():
	# 	title = "My Title %s" % (request.user)
	# add a form
	if request.method == 'POST':
		print request.POST 
	form = SignUpForm(request.POST or None)

	context = {
		"title" : title,
		"form" : form

	}

	if form.is_valid():
		#form.save()
		print request.POST['email'] # not recommended

		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name

		instance.save()

		# print instance.email
		context = {
			"title" : "Thank you"
		}
			
	if request.user.is_authenticated() and request.user.is_staff:
		# i=1
		# for instance in SignUp.objects.all():

		# 	print i, instance.full_name
		# 	i+=1
		queryset = SignUp.objects.all().order_by("-timestamp")#.filter(full_name__icontains="bad")
		print SignUp.objects.all().order_by("-timestamp").filter(full_name__icontains="bad").count()
		context = {
			"queryset": queryset
		}	
	return render(request, "home.html", context)

def contact(request):
	title = "Contact Us"
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print form_email
		subject = "Site Contact form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,'yourtheremail@email.com']
		contact_message = "%s %s via %s " % (
			form_full_name,
			form_message,
			form_email)

		send_mail(subject,
		 	contact_message, 
		 	from_email, 
		 	to_email, 
		 	fail_silently = False)

		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
#			print form.cleaned_data.get(key)

	context = {
		"form": form,
		"title":title,
		"title_align_center":title_align_center,

	}


	return render(request,"forms.html", context)
