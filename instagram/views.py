from django.shortcuts import render
from .models import Post

def home(request):
    post = Post.objects.all().order_by('-date')
    content = {
        'post':post
    }
    return render(request, 'instagram/index.html', content)
