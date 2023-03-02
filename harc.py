import random
import json

dobas = [random.randint(1,6) for _ in range(2)]
dobas2 = random.randint(1,6)
dobas3 = random.randint(1,6)

sajathp = sum(dobas) + 12
sajatdmg = dobas2 + 6
sajatluckmax = dobas3 + 6

def Tolvaj():
    hp = 6
    dmg = 7
    return f'Tolvaj ellenfél; Életereje: {hp}, Ügyessége {dmg}'

def Oriaspok():
    hp = 5
    dmg = 9
    return f'Óriáspók ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def Torpe():
    hp = 5
    dmg = 8
    return f'Törpe ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def Fenyimadok():
    hp = 11
    dmg = 9
    return f'Fényimádók ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def Iszapsarkany1():
    hp = 6
    dmg = 10
    return f'Iszapsárkány ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def ElsoOrk():
    hp = 6
    dmg = 5
    return f'Első Ork ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def MasodikOrk():
    hp = 5
    dmg = 6
    return f'Második Ork ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def Xlaia():
    hp = 7
    dmg = 8
    return f'Xlaia ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def ElsoDenever():
    hp = 7
    dmg = 5
    return f'Első Denevér ellenfél; Életereje: {hp}, Ügyesség: {dmg}'

def MasodikDenever():
    hp = 6
    dmg = 6
    return f'Második Denevér ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def ElsoSundiszno():
    hp = 5
    dmg = 7
    return f'Első Sündisznó ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def MasodikSundiszno():
    hp = 5
    dmg = 8
    return f'Második Sündisznó ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def Hobgoblin():
    hp = 8
    dmg = 7
    return f'Hobgoblin ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def Galon():
    hp = 8
    dmg = 12
    return f'Galon ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def ElsoIszapsarkany():
    hp = 5
    dmg = 9
    return f'Első Iszapsárkány ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def MasodikIszapsarkany():
    hp = 6
    dmg = 10
    return f'Második Iszapsárkány ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

def Iszapsarkany2():
    hp = 5
    dmg = 9
    return f'Első Iszapsárkány ellenfél; Életereje: {hp}, Ügyessége: {dmg}'

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