from django.shortcuts import render,HttpResponse,redirect
from django.views import View

# Create your views here.

def contact(request):
    return HttpResponse("This is contact page")
def login(request):
    return HttpResponse("This is a login page")
def home(request):
    return HttpResponse("This is a home page")
def edit(request,rid):
    print("Id to be edited is",rid)
    return HttpResponse("id to be edited is:"+rid)

def del1(request,pid):
    print("Id to be deleted is",pid)
    return HttpResponse("Id to be deleted is:"+pid)

def newhome(request):
    return render(request,'index.html')
class SimpleView(View):
    def get(self,request):
        return HttpResponse("Hello world!")

class NewView(View):
    def get(self,request):
        return HttpResponse("This is His view")
    
class OldView(View):
    def get(self,request):
        return HttpResponse("This is Old view")
    
def page2(request):
    return redirect('/page2')

def page1(request):
    return render(request,'index.html')

def oldpath(request):
    return redirect('/oldpath')

def newpath(request):
    return render(request,'new.html')
def hello(request):
    context={}
    context['name']='yashmahi'
    return render(request,'hello.html',context)
    
def city(request):
    newcont={}
    newcont['city']='pune'
    return render(request,'hello.html',newcont)