"""
Ukazka prace s textovymi soubory
- Nacteni textoveho souboru ke cteni/psani
- Kodovani
- Pruchod souboru po radcich
- Zapis do souboru
"""
# Otevreni souboru ke cteni/k zapisu: open
# POZOR: Ke kazdemu otevreni souboru musi byt na konci zavreni souboru (close)
# fin: soubor otevreny ke cteni - "r" jako read (cteni)
# parametr encoding neni povinny, automaticky se predpoklada stejne kodovani
# jako vyuziva Vas operacni system
fin = open("textovySoubor.txt", "r", encoding='utf8')
# fout: soubor otevreny k zapisu - "w" jako write (psani)
fout = open("souborVystup.txt", "w")

# Pokud neni soubor moc dlouhy, je mozne ho cely nacist do promenne typu retezec
# a pracovat s retezcem text
#text = fin.read()
#print(text)

# Casto se hodi procitat soubor po jednotlivych radcich - to si vyzkousime
# Ukol:
# 1. Zjistete, kolik je v souboru radku, slov a
# znaku (bez mezer, tabulatoru a koncu radku.
# 2. Do souboru fout zapiste pocet slov v odpovidajicim radku v souboru fin
# Zavedeme si promenne pro pocty radku, slov a znaku
# Na zacatku maji vsechny hodnotu 0
pocetRadku = 0
pocetSlov = 0
pocetZnaku = 0
# Prirazeni hodnot do vice promennych muzeme zapsat i takto:
# pocetRadku, pocetSlov, pocetZnaku = 0, 0, 0

# Cteni souboru po radcich pomoci for
for line in fin:
    # Pricteme jednicku do celkoveho poctu radku (pocetRadku)
    pocetRadku += 1    # ekvivalentni s pocetRadku = pocetRadku + 1
    # Rozdeleni do slov: prikaz split()
    # - rozdeli retezec podle bilych znaku (mezer/tabulatoru/koncu radku)
    # - vytvori seznam
    # - Priklad: "Dobry   den.".split() -> ["Dobry", "den"]
    #print(line.split())
    seznam = line.split()
    # Pocet slov na dane radce je pocet prvku seznamu
    # Pricteme pocet prvku (delku seznamu) do celkoveho poctu slov (pocetSlov)
    pocetSlov += len(seznam)
    # Zapiseme do souboru na samostatnou radku pocet slov
    # '\n' - znak konce radku
    fout.write(str(len(seznam))+'\n')
    # Cyklus pres jednotliva slova v seznamu pro urceni poctu znaku v radce
    for p in seznam:
        # Pricteme pocet znaku slov do celkoveho poctu znaku bez
        # bilych znaku (pocetZnaku)
        pocetZnaku += len(p)

print(f"Pocet radku je {pocetRadku}.")
print(f"Pocet slov je {pocetSlov}.")
print(f"Pocet znaku bez bilych znaku je {pocetZnaku}.")

# POZOR: Na konci musime soubor zavrit
print("Na konci nezapomeneme otevrene soubory zavrit!".upper())
fin.close()
fout.close()