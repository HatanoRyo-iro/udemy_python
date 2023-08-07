some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

for i in some_list:
    print(i)
    
for s in 'abcde':
    print(s)
    
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        # break
        continue
    print(word)
    
    
print('####################')

# for else文

for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break   # elseは実行されない
    print(fruit)
else:
    print('I ate all!')


print('####################')

# 辞書をfor文で処理する

d = {'x': 100, 'y': 200}
print(d.items())

for k, v in d.items():
    print(k, ':', v)