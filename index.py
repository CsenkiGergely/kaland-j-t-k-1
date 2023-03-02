import json


# Fájl beolvasása
with open('index.json', 'r', encoding="utf-8") as f:
    kartyak = json.load(f)
e = 1
# JSON adatok feldolgozása
szoveg = kartyak["a"][e-1]


# Kártya adatainak felhasználása
print('\n')
print(f"Pálya: {szoveg} \n")

with open('index.json', 'r', encoding="utf-8") as f:
    kartyak = json.load(f)
e = 1
szoveg = kartyak["a"][e-1]


print('\n')
print(f"Pálya: {szoveg} \n")



