from django.shortcuts import render
from .forms import *
from .models import *


def create(request):
    if request.method == 'POST':
        fm = studentsForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = studentsForm()
       
    fm = studentsForm()
    return render(request,'index.html', {'fm':fm})

# Create your views here.
