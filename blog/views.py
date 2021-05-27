from django.shortcuts import render

posts = [
    {
        'author': 'Kush',
        'title': 'Blog Post 1',
        'content': 'Post 1 content is big',
        'date_posted': 'May 27, 2021'
    },

    {
        'author': 'Kushal',
        'title': 'Blog Post 2',
        'content': 'Post 2 content is small',
        'date_posted': 'May 28, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
