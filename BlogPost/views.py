from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Posts
from .forms import PostsForm

def index(request):
    return render(request, 'BlogPost/index.html')

@login_required
def post(request):
    posts = Posts.objects.filter(owner=request.user).order_by('date_added')
    context = {'posts': posts}
    return render(request, 'BlogPost/post.html', context)

@login_required
def new_post(request):

    if request.method != 'POST':
        form = PostsForm()
    else:
        form = PostsForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('BlogPost:post')
        
    context={'form': form}
    return render(request, 'BlogPost/new_post.html', context)

@login_required
def edit_post(request, post_id):
    post = Posts.objects.get(id=post_id)
    check_post_owner(request, post)

    if request.method != 'POST':
        form = PostsForm(instance=post)
    else:
        form = PostsForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            
    context={'post': post, 'form': form}
    return render(request, 'BlogPost/edit_post.html', context)

@login_required
def delete_post(request, post_id):
    post = Posts.objects.get(id=post_id)
    check_post_owner(request, post)
    Posts.objects.get(id=post_id).delete()
    return redirect('BlogPost:post')

def check_post_owner(request, post):
    if post.owner != request.user:
        raise Http404