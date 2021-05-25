from django.urls import path
from . import views

#このエディターの予測変換でurlpatternsを書くと綴りがあっていても大文字小文字が合わずにエラーになる
#基本的に小文字で統一が吉かも
urlpatterns = [
    path("", views.index, name="index")
]