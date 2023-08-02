print('a is {}'.format('a'))

print('a is {}'.format('test'))

print('a is {} {} {}'.format(1, 2, 3))
print('a is {2} {1} {0}'.format(1, 2, 3))

print('My name is {} {}.'.format('Taro', 'Yamada'))
print ('私の名前は {name} {family}です.'.format(name='Taro', family='Yamada'))


a='1'
print(type(a))
print(int(a))
print(type(int(a)))

print(('##############'))

# f-string
name = "yuka"
family = "yamada"

print(f'She is {name} {family}.')