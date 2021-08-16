from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Post, Tag
from .utils import objectDetailMixin

from .forms import TagForm


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context = {'posts': posts})


class PostDetail(objectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(objectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
    
class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context = {'form': form})