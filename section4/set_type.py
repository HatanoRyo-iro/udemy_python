# 集合型
a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)   # 重複はない
print(type(a))

b = {2, 3, 3, 6, 7}
print(b)

print('a-b', a - b)   # 差集合
print('b-a', b - a)   # 差集合

print('a & b', a & b)   # 積集合

print('a | b', a | b)   # 和集合

print('a ^ b', a ^ b)   # 排他的論理和