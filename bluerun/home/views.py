from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django import forms
from django.contrib import messages 

# Create your views here.

def index(request):
	return render(request , 'home/index.html')

def aboutus(request):
	return render(request , 'home/about-us.html')

def services(request):
	return render(request , 'home/services.html')

def portfolio(request):
	return render(request , 'home/portfolio.html')

def pricing(request):
	return render(request , 'home/pricing.html')

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            contact = request.POST.get('contact')
            subject = request.POST.get('subject' , '')
            message = request.POST.get('message', '')
            forminstance = Contact(name = name,email = email,contact = contact,subject = subject,message = message)
            forminstance.save()
            messages.success(request, 'Submitted successfully!') 
        else:
            raise forms.ValidationError('Invalid/Missing Fields')
            messages.error(request, 'Submission failed! Please fill out the necessary details.')               
    else:
        form = ContactForm()
    
    return render(request , 'home/contact-us.html')

def careers(request):
	return render(request , 'home/careers.html')
