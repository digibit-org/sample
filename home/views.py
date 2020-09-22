

from django.shortcuts import render, HttpResponse
from home.models import Contact
from home.models import Register
from home.models import Login
import json
from django.views.decorators.csrf import csrf_exempt
# from PayTm import Checksum
# Create your views here.
from django.http import HttpResponse
# MERCHANT_KEY = 'SccIiPAcPEh_B69G'



# Create your views here.
def home(request):
    # return HttpResponse("This is my homepage (/)")
    return render(request, 'home.html')



def contact(request):
    if request.method=='POST':
        # print("This is post")
        name = request.POST['name']
        # lastname = request.POST['lastname']
        email = request.POST['email']
        # subject = request.POST['subject']
        message = request.POST['message']
        # print(name, email, message)
        ins = Contact(name=name, email=email, message=message)
        ins.save()
        print("The data has been written to the db")

    return render(request, 'contact.html')

def register(request):
    if request.method=='POST':
        # print("This is post")
        name = request.POST['name']
        # lastname = request.POST['lastname']
        email = request.POST['email']
        # subject = request.POST['subject']
        phone = request.POST['phone']
        # print(name, email, message)
        ins = Register(name=name, email=email, phone=phone)
        ins.save()
        print("The data has been written to the db")

    return render(request, 'register.html')

def login(request):
    
    if request.method=='POST':
        email = request.POST['email']
        phone = request.POST['phone']
        ins = Login(email=email, phone=phone)
        ins.save()
        print("The data has been written to the db")
    return render(request, 'login.html')


  



@csrf_exempt
def handlerequest(request):
    return HttpResponse('done')
    pass

