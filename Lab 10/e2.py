class Car():
    def __init__(self, brand='Ford', color='red', pilote='person', speed=0):
        self.brand = brand
        self.color = color.title()
        self.pilote = pilote
        self.speed = speed
    def choice_driver(self, name):
        self.pilote = name
    def accelerate(self, flow, duration):
        if self.pilote == 'person':
            print('This car does not have a driver !')
        else:
            self.speed += flow * duration
    def display_all(self):
        print('{} {} driven by {}, speed = {} m/s.'.format(self.color, self.brand, self.pilote, self.speed))
a1 = Car('Peugeot', 'blue')
a2 = Car(color='green')
a3 = Car('Mercedes')
a1.choice_driver('Romeo')
a2.choice_driver('Juliette')
a2.accelerate(1.8,12)
a3.accelerate(1.9,11)
a2.display_all()
a3.display_all()
