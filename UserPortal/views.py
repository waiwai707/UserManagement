from django.shortcuts import render,redirect
from UserPortal.models import User

# Create your views here.
def home(request):
    userdata = User.objects.raw("select * from userportal_user")
    return render(request,'home.html',{'userdata':userdata})

def signup(request):
    return render(request,'signup.html',{})    

#create function
def create(request):
    storedata = User()
    storedata.user_name = request.POST.get('user_name')
    storedata.password = request.POST.get('password')
    storedata.dob = request.POST.get('dob')
    storedata.email = request.POST.get('email')
    storedata.phone_number = request.POST.get('phone_number')
    storedata.user_type = request.POST.get('user_type')
    storedata.save()
    return redirect('/home')

  