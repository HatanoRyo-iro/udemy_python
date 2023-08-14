class Car(object):
    def __init__(self, model=None):
        self.model = model
        
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', 
                enable_auto_run=False,
                password = '123'):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run
        self.password = password
        
    # アンダースコア(_)が一個の時はpropertyと組み合わせて使うのがいい
    @property   # こうすることで書き換え不可になる(propertyデコレーターを使用)
    def enable_auto_run(self):
        return self._enable_auto_run
        
    @enable_auto_run.setter   # 書き換えを許可するには”変数名.setter”デコレーターを使用
    def enable_auto_run(self, is_enable):
        if self.password == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError
    
    def run(self):
        print(self.__enable_auto_run)
        print('super fast')
    def auto_run(self):
        print('auto run')



print('##########')
tesla_car = TeslaCar('Model S', password='111')
tesla_car.run()

