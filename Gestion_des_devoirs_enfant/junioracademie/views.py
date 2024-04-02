from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def classe(request):
    return render(request,'class.html')

def team(request):
    return render(request,'team.html')

def gallery(request):
    return render(request,'gallery.html')

def blog(request):
    return render(request,'blog.html')

def single(request):
    return render(request,'single.html')

def contact(request):
    return render(request,'contact.html')
