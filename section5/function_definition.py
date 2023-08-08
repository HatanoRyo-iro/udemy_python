def say_something():
    print('hi')
    
say_something()
print(type(say_something))

print('####################')

def say_something2():
    s = 'hi'
    return s

result = say_something2()
print(result)

print('####################')

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"
    

result = what_is_this('green')
print(result)


print('####################')

def add_num(a: int , b: int) -> int:
    return a + b

# r = add_num('a', 'b')   # 別にint型でなくてもエラーにならない
r = add_num(10, 20)
print(r)