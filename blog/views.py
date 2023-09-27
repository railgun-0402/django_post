from django.shortcuts import render, redirect
from .models import Post
from blog.forms import CommentForm

def frontpage(request):
    # DBから全て取得
    posts = Post.objects.all()
    # HTMLファイルを返す
    return render(request, "blog/frontpage.html", {"posts": posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
            # 有効な場合
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("post_detail", slug=slug)
    else:
        form = CommentForm()
        
    return render(request, "blog/post_detail.html", {"post": post, "form": form})

