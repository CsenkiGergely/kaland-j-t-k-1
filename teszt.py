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


    def harc(self):
        while self.sajathp > 0 or self.Thp > 0:
            DoboKocka() + self.Tdmg
            DoboKocka() + self.sajatdmg
            
            sebzes = 2
            if self.Tdmg < self.sajatdmg:
                self.Thp -= sebzes
            if self.Tdmg > self.sajatdmg:
                self.sajathp -= sebzes
            if self.Thp <= 0:
                print(f"nyertél a harcban.")
                print(f'A hp-d {self.sajathp}')
            if self.sajathp <= 0:
                print(f"nem nyertél, kalandod itt véget ért")
                print(f'A hp-d {self.Thp}')

            