# 管理者画面
# models.pyのクラスを登録して利用する
# データベースにも保存できる

from django.contrib import admin
from .models import Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)