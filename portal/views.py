from genericpath import exists
from django.shortcuts import render
from portal.forms import MyFileForm
from portal.models import MyFileUpload
from django.contrib import messages
from django.shortcuts import redirect
import datetime
 
# Create your views here.

def home(request):
    myform = MyFileForm
    context = {'myform':myform}
    return render(request,'upload.html',context)

def upload(request):
    
    data = MyFileUpload.objects.all()
    
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
        return redirect('home')
    