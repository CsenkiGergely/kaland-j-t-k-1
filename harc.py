import random
import json

dobas = [random.randint(1,6) for _ in range(2)]
dobas2 = random.randint(1,6)
dobas3 = random.randint(1,6)

sajathp = sum(dobas) + 12
sajatdmg = dobas2 + 6
sajatluckmax = dobas3 + 6

def Tolvaj():
    Thp = 6
    Tdmg = 7
    return f'Tolvaj ellenfél; Életereje: {Thp}, Ügyessége {Tdmg}'

def Oriaspok():
    Ohp = 5
    Odmg = 9
    return f'Óriáspók ellenfél; Életereje: {Ohp}, Ügyessége: {Odmg}'

def Torpe():
    Thp = 5
    Tdmg = 8
    return f'Törpe ellenfél; Életereje: {Thp}, Ügyessége: {Tdmg}'

def Fenyimadok():
    Fhp = 11
    Fdmg = 9
    return f'Fényimádók ellenfél; Életereje: {Fhp}, Ügyessége: {Fdmg}'

def Iszapsarkany1():
    Ihp = 6
    Idmg = 10
    return f'Iszapsárkány ellenfél; Életereje: {Ihp}, Ügyessége: {Idmg}'

def ElsoOrk():
    EOhp = 6
    EOdmg = 5
    return f'Első Ork ellenfél; Életereje: {EOhp}, Ügyessége: {EOdmg}'

def MasodikOrk():
    MOhp = 5
    MOdmg = 6
    return f'Második Ork ellenfél; Életereje: {MOhp}, Ügyessége: {MOdmg}'

def Xlaia():
    Xhp = 7
    Xdmg = 8
    return f'Xlaia ellenfél; Életereje: {Xhp}, Ügyessége: {Xdmg}'

def ElsoDenever():
    EDhp = 7
    EDdmg = 5
    return f'Első Denevér ellenfél; Életereje: {EDhp}, Ügyesség: {EDdmg}'

def MasodikDenever():
    MDhp = 6
    MDdmg = 6
    return f'Második Denevér ellenfél; Életereje: {MDhp}, Ügyessége: {MDdmg}'

def ElsoSundiszno():
    EShp = 5
    Esdmg = 7
    return f'Első Sündisznó ellenfél; Életereje: {EShp}, Ügyessége: {Esdmg}'

def MasodikSundiszno():
    MShp = 5
    MSdmg = 8
    return f'Második Sündisznó ellenfél; Életereje: {MShp}, Ügyessége: {MSdmg}'

def Hobgoblin():
    Hhp = 8
    Hdmg = 7
    return f'Hobgoblin ellenfél; Életereje: {Hhp}, Ügyessége: {Hdmg}'

def Galon():
    Ghp = 8
    Gdmg = 12
    return f'Galon ellenfél; Életereje: {Ghp}, Ügyessége: {Gdmg}'

def ElsoIszapsarkany():
    EIhp = 5
    Eidmg = 9
    return f'Első Iszapsárkány ellenfél; Életereje: {EIhp}, Ügyessége: {Eidmg}'

def MasodikIszapsarkany():
    MIhp = 6
    MIdmg = 10
    return f'Második Iszapsárkány ellenfél; Életereje: {MIhp}, Ügyessége: {MIdmg}'

def Iszapsarkany2():
    EIhp = 5
    Eidmg = 9
    return f'Első Iszapsárkány ellenfél; Életereje: {EIhp}, Ügyessége: {Eidmg}'

print(*dobas)
print(dobas2)
print(dobas3)
print(f'Saját Életerő: {sajathp}')
print(f'Saját Ügyesség: {sajatdmg}')
print(f'Saját Szerencse: {sajatluckmax}')

sajatluck = (sajatluckmax)
érték = 1
kérdés = input('próbára teszed a szerencsédet?(igen/nem)')
if kérdés == 'igen':
    dobas4 = random.randint(1,6)
    szamok = [dobas4, sajatluck]
    eredmeny = sum(szamok)
    print(f'a te szerencséd {eredmeny}')
    print(f'a te maximális szerencséd {sajatluckmax}')
    
elif kérdés == 'nem':
    print('nem tetted próbára a szerencsédet')
    print(f'a te szerencséd {sajatluckmax}')



class Tolvaj:
    def __init__(self, Thp, Tdmg):
        self.Thp = Thp
        self.Tdmg = Tdmg

    def getEletero(self):
      return self.eletero

    def getHarciero(self):
      return self.harciero




class Tolvaj:
    def __init__ (self, Thp, Tdmg):
        self.Thp = Thp = 6
        self.Tdmg = Tdmg = 7


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

