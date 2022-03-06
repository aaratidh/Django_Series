from django.shortcuts import render

posts = [{
    'author': 'CoreyMS' ,
    'title':'Blog Post 1',
    'content': 'First post Content',
    'date_posted': 'Agust 27, 2018',

},
    {
        'author': 'Jane',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'August 27, 2018',
     }
]

#display what user wants to see 
def home(request):
    context = {
        'posts': posts
    }
    return render(request,'web_app/home.html', context)

def about(request):
    return render(request,'web_app/about.html' ,{'title':'About'})
