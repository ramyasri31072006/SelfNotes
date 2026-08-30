from Bird import Bird
from lowflyingbird import lowflyingbird
from flyer import Flyer
class Dove(Bird):
    def __init__(self,name,age,color):
          super().__init__(name,age,color)
          #self._lowflyingbird = lowflyingbird()
          self._flyer =lowflyingbird()
      
    def fly(self):
       # self._lowflyingbird.lowfly()
        self._flyer.fly_altitude()
        print("Dove is flying")