from django.urls import path
from . import views

#このエディターの予測変換でurlpatternsを書くと綴りがあっていても大文字小文字が合わずにエラーになる
#基本的に小文字で統一が吉かも
#app_nameとしておくとhtmlのformのリンクをいちいちディレクトリ名で設定しなくていいので修正が楽らしい
app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
]