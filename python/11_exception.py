#pythonでゼロまたは文字などを除算するとエラーが起きる
#なのでそういった場合にエラーが起きた場合に対処をする為の処理を創る

import sys#sysは標準モジュールでシステムパラメータに関する関数が入っているライブラリ

#以下のtryではx,yにint型以外の値を入れた場合valueErrorになり、11行目の文がprintされ異常終了として終了ステータス
#が指定される＝プログラムが終了する
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)
#以下のtryではゼロで除算した場合エラー文が出て、プログラムが終了するようになっている。
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program
    sys.exit(1)

#何もなければx変数とy変数の結果のresult変数がprintされる    
print(f"{x} / {y} = {result}")