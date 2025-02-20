from abc import ABC,abstractclassmethod
class Person(ABC):
    @abstractclassmethod
    def speak(self):
        pass


class Engilish(Person):
    def speak(self):
        print("i cen speak  UZBEK")






class Uzbek(Person):
    def __init__(self,name,age):
        print("mani ismim NOdir,yoshim 17da")








u = Uzbek()

