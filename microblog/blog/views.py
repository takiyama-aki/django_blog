from django.shortcuts import render, redirect, get_object_or_404

from .forms import CommentForm, NewPost
from .models import Post # データベースをインポート

def frontpage(request):
    # Postデータベースのオブジェクトを全て取得する
    posts = Post.objects.all()
    print("frontpage test")
    # frontpage.htmlをサーバーに返す
    return render(request, "blog/frontpage.html", {"posts": posts}) # "posts"という名前でpostsのデータを渡す

def post_detail(request, slug):
    # Postデータベースのslugが引数のslugのやつと同じオブジェクトを取得する
     # Postデータベースのslugが引数のslugのやつと同じオブジェクトを取得する
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # コメントが保存されたことをユーザーに通知
            return render(request, "blog/post_detail.html", {"post": post, "form": form, "comment_saved": True})
    else:
        form = CommentForm()

    return render(request, "blog/post_detail.html", {"post": post, "form": form})

def new_post(request):
    
    # Postデータベースのオブジェクトを全て取得する
    # posts = Post.objects.all()
    
    # frontpage.htmlをサーバーに返す
    print("new post test")
    return render(request, "blog/new_post.html") # "posts"という名前でpostsのデータを渡す