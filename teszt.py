import random
dobas = [random.randint(1,6) for _ in range(2)]
dobas2 = random.randint(1,6)
dobas3 = random.randint(1,6)
sajathp = sum(dobas) + 12
sajatdmg = dobas2 + 6
sajatluckmax = dobas3 + 6
class Tolvaj:
    def __init__ (self, Thp, Tdmg):
        self.Thp = Thp = 6
        self.Tdmg = Tdmg = 7
        
class fohos:
    def __init__ (self, sajathp, sajatdmg, sajatluckmax):
        self.sajathp = sajathp = sum(dobas) + 12
        self.sajatdmg = sajatdmg = dobas2 + 6
        self.sajatluck = sajatluckmax = dobas3 + 6



class harc:
    def sebzés(self):
        dobas5 = random.randint(1,6)
        dobas6 = random.randint(1,6)
        ertek1 = dobas5 =+ sajatdmg
        ertek2 = dobas6 =+ self.Tdmg

        if ertek2 > ertek1:
            sajathp =- 2
            print(f'Meg sebeztek. A te életerőd {sajathp}')
        elif ertek2 < ertek1:
            self.Thp -= 2
            print(f'Megsebezted az ellenfelet. Az ellenfél életereje: {self.Thp}')
        else:
            print('Egyikőtök sem sebződött.')

    def halal(self):
        if sajathp <= 0:
            print("A játéknak itt vége ")

    def ellenfelhalal(self):
        if self.Thp <= 0:
            print("Meg ölted")