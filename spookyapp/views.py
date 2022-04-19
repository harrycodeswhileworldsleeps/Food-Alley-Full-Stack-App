from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Blog

def main(request):
    return render(request,'spookyapp/index.html')

def BlogView(DetailView):
    model=Blog

def main2(request):
    return render(request,'spookyapp/index2.html')

def main3(request):
    return render(request,'spookyapp/index3.html')