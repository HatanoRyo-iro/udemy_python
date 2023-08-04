d = {'x' : 10, 'y' : 20}

print(d.keys())
print(d.values())

d2 = {'x' : 1000, 'j' : 500}
print(d2)

d.update(d2)   # オーバーライド
print(d)
print(d['x'])
print(d.get('x'))

# print(d['z'])   # エラー
print(d.get('z'))   # Noneが帰ってくる
r = d.get('z', -1)   # -1が帰ってくる
print(r)

print(d)
d.pop('x')   # 削除
print(d)
del d['y']   # 削除
print(d)

d.clear()   # からの辞書になる　del dならそもそもが消えるからエラーになる

print('------------------')
d = {'a' : 100, 'b' : 200}
print('a' in d)   # True
print('j' in d)   # False
