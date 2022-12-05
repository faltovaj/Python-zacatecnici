"""
Prenos argumentu (argparse)
Pozor: makro se pousti v prikazove radce (cmd):
python parametry.py 'jelen' 'retezce.py'
python parametry.py 'jelen' --verbosity 1 'retezce.py'
Pri zadani python parametry.py --help se zobrazi napoveda ohledne pozadovanych parametru
Poradi argumentu odpovida vypisu v napovode; nepovinne parametry jsou v napovode uvedeny v []
"""

# Nacteme modul argparse
import argparse
# Nacteme si makra ze soubor.py (vyzkousime analyzu souboru, kterou jsme si napsali)
from soubory import *
# Nacteme modul os.path kvuli kontrole vstupniho souboru (viz nize)
import os.path

# Zavolame ArgumentParser
parser = argparse.ArgumentParser()
# Nadefinujeme paramentry
parser.add_argument('text', help='text, ktery se vypise')     # povinny parametr
# --nazev -> nepovinny parametr
# Parametr muze ale nemusi byt uveden pri spusteni
parser.add_argument("--verbosity", help="regulace mnozstvi vypisu")
parser.add_argument("filename", help="jmeno souboru", type=str)    # nazev souboru k analyze
# Argumenty predame do promenne args (pres tu se k nim dostaneme)
args = parser.parse_args()

# Vypise, co jsme zadali do argumentu text
print(args.text)
# Pokud je zapnuty argument verbosity (nepovinny parametr), tak vypise vzkaz
if args.verbosity:
    print('Detailni vypisy zapnuty.')

# Projdeme soubor se jmenem zadanym argumentem
# Nejprve zkontolujeme, ze soubor existuje
if os.path.isfile(args.filename):
    pocty = projdiSoubor(args.filename)
    print(f'Pocet radku v souboru {args.filename} je {pocty[0]}')
    print(f'Pocet radku v souboru {args.filename} je {pocty[1]}')
else:
    print(f'Soubor {args.filename} neexistuje.')
