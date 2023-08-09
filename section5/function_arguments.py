def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ',drink)
    print('dessert = ', dessert)
    
menu(entree='beef', dessert='ice', drink='beer')   # キーワードを指定すれば順序は関係ない
menu('beef', dessert='ice', drink='beer')   # 一つ目の引数はキーワードを指定しなくてもいい

print('####################')

# デフォルト引数
def menu2(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ',drink)
    print('dessert = ', dessert)
    
menu2('chicken', dessert='chocolate')   # デフォルト引数を上書きできる


print('####################')

# デフォルト引数で気をつけること
def test_func(x, l=[]):   # 暗黙の了解としてデフォルト引数でリストを与えるべきではない
    l.append(x)
    return l

# x = [1, 2, 3]
# r = test_func(100, x)   
# print(r)

# x = [1, 2, 3]
# r = test_func(200, x)
# print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)



# じゃあどうするか
def test_func2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func2(100)
print(r)

r = test_func2(100)
print(r)