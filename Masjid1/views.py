from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

def home(request):
    return render(request,'index.html')

def registration(request):
    return render(request,'registration.html')

def progress(request):
    surah = [a for a in range(0,115)]
    ayat = [a for a in range(0,287)]
    return render(request,'progress.html',{'surahs':surah,'ayats':ayat})

def fee_record(request):
    month = [m for m in range(1,13)]
    year = [y for y in range(1980,2025)]
    # print(month)
    return render(request,'fee_record.html',{'months':month,'years':year})

def student_record(request):
    return render(request,'student_record.html')

def account_record(request):
    month = [m for m in range(1,13)]
    year = [y for y in range(1980,2025)]
    # print(month)
    return render(request,'account_record.html',{'months':month,'years':year})

def expense(request):
    month = [m for m in range(1,13)]
    year = [y for y in range(1980,2025)]
    data = ['Salary','Income','Gift']
    # print(month)
    return render(request,'expense.html',{'months':month,'years':year,'data':data})
