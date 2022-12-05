"""
Automat na mince: rozmeni bankovky na mince
Vstup: kolik chceme rozmenit
Vystup: kolik 50-ti, 20-ti, 10-ti, 5-ti, 2 a 1 korun
//, %
"""
# Do promenne castka si ulozim castku na rozdeleni
castka = int(input('Zadejte castku: '))
# Hodnotu si ulozim do promenne castkaNova
# Promenna castkaNova se bude v prubehu vypoctu menit
castkaNova = castka

# Celociselnym delenim 50-ti zjistim, kolik se vejde do castky 50-ti korun
pocet50 = castkaNova//50
# Zjistim, kolik mi po vyplaceni 50-ti korunami zbyde na rozmeneni
castkaNova = castkaNova%50
# Stejnym zpusobem pokracujeme i s ostatnimi mincemi
pocet20 = castkaNova//20
castkaNova = castkaNova%20
pocet10 = castkaNova//10
castkaNova = castkaNova%10
pocet5= castkaNova//5
castkaNova = castkaNova%5
pocet2 = castkaNova//2
pocet1 = castkaNova%2

# Zkontroluji si, ze jsem opravdu rozmenila celou castku
kontrola = 50*pocet50+20*pocet20+10*pocet10+5*pocet5+2*pocet2+pocet1
print(kontrola, castka)

print('Pocet 50', pocet50)
print('Pocet 20', pocet20)
print('Pocet 10', pocet10)
print('Pocet 5', pocet5)
print('Pocet 2', pocet2)
print('Pocet 1', pocet1)