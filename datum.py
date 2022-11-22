# Zjistete dnesni datum a cas s pouzitim module datetime
from datetime import date, datetime
datum = date.today()
print('Dnesni datum:', datum)
print(f'Cas {datetime.now().hour} h {datetime.now().minute} min')

# Kolik dni do 24.12.2022?
vanoce = date(2022,12,24)
delta = vanoce - date.today()
print('Pocet dni do Vanoc: ', delta.days)

#Help
#help(datetime)