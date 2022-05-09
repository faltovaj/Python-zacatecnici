"""
Prevody jednotek: Prevedte delku zadanou v mm na cm, dm nebo m (podle prani uzivatele)
Vstup:
- delka v mm
- jednotky, na ktere chceme prevadet (cm, dm, m)
Vystup:
- delka v pozadovanych jednotkach
"""
print('====== Prevody jednotek delky =========')
# Prvni vstup: pretypovani na realne cislo (float)
delka = float(input("Zadejte delku v mm "))
# Druhy vstup ja retezec - nemusi pretypovavat
jednotka = input("Na jakou jednotku chcete prevadet? ")

# Prevody a vypis
if jednotka=="cm":
    print(f"Delka v cm je {delka/10}")
elif jednotka=='dm':
    print(f"Delka v dm je {delka/100}")
elif jednotka=='m':
    print(f"Delka v m je {delka/1000}")
else:
    print("Zadali jste spatne jednotky. Prevod neprobehne.")