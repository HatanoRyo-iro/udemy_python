count = 0

# while count < 5:
#     print(count)
#     count += 1

while True:
    if count >= 5:
        break
    
    if count == 2:
        count += 1
        continue
    
    print(count)
    count += 1
    
print('##############')
# while else文

count = 0

while count < 5:
    if count == 1:
        break   # breakしてしまうのでelseには行かない
    print(count)
    count += 1
else:   # whileの中でbreakで抜けなければ実行される
    print('done')