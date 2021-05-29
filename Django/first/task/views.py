from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http  import HttpResponseRedirect, request

def index(request):
    #htmlから送られてきたtasksセッションが無かったらリストを創る
    if"tasks" not in request.session:
        request.session["tasks"] = []
    #セッションがあればhtmlのtasksにリストを持たせる
    return render(request, "tasks/index.html", {
        "tasks":request.session["tasks"]
    })
# Add a new task:
def add(request):#addリクエストが飛んだとき起動

    # Check if method is POST
    #リクエストがポストメソッドかどうか判断＝何かデータが送られていないか判断しているという事
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        #NewTskFormに送られてきたデータを持たせてインスタンスを実体化させる
        #つまりformでformモジュールの関数やメソッドを使えるようにするという事
        form = NewTaskForm(request.POST)

        # Check if form data is valid (server-side)
        #呼び出させるとデータを検証して、trueを返す。
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            #検証されるとform.cleaned_dataディクショナリに格納されるのでそこから取り出す
            task = form.cleaned_data["task"]

            # Add the new task to our list of tasks
            #取り出したデータをセッションのtaskリストに追加する

            request.session["tasks"]+= [task]

            # Redirect user to list of tasks
            #正常に追加出来たらtask:index urlを返して画面を変える
            return HttpResponseRedirect(reverse("tasks:index"))

        else:

            # If the form is invalid, re-render the page with existing information.
            #データの検証が出来なかった場合（＝最初に画面に来た時やデータが送れてなかった場合）
            # にadd.htmlを返す
            return render(request, "tasks/add.html", {
                "form": form
            })
    #addリクエストが着た場合task/add.htmlを NewTaskForm()インスタンスをformに持たせて返す
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })

#このクラスは単なるformのフィールドを意味している。
#継承したformsモジュールの中のform関数を使い、文字入力可能なフォームを持つ変数taskを作っている
#すると、初めてレンダリングされるとき　input id=変数,type=text,name=label required　となる
#そして上の処理でこのインスタンスを持たせることで
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


        