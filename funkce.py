"""
Funkce: zprehlednuji kod, daji se zavolat z jineho makra (priklad test.py)
"""

# Funkce, ktera posoudi, zda je cislo sude ci liche
# Tato funkce ma jeden parameter (se jmenem cislo)
# Funkce muze vracet hodnotu - klicove slovo return
# (pokud return vynechate, kod stale bude pracovat, jen funkce nebude nic vracet)
# V nasem pripade vraci True, pokud je cislo sude a False, pokud je liche
def sude(cislo):
    # Posouzeni sudosti
    if (cislo%2 == 0):
        print('Cislo', cislo, 'je sude')
        return True
    else:
        print('Cislo', cislo, 'je liche')
        return False

# Kod pod radkem 16 probehne pouze pri spusteni tohoto makra
# neprobehne pri importovani funkce do jineho souboru
if __name__ == '__main__':
    # Volani funkce
    sude(10)
    sude(11)
    # V tomto pripade jsem si do promenne jeSude nacetla hodnotu, kterou funkce sude vraci
    jeSude = sude(20)
