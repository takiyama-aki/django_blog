# クラスとしてデータベースを作成する

from django.db import models

# ブログの投稿内容データベース
class Post(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add = True)

# 投稿に対するコメントデータベース
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE) # 1つの投稿に対して複数のデータがある,Postデータベースに紐づけを行っている
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add = True)