from django.shortcuts import render
import datetime
#datetimeモジュールをインポートして下の処理で使えるようにしている
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        #"newyear": now.month == 1 and now.month == 1
        "newyear": True #newyaer変数にtrueを渡すという処理
    })
    #return render(request,newyear/index.html)でindexが呼び出されたときにindex.htmlを返す
    #requestに対してindex.htmlをnewyaerという変数にtrueかfalseを渡した状態でレンダリングして返すというのが
    #7行目以降の処理になる