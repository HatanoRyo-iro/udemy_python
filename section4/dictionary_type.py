d = {'x': 10, 'y': 20}
print(d)
print(type(d))
print(d['x'])
d['x'] = 100
print(d)
d['x'] = 'XXXX'
print(d)

d['z'] = 200
print(d)

d[1] = 10000
print(d)


dict(a=10, b=20)   # これでも生成できる
print(dict(a=10, b=20))
print(dict([('a', 10), ('b', 20)]))
