import json


# Fájl beolvasása
with open('index.json', 'r', encoding="utf-8") as f:
    kartyak = json.load(f)
e = 4
# JSON adatok feldolgozása
szoveg = kartyak["a"][e-1]


# Kártya adatainak felhasználása
print('\n')
print(f"Pálya: {szoveg} \n")


#Tanári json használata:
#import json
#
#with open('kaland.json', 'r', encoding='utf-8') as f:
#   data = json.load(f)
#
#print(data['bevezeto'])
#
#k = 0
#
#szoveg = data['kartyak'][k]['szoveg']
#akcio = data['kartyak'][k]['akcio']
#if akcio['tipus'] == 'ugras':
#   print(szoveg)