class Person(object):
    # コンストラクタ
    def __init__(self, name):
        self.name = name
        print(self.name)
        
    def say_something(self):
        print(f'I an {self.name}. hello')
        self.run(10)   # 自分自身のメソッドを呼び出すこともできる
        
    def run(self, num):
        print('run' * num)
        
    # デストラクタ
    def __del__(self):
        print('good bye')
         
person = Person('Mike')
person.say_something()

del person   # 明示的にデストラクタが呼ばれる

print('##########')