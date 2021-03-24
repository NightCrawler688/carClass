class Car(object):
        def __init__(self,model,color,company,speed_limit):
                self.color = color
                self.model = model
                self.company = company
                self.speed_limit = speed_limit
        def start(self):
                print('Started')
        def stop(self):
                print('Finished')
        def acclerate(self):
                print('Accelerating')
        def change_gear(self,gear_type):
                print('Gear Changed')

audi = Car('A6','red','Audi','80')
print(audi.color)
print(audi.model)
print(audi.company)
print(audi.speed_limit)
print(audi.start())
print(audi.acclerate())
print(audi.change_gear('automatic'))
print(audi.stop())