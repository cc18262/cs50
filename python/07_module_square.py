from function import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")

#function.pyファイルからsquare関数を呼び出している

"""
import functions

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")

function.pyファイルをimportして、使いたいときに
function.~~とすることでも関数の呼び出しが出来る

"""