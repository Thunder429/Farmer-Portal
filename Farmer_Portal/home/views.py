from django.shortcuts import render,redirect
from farmer_info.models import farmer
from crop_info.models import crop
# Create your views here.

def home(request):
    obj = crop.objects.all()
    arr = [obj[0],obj[1],obj[2],obj[3],obj[4],obj[5]]
    return render(request, 'home.html',{'objects':arr})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        obj = farmer.objects.filter(contact__exact=username, password__exact=password)[0]
        crops = crop.objects.filter(contact__exact=username)

        if obj:
            return render(request, 'profile.html', {'farmer':obj, 'crops':crops})
        else:
            #messages.error(request, 'User is not exist. Please check your Event-Id or Password.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')