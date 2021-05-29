from django.shortcuts import render
from .models import farmer

def info(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('Contactno')
        email = request.POST.get('Email')
        address = request.POST.get('Address')
        photo = request.POST.get('photo')
        password = request.POST.get('password')

        obj = farmer(name=name, contact=contact, email=email, address=address, photo=photo, password=password)
        obj.save()
    return render(request, 'signup.html')
