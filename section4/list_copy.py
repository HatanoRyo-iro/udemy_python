i = [1, 2, 3, 4, 5]
j = i
j[0] = 100   # i[0]も100になる(アドレスの先頭を指しているだけだから同じ)
print('j =', j)
print('i =', i)

print('#################')

x = [1, 2, 3, 4, 5]
y = x.copy()
# y = x[:]   # こっちでも同じ
y[0] = 100
print('y =', y)
print('x =', x)

print('#################')

#   整数とか数字は値渡し、リストや辞書は参照渡し

X = 20
Y = X
Y = 5
# 値渡しの場合はアドレスが変わる
print(id(X))
print(id(Y))
print('X =', X)
print('Y =', Y)

X = ['a', 'b']
Y = X
Y[0] = 'p'
# 参照渡しの場合はアドレスが変わらない
print(id(X))
print(id(Y))
print('X =', X)
print('Y =', Y)
