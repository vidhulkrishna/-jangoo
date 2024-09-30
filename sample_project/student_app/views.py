from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def message(request):
    return HttpResponse("Hi python")

def sample(request):
     if request.method=='POST':
         obj=Student()
         obj.Name=request.POST.get('n1')
         obj.Age=request.POST.get('a1')
         obj.Address=request.POST.get('ad1')
         obj.Dob=request.POST.get('d1')
         obj.photo=request.POST.get('f1')
         obj.save()
     return render(request,'sample.html')

def view_data(request):
    obj=Student.objects.all()
    return render(request,'data_view.html',{'x':obj})