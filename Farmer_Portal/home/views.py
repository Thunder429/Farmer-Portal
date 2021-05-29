from django.shortcuts import render
from farmer_info.models import farmer

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        x = 1
        temp = farmer()
        for temp in farmer.objects.all():
            if temp.contact == int(username) and str(temp.password) == password:
                x = 2
                break
        return render(request, 'signup.html')
    else:
        return render(request, 'login.html')



