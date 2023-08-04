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


print('----------------')

# 集合の使い所
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}

print('共通の友達', my_friends & A_friends)   # 共通の友達


# ユニークなものだけ出力したい
f = ['apple', 'banana', 'apple', 'banana']
print(f)   # 重複あり
kind = set(f)
print(kind)   # 重複をなくす