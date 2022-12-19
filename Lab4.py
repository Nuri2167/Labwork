from dataclasses import dataclass


class Person:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age

    def __str__(self):
        return f'Username: {self.username}\nAge: {self.age}'


@dataclass
class Driver(Person):
    def __init__(self, experience: int, username: Person, age: Person):
        Person.__init__(self, username, age)
        self.experience = experience

    def __str__(self):
        return f'{self.username} has an experience of {self.experience} years'


class Engine:
    def __init__(self, power: int, producer: str):
        self.power = power
        self.producer = producer

    def __str__(self):
        return f'Engine power:{self.power} \n producer:{self.producer}'


@dataclass
class Car:
    def __init__(self, brand: str, carClass: str, weight: float, driver: Driver, engine: Engine):
        self.brand = brand
        self.carClass = carClass
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turnRight(self):
        print('Turn to the right')

    def turnLeft(self):
        print('Turn to the left')

    def __str__(self):
        return f' Car brand: {self.brand} \n class: {self.carClass} \n' \
               f' weight: {self.weight} \n driver: {self.driver} \n' \
               f' engine: {self.engine} \n'

@dataclass()
class Lorry(Car):
    def __init__(self, carrying: int):
        self.carrying = carrying

    def __str__(self):
        return super().__str__() + f'carrying: {self.carrying}'


@dataclass()
class SportCar(Car):
    def __init__(self, speed: float):
        self.speed = speed

    def __str__(self):
        return super().__str__() + f'speed: {self.speed}'


person = Person(username='Nur Erkinkyzy', age='22')
driver = Driver(username='Nur Erkinkyzy', age='22', experience='2')
car = Car(brand='Mers', carClass='S class', weight='53', driver='Bek', engine='53')
print(driver)
car.start()
car.stop()
