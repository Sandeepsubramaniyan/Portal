from django.shortcuts import render

from portal.forms import MyFileForm

# Create your views here.

def home(request):
    myform =MyFileForm
    context={'myform':myform}
    return render(request,'upload.html',context)


    