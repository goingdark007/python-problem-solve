class Vechile():
    def __init__(self,type,brand):
        self.type = type
        self.brand = brand

class Motor_cycle(Vechile):
    def __init__(self,type,brand,c,d):
        super().__init__(type,brand)
        self.top_speed = c
        self.mileage = d

class Car(Vechile):
    def __init__(self,type,brand,c,d):
        super().__init__(type, brand)
        self.price = c
        self.turbocharged = d

class Truck(Vechile):
    def __init__(self,type,brand, c, d):
        super().__init__(type, brand)
        self.weight = c
        self.wheels = d

class Ship(Vechile):
    def __init__(self, type, brand, c, d):
        super().__init__(type, brand)
        self.ship_type = c
        self.ship_speed = d

yamato = Ship('Big ship','Japanese','Battle ship-(destroyer class)','160 nautical miles/hour')

h2r = Motor_cycle('Motorcycle','Kawasaki',240,'60 miles/liter')

supra = Car('Car','Toyota','60 lakhs','twin turbo')

mitsubishi = Truck('Truck','Mitsubishi','100 tons',6)

def printing(obj,attributes):
    for i in attributes:
        print(f'{i} : {getattr(obj,i)}')

vehicles = {
    h2r:['top_speed','mileage'],
    supra:['price','turbocharged'],
    mitsubishi:['weight','wheels'],
    yamato:['ship_type','ship_speed']
}

list = [h2r,supra,mitsubishi,yamato]

for i in list:

    printing(i,['type', 'brand'] + vehicles.get(i, []))
    print()