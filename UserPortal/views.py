from django.shortcuts import render,redirect
from UserPortal.models import User
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm

# Create your views here.
def home(request):
    userdata = User.objects.raw("select * from userportal_user where status is Null")
    return render(request,'home.html',{'userdata':userdata})

def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

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

  