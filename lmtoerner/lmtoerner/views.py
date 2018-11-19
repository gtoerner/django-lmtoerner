from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def pricing(request):
    return render(request, 'pricing.html')

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
            subject = form.cleaned_data['contact_subject']
            from_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['contact_message']
            try:
                send_mail(subject, message, from_email, ['gtoerner@gmail'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact_success')
    return render(request, "contact.html", {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')
