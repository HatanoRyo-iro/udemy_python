# pythonはセミコロンを書いてはいけない
x = 1;
y = 2;

print(x,y)

print('###################################')

# ラインの長さ
"""
長さは80文字以下にしよう
超える場合は\を入れて改行しよう
"""

def test_func(x, y, z, 
              dsfkdjsafljaflasjdf):
    
    """
    以下のようなURLは改行しない
    
    See details at: http://fajdoifoasdjfpoajfaosdjfsodfjaosjfafjasdfdasd
    """

print('###################################')

# 必要な時は書くが、無駄なものは書かない
if (x and y):   # <- こういう()のこと
    print('faj')
    
if (x):
    print('fdaj')
    
print('###################################')

# インデントは4

x = {
    'test': 'aaa'   # セミコロンの後ろは一個スペース空ける
}

x, y = y, x
x = y
# 関数のデフォルト引数とか渡す時はスペースなし
def test(abcd='test'):
    print('not space')

print('###################################')

"""
class同士は2行空ける
def同士も2行空ける

class内のメソッド同士は1行空ける


import の下も2行空ける

グローバルの変数の下も2行空ける

"""

print('###################################')

word = 'hello'
word2 = '!'

new_word = '{}{}'.format(word, word2)   # くっつけるのはこれはだめ
new_word = word + word2


"""
ループの時
どんどん文字を足していくより、いったんリストにappend指定って最後にjoinしたほうがいい
"""
long_word = ''
for word in ['fajdf', 'fjaodj', 'ojgteng']:
    long_word += "{}sdjfoad".format(word)
    
print('longword', long_word)
    
# こっちの方がメモリの管理上、都合がいい
long_word = []
for word in ['fajdf', 'fjaodj', 'ojgteng']:
    long_word.append("{}sdjfoad".format(word))
new_long_word = ''.join(long_word)

print(long_word)
print('new_long_word', new_long_word)


print('###################################')


"""
''は中に何も処理するものがない時
""はスペシャルキャラクターがあったりとか、代入するものがある時に使う


※但し企業による。
"""
# 文字列
print('faodjf')
print("fao'djf")

# 代入する時
"faidhfaidf {} faodfjai".format('test')

print('###################################')

# #の後は一個開ける

# TODO (hatano) 企業内で自分が使っているユニーク（例えばemailの@の前のものとか）自分の作業がわかる

print('###################################')

# import に関して、カンマを使えば横にかけるが書かない

print('###################################')


"""
企業にはよるが、2行推奨
"""
if x:
    print('aaa')
else:
    print('bbb')
    
if x: print('aaa')
else: print('bbb')

print('###################################')

# 大文字を使うか、小文字を使うか

"""
classに関しては、初めは大文字、つなげる場合も大文字　　=キャメルケース
defに関して、_でつなげる　　　=スネークケース


global変数は全部大文字で_で繋ぐ　でも、なるべくblobal変数は使わない(書き換えられるから)

"""


print('###################################')

"""
def main():
    start()
    
if __name__ == '__main__':
    main()
    
のような形で書く
"""

