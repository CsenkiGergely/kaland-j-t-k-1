import json
import random


# Fájl beolvasása
with open('index.json', 'r', encoding="utf-8") as f:
    kartyak = json.load(f)
e = 1
# JSON adatok feldolgozása
szoveg = kartyak["a"][e-1]


# Kártya adatainak felhasználása
print('\n')
print(f"Pálya: {szoveg} \n")

def DoboKocka():
        dobas = random.randint(1,6)
        return dobas

sajathp = DoboKocka() + DoboKocka() + 6
sajatdmg = DoboKocka() + 6
sajatluckmax = DoboKocka() + 6

print(f'HP= {sajathp}, DMG= {sajatdmg}, Luck= {sajatluckmax}')
with open('index.json', 'r', encoding="utf-8") as f:
        kartyak = json.load(f)
        e = 2
        szoveg = kartyak["a"][e-1]
        print('\n')
        print(f"Pálya: {szoveg} \n")

while True:
    b = input("ha menni akarsz tovább írd be hogy (41):")
    if b == '41':

        with open('index.json', 'r', encoding="utf-8") as f:
            kartyak = json.load(f)
            e = 42
            szoveg = kartyak["a"][e-1]
            print('\n')
            print(f"Pálya: {szoveg} \n")
            break

    else:
        print('hibás bemenet')


















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

while True:
    b = input("ha menni akarsz tovább írd be hogy (85):")
    if b == '85':

        with open('index.json', 'r', encoding="utf-8") as f:
            kartyak = json.load(f)
            e = 86
            szoveg = kartyak["a"][e-1]
            print('\n')
            print(f"Pálya: {szoveg} \n")
            break

    else:
        print('hibás bemenet')

while True:
    b = input("ha menni akarsz tovább írd be hogy (108 vagy 147):")
    if b == '108':

        with open('index.json', 'r', encoding="utf-8") as f:
            kartyak = json.load(f)
            e = 109
            szoveg = kartyak["a"][e-1]
            print('\n')
            print(f"Pálya: {szoveg} \n")
            break

    elif b == '147':

        with open('index.json', 'r', encoding="utf-8") as f:
            kartyak = json.load(f)
            e = 148
            szoveg = kartyak["a"][e-1]
            print('\n')
            print(f"Pálya: {szoveg} \n")
            break

    else:
        print('hibás bemenet')
A = True
if b == 147:
    while A == False:
        b = input("ha menni akarsz tovább írd be hogy (147):")
    if b == '147':
        with open('index.json', 'r', encoding="utf-8") as f:
            kartyak = json.load(f)
            e = 148
            szoveg = kartyak["a"][e-1]
            print('\n')
            print(f"Pálya: {szoveg} \n")
            A == False 

    else:
        print('hibás bemenet')

else:
    while  A == False:
        b = input("ha menni akarsz tovább írd be hogy (108):")
    if b == '108':
        with open('index.json', 'r', encoding="utf-8") as f:
            kartyak = json.load(f)
            e = 109
            szoveg = kartyak["a"][e-1]
            print('\n')
            print(f"Pálya: {szoveg} \n")
            A == False 
            

    else:
        print('hibás bemenet')


   