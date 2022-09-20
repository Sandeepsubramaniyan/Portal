from genericpath import exists
from django.shortcuts import render
from portal.forms import MyFileForm , SignUpForm
from portal.models import MyFileUpload
from django.contrib import messages
from django.shortcuts import redirect
import datetime
from django.contrib import auth
 
# Create your views here.

def profile(request):
    myform = MyFileForm
    context = {'myform':myform}
    return render(request,'upload.html',context)

def upload(request):
            
    if request.method =="POST":
        myform = MyFileForm(request.POST,request.FILES)
        if myform.is_valid():
            
            MyUserName = request.POST.get('username')
            MyFileName = request.POST.get('file_name')
            MyFileType = request.POST.get('file_type')
            MyFile = request.FILES.get('file')
            
            exists = MyFileUpload.objects.filter(file=MyFile).exists()
            
            if exists:
                messages.error(request,'The file %s is already exists...!!!'% MyFile)
            else:
                MyFileUpload.objects.create(username=MyUserName,file_name=MyFileName,file_type=MyFileType,file=MyFile).save()
                messages.success(request,"file uploaded successfully")
        return redirect('profile')
    
def home(request):
    return render(request,'home.html')
    
    
def signup(request):
    if request.method =="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('login')
    
    else:
        form = SignUpForm()
    return render(request,"signup.html",{'form':form})    

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')
    

    
    
    