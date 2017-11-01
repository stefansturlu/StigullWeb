from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/homepage.html')

def laws(request):
    return render(request, 'home/laws.html')

def contact(request):
    return render(request, 'home/basic.html', {'info':['If you would like to contact me, please email me','email@email.com']})
