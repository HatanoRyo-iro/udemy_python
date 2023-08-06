y = [1, 2, 3]
x = 1

if x in y:
    print('in')
    
if 100 not in y:
    print('not in')
    
a = 1
b = 2

# if not a == b:
#     print('Not equal')

if a != b:   # こっちにする
    print('Not equal')
    
    
print('##############')

is_ok = True

if not is_ok:
    print('hello')
    
print('##############')

# 値が入っていない判定

# is_ok = True
# False, 0, 0.0, '', [], (), {}, set()
is_ok = [1, 2, 3, ]

if is_ok:
    print('OK!')
else:
    print('No!')