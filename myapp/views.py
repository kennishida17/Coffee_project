from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_at')[:3]
    return render(request, 'myapp/index.html', {'posts':posts})

def postlist(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'myapp/postlist.html', {'posts':posts})

def add(request):
    if request.method == 'POST':
        post = Post()
        post.store_name = request.POST['store_name']
        post.ordereddrink = request.POST['ordereddrink']
        post.amount = request.POST['amount']
        post.save()
        return HttpResponseRedirect('/top')
    else:
        return render(request, 'myapp/create.html')

def detail(request,post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'myapp/detail.html',{'post':post})

def overview(request):
    return render(request, 'myapp/overview.html')

def contact(request):
    return render(request, 'myapp/contact.html')