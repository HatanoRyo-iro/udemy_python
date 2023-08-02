print('Hello')

print('I don\'t know')
print('say "I dont\'t know"')
print("say \"I dont't know\"")

print('Hello. \nHow are you?')
print(r'C:\name\name')   # rをつけるとraw文字列となり，エスケープ文字が無効になる


print("###############")
print("""\
line1
line2
line3\
""")
print("###############")


print('Hi.' * 3 + 'Mike.')

print('Py' 'thon')
prefix = 'Py'
print(prefix + 'thon')


word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[:5])
print(word[2:])

print('#################')

word = 'j' + word[1:]
print(word)
length = len(word)
print(length)