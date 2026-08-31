'''
Brid System
How to spot SRP violations
-->Large classes
-->Monster Methods
  void update():one method perform lot of work in it
    logic open DB   --> call open DB(not a monister)
    logic query push DB
    logic close DB
-->Many unrelated if/else block
-->Utility Class becoming dumping
--> Multiple Unrealated responsibilites inside one class
  
solution : Inheritance 

OCP --> A class should be opened for extension .but closed for modification
Regression : change that adds a side effect silently -->breaks existing functionality
Avoid Regression

Liskov substitution  principle(LSP):
A child object should be usable where ever its parents is excepted with out 
Breaking the correctness of the program
Force you to implement interface(can -- Interface)
class Explosion -->Multiple Inheritance

Interface Segregation Principle: how interface should look like 
(must follow SRP ,OCP)

Dependency Inversion Principle(DIP):
concrete class doesn't depend on directly on other concrete class.
depends on interface this help you to call common function
'''
from abc import ABC,abstractmethod
class Bird:
    def __init__(self,name,age,color):
        self.__name = name
        self.__age = age
        self.__color = color

    # def fly(self):
    #     if(self.__name == 'Pigeon'):
    #         print("Pigeon is flying")
    #     elif(self.__name == 'Crow'):
    #         print("Crow is flying")
    #     elif(self.__name == 'Duck'):
    #         print("Duck is Canot fly")
    @abstractmethod
    def fly():
        pass
    def eat():
        pass
    def Swim():
        pass
