"""
Ukazka datoveho typu retezec (string)
- Operace s retezci
- Ukazka metod definovanych pro retezce
- Prochazeni retezce po znacich (for cyklus)
"""
print("======== Retezce a jejich delka ============")
slovo = "ahoj"
print("Testujeme slovo", slovo)
# len() - vraci pocet znaku v retezci
print("Delka slova (pocet znaku): ", len(slovo))
# pristup k jednotlivym znakum pres index v hranate zavorce
# Pozor: prvni index je 0, posledni index je len(slovo)-1
print("Jednotlive znaky: ", slovo[0], slovo[1], slovo[2], slovo[3])

print("======== Scitani a nasobeni retezcu ============")
# Retezce muzeme scitat a nasobit
soucet = slovo + " " + slovo
print("Soucet retezcu (s mezerou uprostred): ", soucet)
nasobek = slovo*3
print("Nasobeni retezcu cislem 3: ", nasobek)

print("========= Metody pro retezce ==========")
# Nekolik prikladu metod definovanych pro retezce
# lower()/upper() - cely retezec malymi/velkymi pismeny
slovoVelka = slovo.upper()
print("Slovo velkymi pismeny: ", slovoVelka)
# isdigit()/isalpha() - je retezec tvoren pouze cisly/pismeny?
# - nabyva hodnot True/False (typ boolean)
# Priklad - nacteme retezec z klavesnice a zjistime, jestli se jedna
# o cislo, pismena nebo jine znaky
#mujRetezec = input("Zadejte retezec ")
mujRetezec = '1234'
# Je retezec cislo?
if mujRetezec.isdigit():
    print("Zadali jste cislo.")
# Pokud neni cislo, je tvoren pouze pismeny?
elif mujRetezec.isalpha():
    print("Zadali jste pismena.")
# Pokud neplati ani jedno, vypiseme tento vzkaz
else:
    print("Zadali jste jine znaky nebo mix cislic a pismen.")

print("====== Prochazeni retezce (for) =======")
# Prochazeni znaku v retezci cyklem for
# Priklad: vypiste z retezce cislice
mixRetezec = 'do1bry5'
print(f"Zadali jste retezec {mixRetezec}")
# for-cyklus prochazi retezec znak po znaku
# Pri prvnim pruchodu bude promenna p rovna prvnimu znaku v retezci,
# pri druhem pruchodu druhemu znaku, ..., pri poslednim pruchodu bude rovna
# poslednimu znaku retezce
for p in mixRetezec:
    # Pokud je tento znak cislice, tak ji vypiseme
    if p.isdigit():
        print(f"Cislice {p}")
