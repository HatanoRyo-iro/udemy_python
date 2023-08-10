def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)
    
# menu(entree='beef', drink='coffee')   # beef coffee

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
menu(**d)   # 辞書をアンパッキングして渡す


print('----------------------------------')

# 位置引数とタプル化と辞書化の組み合わせ

def menu2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)
    
menu2('banana', 'apple', 'orange', entree='beef', drink='coffee')
"""
出力結果

banana
('apple', 'orange')
{'entree': 'beef', 'drink': 'coffee'}
"""