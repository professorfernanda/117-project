from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    return render(request, 'pages/about_me.html')

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST) 
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email_from = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string("pages/email.html", request.POST)

            send_mail("Message from " + name, message, email_from, ['mariafeernanda.murillo@gmail.com'], html_message=html)
            
            print("Enviado");
            return redirect('home')
        else:
            print("No se pudo enviar el mensage");
        
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {
        'form': form
    })