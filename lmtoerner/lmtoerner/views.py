from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def baseball(request):
    return render(request, 'TeamSports/baseball.html')

def basketball(request):
    return render(request, 'TeamSports/basketball.html')

def cycling(request):
    return render(request, 'TeamSports/cycling.html')

def testering(request):
    return render(request, 'TeamSports/testering.html')

def rugby(request):
    return render(request, 'TeamSports/rugby.html')

def soccer(request):
    return render(request, 'TeamSports/soccer.html')

def softball(request):
    return render(request, 'TeamSports/softball.html')

def football(request):
    return render(request, 'TeamSports/football.html')

def hockey(request):
    return render(request, 'TeamSports/hockey.html')

def delivery(request):
    return render(request, 'delivery.html')

def pricing(request):
    return render(request, 'pricing.html')

def products(request):
    return render(request, 'products.html')

def privacy(request):
    return render(request, 'privacy.html')

def sizechart(request):
    return render(request, 'size-chart.html')

def terms(request):
    return render(request, 'terms.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['contact_name']
            #subject = form.cleaned_data['contact_subject']
            from_email = form.cleaned_data['contact_email']
            tmpmessage = form.cleaned_data['contact_message']
            message = name + " " + tmpmessage
            try:
                send_mail("ContactForm ", message, from_email, ['gtoerner@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contct_success')
    return render(request, "contact.html", {'form': form})

def contct_success(request):
    return render(request, 'contact_success.html')
