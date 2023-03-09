import random
import json

dobas = [random.randint(1,6) for _ in range(2)]
dobas2 = random.randint(1,6)
dobas3 = random.randint(1,6)

sajathp = sum(dobas) + 12
sajatdmg = dobas2 + 6
sajatluckmax = dobas3 + 6

class Jatekos:
    def __init__(self, hp=sajathp, dmg=sajatdmg, maxluck=sajatluckmax):
        self.hp = sajathp
        self.dmg = sajatdmg
        self.maxluck = sajatluckmax

    def __repr__(self):
        return f'Ez te vagy. Életerőd: {self.hp}, Támadóerőd: {self.dmg}, Szerencséd: {self.maxluck} ({self.maxluck})'

class Tolvaj:
    def __init__(self, hp = 6, dmg = 7):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Tolvaj ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class Oriaspok:
    def __init__(self, hp = 5, dmg = 9):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Óriáspók ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class Torpe:
    def __init__(self, hp = 5, dmg = 8):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Törpe ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class Fenyimadok:
    def __init__(self, hp = 11, dmg = 9):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Fényimádók ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class Iszapsarkany:
    def __init__(self, hp = 6, dmg = 10):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Iszapsárkány ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class ElsoOrk:
    def __init__(self, hp = 6, dmg = 5):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Első Ork ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class MasodikOrk:
    def __init__(self, hp = 5, dmg = 6):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Második Ork ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class Xlaia:
    def __init__(self, hp = 7, dmg = 8):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Xlaia ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class ElsoDenever:
    def __init__(self, hp = 7, dmg = 5):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Első Denevér ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class MasodikDenever:
    def __init__(self, hp = 6, dmg = 6):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Második Denevér ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class ElsoSundiszno:
    def __init__(self, hp = 5, dmg = 7):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Első Sündisznó ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class MasodikSundiszno:
    def __init__(self, hp = 5, dmg = 8):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Második Sündisznó ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class Hobgoblin:
    def __init__(self, hp = 8, dmg = 7):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Hobgoblin ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class Galon:
    def __init__(self, hp = 8, dmg = 12):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Galon ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class ElsoIszapsarkany:
    def __init__(self, hp = 5, dmg = 9):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Első Iszapsárkány ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class MasodikIszapsarkany:
    def __init__(self, hp = 6, dmg = 10):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Második Iszapsárkány ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

class Iszapsarkany2:
    def __init__(self, hp = 5, dmg = 9):
        self.hp = hp
        self.dmg = dmg

    def __repr__(self):
        return f'Iszapsárkány ellenfél. Életereje: {self.hp}, TÁmadóereje: {self.dmg}'

def Szerencseproba():
    sajatluck = (sajatluckmax)
    kérdés = input('próbára teszed a szerencsédet?(igen/nem)')
    if kérdés == 'igen':
        luckdice = [random.randint(1,6) for _ in range(2)]
        siker = False
        if sum(luckdice) < sajatluck:
            siker = True
            sajatluck -= 1
            print(f'Szerencséd volt, így a következmények eredményeit csökkentetted. Új szerencse értéked: {sajatluck} ({sajatluckmax})')
        else:
            siker = False
            sajatluck -= 1
            print(f"Nem volt szerencséd, így következményeket vállalnod kell. Új szerencse értéked: {sajatluck} ({sajatluckmax})")
    
    elif kérdés == 'nem':
        print('Nem tetted próbára a szerencsédet.')

Jatekos()
Szerencseproba()