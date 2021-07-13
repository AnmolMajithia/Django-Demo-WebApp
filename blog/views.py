from django.shortcuts import render

posts = [
    {
        'author': 'AnmolM',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'June 13, 2021'
    },
    {
        'author': 'Dummy1',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'June 14, 2021'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
