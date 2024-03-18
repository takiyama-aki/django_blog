from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post # データベースをインポート

def frontpage(request):
    # Postデータベースのオブジェクトを全て取得する
    posts = Post.objects.all()
    
    # frontpage.htmlをサーバーに返す
    return render(request, "blog/frontpage.html", {"posts": posts}) # "posts"という名前でpostsのデータを渡す

def post_detail(request, slug):
    # Postデータベースのslugが引数のslugのやつと同じオブジェクトを取得する
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            # どこにページ遷移するのか
            return redirect("post_detail", slug=post.slug)
        
    else:
        form = CommentForm( )

    return render(request, "blog/post_detail.html", {"post": post, "form": form})