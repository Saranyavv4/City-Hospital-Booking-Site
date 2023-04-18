from django.shortcuts import render
from .models import Departments,Doctors
from .forms import BookingForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def booking(request):
    if request.method == "POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    doc_dict={
        'docs':Doctors.objects.all()
    }
    return render(request,'doctors.html',doc_dict)


def department(request):
    dep_dict={
        'dep':Departments.objects.all()
    }
    return render(request,'department.html',dep_dict)
