from django.shortcuts import render
from register.models import Profile
# Create your views here.
def chat(request):
    if request.method=="GET":
        
        
        return render(request,"index.html")
    
    
def blog(request):
    if request.method=="GET":
        return render (request,"blog.html")