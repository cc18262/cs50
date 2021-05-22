#8行目でhello関数が呼ばれた場合デコレータを起動するようにし、任意＝（ｆ）でhello関数を処理するようにしている
def announce(f):
    #wrapper関数の中でhello関数を呼び出している
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce   #＠関数にしておくとデコレータにできる＝hello関数を値として扱えるようになる
def hello():
    print("Hello, world!")
#ここでhello関数を呼び出している。
hello()

""" Output:
About to run the function
Hello, world!
Done with the function
"""