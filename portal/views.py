from genericpath import exists
from django.shortcuts import render
from portal.forms import MyFileForm , SignUpForm
from portal.models import MyFileUpload
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib import auth
 
# Create your views here.

def upload(request):
    
    myform = MyFileForm
    context = {'myform':myform}
            
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
    return render(request,'upload.html',context)  
    
def home(request):
    
    posts = MyFileUpload.objects.all().count()
    pdf_file=MyFileUpload.objects.filter(file_type__contains='pdf').count()
    excel_file=MyFileUpload.objects.filter(file_type__contains='excel').count()
    doc_file=MyFileUpload.objects.filter(file_type__contains='doc').count()
    context = {
        'posts':posts,
        'pdf_file':pdf_file,
        'excel_file':excel_file,
        'doc_file':doc_file,
        
        
        
    }

    return render(request,'home.html',context)

def index(request):
    mydata=MyFileUpload.objects.all()    
    myform=MyFileForm()
    if mydata!='':
        context={'form':myform,'mydata':mydata}
        return render(request,'index.html',context)
    else:
        context={'form':myform}
        return render(request,"index.html",context)
    
    
    
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
    

    
    
    