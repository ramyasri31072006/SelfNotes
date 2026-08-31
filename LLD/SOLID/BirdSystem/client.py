from Bird import Bird
from pigeon import Pigeon
from penguin import penguin
from dove import Dove
from lowflyingbird import lowflyingbird
from highflyingbird import HighflyingBird
from flyer import Flyer
def make_bird_fly(bird:Bird):
   bird.fly()

def main():
  #b1 = Bird("Pigeon",3,"Indigo")
  #b1.fly()
  # b1 = Pigeon("Pigeon",3,"Indigo")
  # make_bird_fly(b1)
  # b2 = penguin("penguin",4,"Whilte")
  # make_bird_fly(b2)
  b3 = Dove("Dove",5,"black")
  make_bird_fly(b3)

if(__name__ == "__main__"):
    main()