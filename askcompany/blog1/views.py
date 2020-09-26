from django.shortcuts import render

from .models import Post


def post_list(request):
    queryset = Post.objects.all()
    return render(request, 'blog1/post_list.html', {
        'post_list': queryset,
    })
