from django.shortcuts import render, redirect
from .forms import ContactUsForm
from django.http import HttpResponse
from django.contrib import messages
def home_view(request):
    return render(request,'home.html')
def Contact_Us_View(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,message='added suceesfully')
            return redirect('contact')  # Redirect to a success URL after form submission
    else:
        form =ContactUsForm()
    return render(request, 'contact_us.html', {'form': form })
