def analyzujSoubor(filename):

    pocetRadku = 0
    pocetSlov = 0
    pocetZnaku = 0

    with open(filename, 'r') as f:
        for radek in f:
            slova = radek.split()
            if slova != []:
                pocetSlov += len(slova)
                pocetRadku += 1
                for p in slova:
                    pocetZnaku += len(p)

    print(pocetZnaku, pocetRadku, pocetSlov)
