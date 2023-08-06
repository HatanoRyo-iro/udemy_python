"""
range関数
enumerate関数
zip関数        の紹介
"""

# range関数
for i in range(2, 10, 3):   # 2から9まで3ずつ増える
    print(i)
    
# for i in range(10):
#     print(i, 'hello')

for _ in range(10):   # iを使わない場合は_を使って明示的にする
    print('hello')
    
    
    
print('####################')

# enumerate関数

# i=0
# for fruit in ['apple', 'banana', 'orange']:
#     print(i, fruit)
#     i += 1

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, ':' ,fruit)
    
    
print('####################')

# zip関数
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# for i in range(len(days)):
#     print(days[i], fruits[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)