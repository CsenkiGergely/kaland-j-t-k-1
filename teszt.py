import random
dobas = [random.randint(1,6) for _ in range(2)]
dobas2 = random.randint(1,6)
dobas3 = random.randint(1,6)


def DoboKocka():
        dobas = random.randint(1,6)
        return dobas



sajathp = DoboKocka() + DoboKocka() + 6
sajatdmg = DoboKocka() + 6
sajatluckmax = DoboKocka() + 6



class Ellenfel:
    def __init__ (self, Tdmg, Thp = 6):
        self.Thp = Thp
        self.Tdmg = Tdmg


        
class Fohos:
    def __init__ (self, sajathp, sajatdmg, sajatluckmax):
        self.sajathp = sajathp 
        self.sajatdmg = sajatdmg
        self.sajatluck = sajatluckmax



