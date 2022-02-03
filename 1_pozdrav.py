"""
1. program: pozdrav (hello world :))
- vypis na obrazku
- nacteni vstupu z klavesnice
"""
# Vypis na obrazovku
# print vypise jeden radek na obrazovku
print('Prvni test: Dobre rano')

# Poznamka: Uvozovky "" nebo '' Python nerozlisuje, muzeme pouzivat oboje
# Vypis promenne pozdrav
pozdrav = "Vitej na kurzu Python!"
print("======= Vypis =========")
print(pozdrav)

# Naciteni vstupu z klavesnice (input)
print("======= Vstup a vystup =========")
# Text v zavorce za input se vypise na obrazovku (pekne, pokud je posledni znak mezera)
jmeno = input("Zadejte sve jmeno ")
# Promenne typu retezec muzeme scitat
# +' ' - aby byla mezi pozdravem a jmenem vypsana mezera
print(pozdrav+' '+jmeno)