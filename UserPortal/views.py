from django.shortcuts import render,redirect
from UserPortal.models import User

# Create your views here.
def home(request):
    userdata = User.objects.raw("select * from userportal_user where status is Null")
    return render(request,'home.html',{'userdata':userdata})

def signup(request):
    return render(request,'signup.html',{})

def update(request,pk):
    updatedata = User.objects.get(id=pk)
    return render(request,'update.html',{'updatedata':updatedata})   

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

#Edit Function
def edit(request,pk):
    editdata = User.objects.get(id=pk)
    editdata.user_name = request.POST.get('user_name')
    editdata.password = request.POST.get('password')
    editdata.dob = request.POST.get('dob')
    editdata.email = request.POST.get('email')
    editdata.phone_number = request.POST.get('phone_number')
    editdata.user_type = request.POST.get('user_type')
    editdata.save()
    return redirect('/home')

#Delete Function
def delete(request,pk):
    selectdata = User.objects.get(id=pk)
    selectdata.status = 'deleted'
    selectdata.save()
    return redirect('/home')

  