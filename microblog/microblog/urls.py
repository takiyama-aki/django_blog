
from django.contrib import admin
from django.urls import path

from blog.views import frontpage, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),                       # djangoオリジナルの管理者画面 [user: admin pass: pass1234]
    path("", frontpage),                                   # ""のパスが呼ばれたら, frontpage関数を探す (views.py)
    path("<slug:slug>/", post_detail, name="post_detail")  # "<slug:~/"のパスが呼ばれたらpost_detail関数を探す, nameはhref属性で使う
]
