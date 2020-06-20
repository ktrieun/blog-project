from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'KevinNguyen',
        'title': 'Test Post',
        'content': 'Testing Blog Post Content',
        'date_posted': '20 June 2020'
    },
    {
        'author': 'KevinNguyen',
        'title': 'Test Post 2',
        'content': 'Testing Blog Post Content 2',
        'date_posted': '20 June 2020'
    },
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})