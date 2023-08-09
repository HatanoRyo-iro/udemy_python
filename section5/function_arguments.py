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