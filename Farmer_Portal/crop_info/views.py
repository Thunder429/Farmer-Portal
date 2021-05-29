from django.shortcuts import render,redirect
from .models import crop

def crop_info(request):
    if request.method == "POST":
        name = request.POST['Name']
        contact = request.POST['contact']
        owner = request.POST['owner']
        description = request.POST['desc']
        prize = request.POST['prize']
        stock = request.POST['stock']
        photo = request.POST['photo']
        
        obj = crop.objects.create(name=name, contact=contact, owner=owner, description=description, prize=prize, stock=stock, photo=photo)
        obj.save()
    return render(request, 'add_item.html')