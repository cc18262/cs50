def square(x):
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}")

""" 
squareという関数を作成したことで、for文の中でも計算できるようになっている
Output:
The square of 0 is 0
The square of 1 is 1
The square of 2 is 4
The square of 3 is 9
The square of 4 is 16
The square of 5 is 25
The square of 6 is 36
The square of 7 is 49
The square of 8 is 64
The square of 9 is 81
"""