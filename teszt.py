import random
dobas = [random.randint(1,6) for _ in range(2)]
dobas2 = random.randint(1,6)
dobas3 = random.randint(1,6)
sajathp = sum(dobas) + 12
sajatdmg = dobas2 + 6
sajatluckmax = dobas3 + 6
class Ellenfel:
    def __init__ (self, Thp, Tdmg):
        self.Thp = Thp
        self.Tdmg = Tdmg
        
class Fohos:
    def __init__ (self, sajathp, sajatdmg, sajatluckmax):
        self.sajathp = sajathp
        self.sajatdmg = sajatdmg
        self.sajatluck = sajatluckmax

    def getEletero(self):
        return self.sajathp

    def getHarciero(self):
        return self.sajatdmg
    
    def getLuck(self):
        return self.sajatluckmax

    
    def sebzodik(self, harciero):
        self.sajathp -= harciero

    def harcol(self, harcos):
        self.sebzodik(harcos.getHarciero())
        harcos.sebzodik(self.getHarciero())
        if self.getEletero() < 1 or harcos.getEletero() < 1:
            return True
        return False

    
    def __repr__(self):
        return f'<object.harcos: HE:{self.getHarciero()}, EE:{self.getEletero()} SZ:{self.getLuck()})>'
    
    



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


h1 = Fohos(200, 30, 1)
h2 = Ellenfel(120, 40, 1)

kor = 1
while not h1.harcol(h2):
  print(f'{kor}. kör:')
  print(h1)
  print(h2)
  kor+=1

if h1.getEletero()<1 and h2.getEletero()<1:
  print('Mindketten veszítettel!')
elif h1.getEletero() < 1:
  print(f'Nyertes: {h2}')
else:
  print(f'Nyertes: {h2}')

#def vane(b,e):
#    for i in (b):
#        if e == i:
#            return True
#        else:
#            return False