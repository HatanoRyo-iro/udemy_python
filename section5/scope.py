"""
Test scope ################
"""

animal = 'cat'

def f():
    #print(animal) これエラーになる　書くなら global animal
    animal = 'dog'
    print('local:', locals())

f()
print(__name__)
print('global:', globals())


print("####################")

def f2():
    """Test func doc"""
    print(f2.__name__)
    print(f2.__doc__)
    
f2()
print('global:', __name__)