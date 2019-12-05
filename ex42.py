 ## Animal is- a object (yes, sort of confusing) look at the extra credit
class Animal(object):
 pass
 
## ??
class Dog(Animal):

 def __init__(self, name):
  self.name = name
  print self.name

class Cat(Animal):
 def __init__(self, name):
  self.name = name
  print self.name 

class Person(object):
 def __init__(self, name):
  self.name = name
  self.pet = None

 def changepet(self,n):
  self.pet=n
 
 def abc(self):
  print self.pet

class Employee(Person):
 def __init__(self, name, salary):
  super(Employee, self).__init__(name)
  self.salary = salary

class Fish(object):
 pass

class Salmon(Fish):
 pass

class Halibut(Fish):
 pass

rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.changepet("dog")
mary.abc()
frank = Employee("Frank", 120000)
frank.pet = rover
flipper = Fish()
