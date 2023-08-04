x = {'a': 1}
y = x
# list同様、参照渡しとなってしまう
y['a'] = 1000
print(x)   # xも変わる
print(y)

print('-----避けるには-----')
x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)