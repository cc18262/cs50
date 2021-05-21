class Point():#クラス名
    # A method defining how to create a point:
    def __init__(self, x, y):#インスタンス化メソッド
        self.x = x  #横の位置の値をつける
        self.y = y
    
    #クラス内のメソッドの最初の引数はselfでないといけない