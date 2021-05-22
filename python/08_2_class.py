class Flight():
    # Method to create new flight with given capacity
    #ここでcapacityプロパティを作成し、passengerプロパティに空のリストを代入するようにした
    #このクラスがインスタンスになり、値が入力された場合、capacityに代入される
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Method to add a passenger to the flight:
    #ここでadd_passengerメソッドを作成
    #このメソッドが呼ばれ、値が入力された場合、nameプロパティとして入力値は扱われる
    #もし、open_seatsメソッドがゼロ（＝falseを表す、pythonの場合）を返した場合、falseが返ってくる。
    # notを使うことでfalseが返ってきた場合が、if式全体ではではtrueだと扱われるようにしている。
    #なのでfalseが返ってきたらtrue式にいき、falseが返され、trueが返ってきたらfalse式に行くようになっている。
    #passengerプロパティに入力された値を追加してtrueを返す
    #false、trueを返すのは46行目からのfor文を回すために必要だから
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    """open_seatsでtrue=ゼロ以外の値が返ってきて、それをtrueで扱う場合のif式
        これでもきちんと動作します
    def add_passenger(self, name):
        if self.open_seats():
            self.passengers.append(name)
            return True

    """
    # Method to return number of open seats
    #空席があるかの確認のためのメソッド。flight変数にクラスと一緒に代入された値が飛行機のキャパ、passengerプロパティ
    # のリストに格納された乗客名から乗客数を割り出してキャパと比較し、空席数を返している
    def open_seats(self):
        return self.capacity - len(self.passengers)

# Create a new flight with o=up to 3 passengers
#インスタンスにキャパを代入
flight = Flight(3)

# Create a list of people
#リストなのでpassengerプロパティに代入される
people = ["Harry", "Ron", "Hermione", "Ginny"]

# Attempt to add each person in the list to a flight
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")

""" Output:
Added Harry to flight successfully
Added Ron to flight successfully
Added Hermione to flight successfully
No available seats for Ginny
"""
"""まとめ：
self.~で変数をメソッド内でもアクセスできるインスタンス変数に変化させている
クラス内でのdef ~~はメソッド、通常のdefは関数
変数を持った、クラスを変数に代入することでインスタンスを生成している＝変数に応じて処理できるようにしている
＝実体化させている
"""