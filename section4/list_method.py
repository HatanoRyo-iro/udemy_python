r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))   # インデックス[3]以降で最初に見つかった3のインデックスを返す

print(r.count(3))   # 2

if 5 in r:
    print('exist')
    
r.reverse()   # reverseメソッドはただリストを逆にするだけ
print(r)
    
r.sort()
print(r)

r.sort(reverse=True)   # sortメソッドの引数にreverse=Trueを取ると降順にソートされる
print(r)
r.reverse()
print(r)

print('#################')

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = '$$$'.join(to_split)
print(x)


print(help(list))   # help関数はそのオブジェクトのドキュメントを表示する