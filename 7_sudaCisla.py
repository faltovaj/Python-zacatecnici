"""
Uloha na cykly:
Vypiste vsechna suda cisla do hodnoty N (vcetne)
vstup: N
posouzeni sudosti pomoci modulo (%)
Vyuzijte cyklus for i in range():
"""
N = int(input("Zadejte cislo "))
print(f"Suda cisla <={N}:")
# Budeme zkouset cisla 1, 2, ..., N -> to odpovida range(1,N+1)
for i in range(1,N+1):
    # Pokud je zbytek cisla i po deleni 2 roven 0, jde o sude cislo
    if i%2 == 0:
        print(i)