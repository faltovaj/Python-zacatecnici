"""
Prevody jednotek: Prevedte delku zadanou v mm na cm, dm nebo m (podle prani uzivatele)
Vstup:
- delka v m
- jednotky, na ktere chceme prevadet (mm, cm, dm)
Vystup:
- delka v pozadovanych jednotkach
"""
print('====== Prevody jednotek delky =========')
# Prvni vstup: pretypovani na realne cislo (float)
delka = float(input("Zadejte delku v m "))
# Druhy vstup je retezec - nemusime pretypovavat
jednotka = input("Na jakou jednotku chcete prevadet? ")

# Prevody a vypis
if jednotka=="mm":
    print(f"Delka v mm je {delka*1000}")
elif jednotka=='cm':
    print(f"Delka v cm je {delka*100}")
elif jednotka=='dm':
    print(f"Delka v dm je {delka*10}")
else:
    print("Zadali jste spatne jednotky. Prevod neprobehne.")