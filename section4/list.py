l = [1, 2, 3, 4, 5]
print(l[0])

print(l[1:3])

print(l[:2])
print(l[:])

print(type(l))

after = list('abcdefg')
print(after)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])
print(n[::-1])

# ネスト
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])