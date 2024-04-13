from django.shortcuts import render
from .models import User
# Create your views here.
def home(request):
    user=User.objects.all()
    return render(request,'webpages/home.html',{'users':user})
