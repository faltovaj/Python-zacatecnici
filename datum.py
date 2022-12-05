"""
Ukazka knihovny datetime - datum a cas
"""

# Zjistete dnesni datum a cas s pouzitim module datetime
from datetime import date, datetime
datum = date.today()
print('Dnesni datum:', datum)
print(f'Cas {datetime.now().hour} h {datetime.now().minute} min')

# Kolik dni zbyva do 24.12.2022?
# Vytvorim si datum pro Stedry den
vanoce = date(2022,12,24)
# odectu od Stedreho dne dnesni datum
delta = vanoce - date.today()
# Zjistim pocet dni
print('Pocet dni do Vanoc: ', delta.days)

# Vice najdete napr. v helpu
#help(datetime)
