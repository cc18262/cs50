from django.http.response import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "hello/index.html")    

def henry(request):
    return HttpResponse("Hello, henry")

def brian(request):
    return HttpResponse("Hello, brian")
"""
def greet(request, name):
    return HttpResponse(f"Hello,{name.capitaliza()}!")
    #.capitalizaは最初の文字を大文字に変換してくれるメソッド
"""

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
    #request,nameとすることでname変数を使えるようにしている。24行目でnameに文字列メソッドを追加している    
