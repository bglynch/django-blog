# posts/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def get_posts(request):
    posts = Post.objects.all()
    return render(request, "posts/blogposts.html", {'posts': posts})
    
def post_detail(request, pk):
    '''
    Create a view tthat returns a single Post object based on the Post ID (pk) and 
    render it to the 'postdetail.html' template
    '''
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "posts/postdetail.html", {'post': post})