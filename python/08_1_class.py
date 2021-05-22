class Point():#クラス名
    # A method defining how to create a point:
    def __init__(self, x, y):#インスタンス化メソッド
        self.x = x  #横の位置の値をつける
        self.y = y
    
    #最初のメソッドの引数にself、関数に__init__を用いて変数の初期化をするのが慣習らしい
    #最初のメソッドの引数に指定したキーワードを用いることで、プロパティへのアクセスができるようになる。（重要）
    #クラスで新しいオブジェクトを作るときはこれを書いてからスタート
    #このコードの場合、Pointというインスタンスに2,8という値が代入された場合、それをx,yに代入して返す処理になっている

p = Point(2, 8)
#ここで値を代入
#下の二つのprintでPointクラスのx,yの値を出している
print(p.x)
print(p.y)

""" Output:
2
8
"""
 