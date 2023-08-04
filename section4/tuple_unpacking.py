num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)
print(type(x), type(y))

x, y = (10, 20)
print(x, y)

x, y = 10, 20   # 実際には直接代入してるのではなく、タプルから展開して代入している
print(x, y)

min, max = 0, 100
print(min, max)

a, b, c, d, e, f = 'Mike', '1', '1', '1', '1', '1'
a = 'Mike'
b = '1'



# タプルのアンパッキングを利用した数字の入れ替え

i = 10
j = 20
print('入れ替え前',  i, j)

tmp = i
i = j
j = tmp
print('入れ替え後', i, j)

print('########アンパッキングを利用して簡単に入れ替える#########')

a = 100
b = 200
print('入れ替え前',  a, b)
a, b = b, a
print('入れ替え後', a, b)