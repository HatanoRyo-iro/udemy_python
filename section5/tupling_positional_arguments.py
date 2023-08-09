def say_something(word, *args):
    print('word = ', word)
    for arg in args:
        print(arg)
    
say_something('hi', 'Mike', 'Nancy')   # hiはwordに入り、2つ目以降の引数はタプルになる

t = ('Mike', 'Nancy')
say_something('hello', *t)   # タプルをアンパッキングして渡す