name = "Harry"
print(name[0])
print(name[1])
# 文字列の場合は配列の変更が出来ず、順序があると扱われる。

# This is a Python comment
names = ["Harry", "Ron", "Hermione"]
# Print the entire list:
print(names)
# Print the second element of the list:
print(names[1])
# Add a new name to the list:ここでリストに追加している
names.append("Draco")
# Sort the list:　ここで順番をアルファベット順に変更している
names.sort()
# Print the new list:
print(names)

#リストの場合は配列の中の変更と順番があるとされる

point = (12.5, 10.6)
#タプルは変更が出来ず、順番はある

# Create an empty set:
s = set()

# Add some elements:
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(1)

# Remove 2 from the set
s.remove(2)

# Print the set:
print(s)

# Find the size of the set:
print(f"The set has {len(s)} elements.")

""" This is a python multi-line comment:
Output:
{1, 3, 4}　同じ要素が複数追加されても1つしか格納されない、各種類毎にしか格納されないのが集合
The set has 3 elements.
"""

#集合には中身の順番が無く変更が出来る

# Define a dictionary
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
# Print out Harry's house
print(houses["Harry"])
# Adding values to a dictionary:
houses["Hermione"] = "Gryffindor"
# Print out Hermione's House:
print(houses["Hermione"])

""" Output:
Gryffindor
Gryffindor
"""
#キー：値のベアでprint(辞書[キー])で対応する値が出てくる

for i in [0, 1, 2, 3, 4, 5]:
    print(i)

""" Output:
0
1
2
3
4
5
"""
#ループのやり方 for版

for i in range(6):
    print(i)
""" output:
0
1
2
3
4
5
6
"""
#ループのやり方 range版

# Create a list:
names = ["Harry", "Ron", "Hermione"]

# Print each name:
for name in names:
    print(name)

""" Output:
Harry
Ron
Hermione
"""
#for文はどの配列も使える

name = "Harry"
for char in name:
    print(char)

""" Output:
H
a
r
r
y
"""
#for文は詳細に指定して、1つの要素の各文字をループできる