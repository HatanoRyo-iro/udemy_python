class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)
        
    def say_something(self):
        print(f'I an {self.name}. hello')
        self.run(10)   # 自分自身のメソッドを呼び出すこともできる
        
    def run(self, num):
        print('run' * num)
        
         
person = Person('Mike')
person.say_something()