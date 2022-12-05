"""
Uzivatel zada svoje jmeno a prijmeni, program vrati jeho inicialy
"""
# Nacteme jmeno
jmeno = input('Zadejte svoje jmeno: ')
# Jmeno rozdeli podle mezer na jmeno a prijmeni
# Ted bude v promenne jmeno ulozen seznam s prvky jmeno a prijmeni
jmeno = jmeno.split()
print(jmeno)

# Projdeme jednotlive slozky seznamu a vypiseme jejich prvni pismeno (index 0)
for p in jmeno:
    #print s parametrem end='.' neukonci vypis novym radkem, ale pripise za vypis .
    print(p[0], end='.')
# print pro odradkovani
print()

# Druhy zpusob: vezmu prvni polozku seznamu (jmeno[0]) a vypisi z ni prvni pismeno (jmeno[0][0])
# Obdodne pro druhou polozku
print(f'{jmeno[0][0]}.{jmeno[1][0]}.')
