"""
Program spocita obvod a obsah ctverce/obdelniku
Vstup: delka strany/stran
Vystup: obvod a obsah
"""

# Metoda input vraci retezec (string)
# Pro vypocet potrebujeme pretypovat retezec na cislo:
# - int() pro pretypovani na cela cisla
# - float() pro pretypovani na realne cislo
print("========= CTVEREC ===========")
strana = float(input("Zadejte velikost strany ctverce: "))
obvod = 4*strana
# Druha mocnina se zadava pomoci **2
obsah = strana**2
print('Obvod ctverce: ', obvod, 'obsah ctverce: ', obsah)

# Vyzkousejte si vypocet obsahu a obvodu obdelniku
print()
print("========= OBDELNIK ===========")
stranaA = float(input("Strana A: "))
stranaB = float(input("Strana B: "))
# print() vypise prazdny radek
print("Obvod obdelnika: ", (stranaA+stranaB)*2, " obsah: ", stranaA*stranaB)
# Vypis pomoci fstring (f''), dosadi se za promenne v {}
print(f'Obvod je {(stranaA+stranaB)*2}, obsah {stranaA*stranaB}')
