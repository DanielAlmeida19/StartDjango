from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from blog.data import posts
from typing import Any

def blog(request):
    print('blog do app 1')

    context = {
            # 'text': 'Olá blog',
            'posts': posts
            }
    return render(
        request,
        'blog/index.html',
        context
    )

def exemplo(request):
    print('exemplo')

    context = {
            'text': 'Olá exemplo',
            'title': 'Esta é uma página de exemplo - '
            }
    return render(
        request,
        'blog/exemplo.html',
        context
    )

def post(request: HttpRequest, post_id: int) -> HttpResponse:
    found_post: dict[str, Any] = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe')

    context = {
            # 'text': 'Olá blog',
            'post': found_post,
            'title': found_post['title'] + ' - '
            }
    return render(
        request,
        'blog/post.html',
        context
    )
