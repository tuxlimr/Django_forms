from django.shortcuts import render


def index(request):
    return render(request,"index.html",{'name':'Ajay'})


def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    res = int(val1)+int(val2)
    return render(request,"index.html",{'result':res})
