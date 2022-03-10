from django.shortcuts import render
from .models  import Post 

#display what user wants to see 
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'web_app/home.html', context)

def about(request):
    return render(request,'web_app/about.html' ,{'title':'About'})
