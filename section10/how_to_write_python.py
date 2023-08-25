# 関数をimportするのはやめよう
"""
NG : from roboter.contoroller.conversation import talk_about_restaurant
OK : import roboter.contoroller.conversation　
    で実行する時にroboter.contoroller.conversation.talk_about_restaurant()にする
"""

"""
import の順番としては

1. 標準モジュール(アルファベット順で)
2. サードパーティライブラリ(アルファベット順で)
3. 自作ライブラリ(アルファベット順で)

例：

import os
import sys

import flask

import roboter.contoroller.conversation
"""


print('################################')

# exceptionの話
"""
こういうどれにでも当てはまるExeptionで処理を書くのはやめる。
具体的なエラーのやつにする
"""
try:
    print('aaa')
except Exception as exc:
    print('error')
    
"""
一番上のExceptionを継承して、自作のエラーを作る

例外処理のところを復習
"""


print('################################')

d = {'key1': 'value1', 'key2': 'value2'}
if 'key1' in d:
    print('入ってるよ')
    
if 'key1' in d.keys():   # こういう無駄なことはしない
    print('test')

# ちゃんとした名前にした方がわかりやすい
"""
例：

for name, count in ranking.items():
    print(name, count)
    
だったり
"""
for k, v in d.items():   # 2行くらいだったらこれでもいいけど、ちゃんとした名前にした方がいい
    print(k, v)
    
    
print('################################')

# ジェネレーターを使えれば使う　ジェネレーターのほうが高速に動く

def t():
    num = []
    for i in range(10):
        num.append(i)
    return num

for i in t():
    print(i)
    
print('----')

def t():
    for i in range(10):
        yield i
        
for i in t():
    print(i)


print('################################')

# lambda

def other_func(f):
    print(f(10))

def test_func(x):
    return x * 2

def test_func2(x):
    return x * 5

other_func(test_func)
other_func(test_func2)

other_func(lambda x: x * 2)   # これだけで済む
other_func(lambda x: x * 5)

print('################################')

# 時々使われる
y = 'dadfad'
x = 1 if y else 2
print(x)

print('################################')

# リストは参照渡しなので初期化しない
"""
もしリストがNoneだったら初期化
ちがったらそのまま
"""
# リストのところを復習する


print('################################')

# クロージャー

def base(x):
    def plus(y):
        return x + y
    return plus

plus = base(10)
print(plus(10))
print(plus(30))


i = 0
def add_num():
    def plus(y):
        return i + y
    return plus

i = 10
plus = add_num()
print(plus(30))
i = 100   # 書き換えられる
print(plus(30))


print('################################')

# デコレーター
