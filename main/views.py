# from django.http import Http404
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from .models import Post

User = get_user_model()


def post_list(request):
    posts = Post.published.all()
    return render(request, 'main/post/list.html', {'posts': posts})


def post_detail(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    context = {
        'post': post,
    }
    return render(request, 'main/post/detail.html', context)
