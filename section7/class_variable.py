class Person(object):
    
    kind = 'human'
    
    def __init__(self, name):
        self.name = name
        
    def who_are_you(self):
        print(self.name, self.kind)
        
a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()


class T(object):
    
    words = []
        
    def add_word(self, word):
        self.words.append(word)
        

c = T()
c.add_word('add 1')
c.add_word('add 2')
print(c.words)

d = T()   # このようなクラス変数の定義だとリストが共有されてしまう。　嫌ならdef __init__(self):で定義
d.add_word('add 6')
d.add_word('add 8')
print(c.words)