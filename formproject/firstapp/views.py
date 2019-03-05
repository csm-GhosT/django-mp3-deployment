from django.shortcuts import render
from . import forms
from django.core.files.storage import FileSystemStorage
from . import test
from django.http import HttpResponse
import glob
import os
# Create your views here.
def index(request):
    return render(request,'firstapp/index.html')

def form_name_view(request):
    form =forms.FormName()
    if(request.method=='POST'):
        form=forms.FormName(request.POST)
        uploaded_file=request.FILES['document']

        emptyMedia()
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        print("Image saved")
        insect_identified=test.main()
        # print(len(insect_identified))
        if(insect_identified=="ant"):
            html = "<html><body><center><h1>Insect:Ant</h1></center></body></html>"
            print("in ant")
            return  HttpResponse(html)
        elif(insect_identified=="butterfly"):
            html = "<html><body><center><h1>Insect:Butterfly</h1></center></body></html>"
            return  HttpResponse(html)
        elif(insect_identified=="centipede"):
            html = "<html><body><center><h1>Insect:Centipede</h1></center></body></html>"
            return  HttpResponse(html)
        elif(insect_identified=="cockroach"):
            html = "<html><body><center><h1>Insect:Cockroach</h1></center></body></html>"
            return  HttpResponse(html)
        elif(insect_identified=="earthworm"):
            html = "<html><body><center><h1>Insect:Earthworm</h1></center></body></html>"
            return  HttpResponse(html)
        elif(insect_identified=="not insect"):
            html = "<html><body><center><h1>Insect:Not Insect</h1></center></body></html>"
            return  HttpResponse(html)




    return render(request, 'firstapp/formpage.html', {'form':form})


def emptyMedia():
    files = glob.glob('media/*')
    for f in files:
        os.remove(f)
