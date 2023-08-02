a = 'My name is Mike. Hi Mike.'
print(a)
is_start = a.startswith('My')
print(is_start)
is_start = a.startswith('L')
print(is_start)

print('#################')

print(a.find('Mike'))
print(a.rfind('Mike'))
print(a.count('Mike'))
print(a.capitalize())
print(a.title())   # 単語の先頭を大文字にする
print(a.upper())
print(a.lower())

print(a.replace('Mike', 'Nancy'))