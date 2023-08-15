class Person(object):
    def talk(self):
        print('talk')
        
    def run(self):
        print('person run')
        
        
class Car(object):
    def run(self):
        print('car run')
        
"""
継承するクラスの引数の順番で継承されるため、
二つ目のクラスに一つ目のクラスと同じメソッドがあった場合、
一つ目が優先される   

今回ならPersonCarRobotはPerson、Carの順番であり
Personのrunメソッドが優先される
"""
class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')
        
person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()