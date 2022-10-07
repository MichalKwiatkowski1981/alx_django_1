from pprint import pprint

from django.contrib.auth.models import User

from posts.models import Post
from django.shortcuts import render, redirect

from tags.models import Tag


def posts_list(request):
    q = title__contains = request.GET.get('q')
    lista_postow = Post.objects.all()
    if q:
        lista_postow = lista_postow.filter(title__contains=q)
    lista_postow = lista_postow.order_by('-sponsored')
    context = {
        'posts_list': lista_postow,
    }
    return render(request, 'posts/list.html', context)


def posts_details(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, 'posts/details.html', context)


def toggle_sponsored(request, id):
    post = Post.objects.get(id=id)
    post.sponsored = not post.sponsored
    post.save()
    return redirect('posts:list')


def add_post_form(request):
    if request.method == "POST":
        pprint(dict(request.POST))
        data = {
            "title": request.POST['title'],
            "content": request.POST['content'],
            "published": 'published' in request.POST,
            "author": User.objects.get(id=request.POST['author'])
        }
        post = Post.objects.create(**data)
        for tag_id in request.POST.getlist('tags'):
            tag_id = int(tag_id)
            t = Tag.objects.get(id=tag_id)
            post.tags.add(t)
        return redirect('posts:list')
    else:
        # wczytać tagi
        # dodać do kontekstu
        context = {
            'tags': Tag.objects.all(),
            'authors': User.objects.all(),
        }
        return render(request, 'posts/add.html', context)