from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'pages/about_me.html')

def contact(request):
    form = ContactForm() #Create an instance of the form

    

    return render(request, 'pages/contact.html', {
        'form': form
    })