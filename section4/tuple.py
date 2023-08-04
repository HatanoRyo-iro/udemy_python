t = (1, 2, 3, 4, 1, 2)
print(t)

print(type(t))

# t[0] = 100   # エラーになる

print(t.count(1))

print(t.index(3))

t = ([1, 2, 3], [4, 5, 6])

print(t)
print(t[0][2])

t = 1, 2, 3, 4, 5
print(type(t))

# タプルは,をつける必要がある

new_tuple = (1, 2, 3) + (4, 5, 6)
print(new_tuple)
# new_tuple = (1) + (4, 5, 6)   # エラー
new_tuple = (1,) + (4, 5, 6)
print(new_tuple)


print('#################')
# タプルの使い所

chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)