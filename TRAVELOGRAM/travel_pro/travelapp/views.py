from django.shortcuts import render
from django.http import HttpResponse
def Testfn(request):
    return HttpResponse('hlooooooo')
def html1(request):
    return render(request,'index.html')

# Create your views here.
