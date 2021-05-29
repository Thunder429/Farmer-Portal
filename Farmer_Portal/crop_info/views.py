from django.shortcuts import render,redirect
from .models import crop

def crop_info(request):
    if request.method == "POST":
        name = request.POST['Name']
        description = request.POST['desc']
        prize = request.POST['prize']
        stock = request.POST['stock']
        photo = request.POST['photo']
        
        obj = crop.objects.create(name=name, description=description, prize=prize, stock=stock, photo=photo)
        obj.save()
        return redirect('crop_info.html')
    else:
        return render(request, 'add_item.html')