"""
and 逻辑与(并且)    2>1 and 3>2      所有条件均为 True，结果才为 True；任一为 False，结果即为 False
or  逻辑或(或者)    2>1 or 3<5       任一条件为 True，结果即为 True
not 逻辑非(取反)    not(2>1)         对布尔值取反，真变假、假变真
"""

# and 逻辑与(并且)    2>1 and 3>2      所有条件均为 True，结果才为 True；任一为 False，结果即为 False
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

print(1 < 2 < 3)  # True
print(2 > 1 and 3 < 2)  # False
print(2 < 1 and 3 > 2)  # False
print(1 > 2 > 3)  # False
print("=" * 50)

# or  逻辑或(或者)    2>1 or 3<5       任一条件为 True，结果即为 True
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# TODO 根据and的写法，补齐四个样例
print("=" * 50)

# not 逻辑非(取反)    not(2>1)         对布尔值取反，真变假、假变真
print(not True)  # False
print(not False)  # True
print(not (1 < 2 < 3))  # False
print(not (2 > 1 and 3 < 2))  # True