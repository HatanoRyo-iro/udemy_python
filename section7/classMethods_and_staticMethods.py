class Person(object):
    
    kind = 'human'
    
    def ___init__(self):
        self.x = 100
    
    # def what_is_your_kind(self):
    #     return self.kind
    
    # これならまだオブジェクトじゃないからできる
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind
    
    @staticmethod
    def about(year):
        print(f'about human {year}')
    
a = Person()
print(a.what_is_your_kind())
b = Person   # まだクラスのまま　オブジェクトにしているわけではない
print(b.kind)   # これはアクセスできる
print(b.what_is_your_kind())   # 上のやつだとこれはダメ

"""
オブジェクトを生成していないけど、インスタンスにアクセスしたい場合は
@classmethodデコレーターを使用する
"""
print(Person.kind)
print(Person.what_is_your_kind())

Person.about(1999)