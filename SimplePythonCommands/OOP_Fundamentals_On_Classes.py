# prints Seattle 500 4 []
class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
    def start(self):
        print('Vroom!')

class Race:
    def __init__(self, race, driver_limit):
        self.race = race
        self.driver_limit = driver_limit
        self.drivers = []

    def add_drivers(self, driver):
        if len(self.drivers) < self.driver_limit:
            self.drivers.append(driver)
            return True
        return False
    def get_average_ranking(self):
        total_ranking_value = 0
        for driver in self.drivers:
            total_ranking_value += driver.get_ranking()
        return total_ranking_value / len(self.drivers)

class Driver:
    def __init__(self, driver, age, ranking):
        self.driver = driver
        self.age = age
        self.ranking = ranking
    def get_ranking(self):
        return self.ranking

my_driver = Driver('Dale Earnhardt', 29, 100)
print(my_driver.ranking)
print(my_driver.get_ranking())

s0 = Driver('Dale Earnhardt', 29, 100)
s1 = Driver('Lewis Hamilton', 36, 83)
s2 = Driver('Eliud Kipchoge', 36, 95)
s3 = Driver('Sebastian Vettel', 34, 76)
s4 = Driver('Ayrton Senna', 34, 99)

course = Race('Seattle 500', 8)

course.add_drivers(s0)
course.add_drivers(s1)
course.add_drivers(s2)
course.add_drivers(s3)
course.add_drivers(s4)
print(course.get_average_ranking())
# prints a returned value of "100"
print(course.drivers)


class Person:
  def __init__(self,in_name,in_age):
    self.name = in_name
    self.age = in_age
      
  def get_name(self):
    return self.name
  

class Customer(Person):
  def __init__(self, in_name, in_age):
    super().__init__(in_name,in_age)
    self.hasTicket = False
    self.inZoo = False
  
  def buy_ticket(self):
    if self.age <= 12:
      print(f"{self.name} has purchased a children's ticket for the zoo!")
    else:
      print(f"{self.name} has purchased an adult ticket for the zoo!")
    self.hasTicket = True

  def enter_zoo(self, zoo):
    if self.hasTicket:
      zoo.add_customer(self.name)
      self.hasTicket = False
      self.inZoo = True
    else:
      print("Please purchase a ticket before entering the zoo.")

  def exit_zoo(self, zoo):
    if self.inZoo:
      self.inZoo = False
      zoo.remove_customer(self.name)

class Zoo:
  def __init__(self,name="Local Zoo"):
    self.name = name
    self.animals = []
    self.customers = []

  def add_animal(self, animal):
    self.animals.append(animal)
    print(f"{self.name} has a(n) {animal}")
  
  def add_animals(self, animals):
    self.animals.extend(animals)
    print(f"{self.name} has many animals")
  
  def add_customer(self, name):
    self.customers.append(name)
    print(f"{name} has entered {self.name}")

  def remove_customer(self, name):
    self.customers.remove(name)
    print(f"{name} has left {self.name}")
  
  def visit_animals(self):
    for a in self.animals:
      print(f"visiting {a.get_name()}")
      a.make_noise()
      a.eat_food()

class Animal:
  def __init__(self,name):
    self.name = name
  def get_name(self):
    return self.name
  def make_noise(self):
    print("Every animal makes noise")
  def eat_food(self):
    print("All creatures need sustenance")

class Fish(Animal):
  def __init__(self, name):
    super().__init__(name)

  def make_noise(self):
    print(f"{self.name} says blub, blub, blub")
  
  def eat_food(self):
    print(f"{self.name} eats seafood.")

class Bird(Animal):
  def __init__(self, name):
    super().__init__(name)

  def make_noise(self):
    print(f"{self.name} says tweet, tweet")
  
  def eat_food(self):
    print(f"{self.name} eats seeds, nuts and berries.")

class Chimp(Animal):
  def __init__(self,name):  
    super().__init__(name)

  def make_noise(self):
    print(f"{self.name} says hoot-grunt")
  
  def eat_food(self):
    print(f"{self.name} eats seeds, fruit, leaves, and bark.")


nycZoo = Zoo("NYC Zoo")

salmon = Fish("salmon")
robin = Bird("robin")
bonobo = Chimp("bonobo")
nycZoo.add_animals([salmon, robin, bonobo])


    

alice = Customer("Alice",25)
bob = Customer("Bob",20)
charlie = Customer("Charlie",10)
dave = Customer("Dave",30)

for c in [alice, bob, charlie, dave]:
  c.buy_ticket()
  c.enter_zoo(nycZoo)
nycZoo.visit_animals()
for c in [alice, bob, charlie, dave]:
  c.exit_zoo(nycZoo)


