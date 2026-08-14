class Dog:
  def __init__(self,name,breed,owner):
    self.name = name
    self.breed = breed
    self.owner = owner
  def bark(self):#instance method
    print("woof woof")
class Owner:
  def __init__(self,name,address):
    self.name = name
    self.address = address

owner = Owner("Alice","pedanindrakolanu")

dog1 = Dog("Leo","idea",owner)

print(dog1.owner.name)
dog1.bark()

'''
what is self ?
In python self is a special parameter thar refers to instance of a class.
It helps python to recognize the method belongs to the instance of a class
so, first parameter of method with in the class must be self

what is __init__? 
It is a special method which runs only once when object is created

what is instance Variable and instance Method?
variable which belongs to the object is called instance variable
In above example (name,breed,owner) are instance variables 
bcoz this info only belongs to the dog1.
if other dog object created this values may get changed. so these are called instance variable
Simillarly
The methods which are belongs to objects are called instance methods
'''
