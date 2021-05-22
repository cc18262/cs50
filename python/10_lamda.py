"""
ラムダ関数の使い方。
square = lambda x: x * x
：より左が入力、右が出力。lamda xとすることでsquareが関数としてあつかわれるようになる
"""

people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
#person[name]をラムダ関数でkey引数を関数として扱うようにしている。＝keyと入力したならばperson["name"]を自動で返すようになった
people.sort(key=lambda person: person["name"])

print(people)

""" Output:
[{'name': 'Cho', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'}, {'name': 'Harry', 'house': 'Gryffindor'}]
"""