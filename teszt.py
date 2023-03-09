import random


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

    def GetTsebzes(self):
        return self.Tdmg + DoboKocka()

    def GetTéleterő(self):
        return self.Thp + DoboKocka()



        
class Fohos:
    def __init__ (self, sajathp, sajatdmg, sajatluckmax):
        self.sajathp = sajathp 
        self.sajatdmg = sajatdmg
        self.sajatluck = sajatluckmax

    def GetTsebzes(self):
        return self.sajatdmg + DoboKocka()

    def GetTéleterő(self):
        return self.sajathp + DoboKocka()

    def GetTéleterő(self):
        return self.sajatluck

    



