umrlec = [
     """
    |--------
    | 
    | 
    | 
    | 
    |
    """,
    """
    |--------
    |    |
    | 
    | 
    | 
    |
    """,
     """
    |--------
    |    |
    |    o    
    | 
    |   
    |
    """,
     """
    |--------
    |    |
    |    o    
    |    | 
    |      
    |         
    """,
     """
    |--------
    |    |
    |    o    
    |    |\   
    |     
    |
    """,
    """
    |--------
    |    |
    |    o    
    |   /|\   
    |     
    |
    """,
    """
    |--------
    |    |
    |    o    
    |   /|\   
    |   / 
    |
    """,
    """
    |--------
    |    |
    |    o    
    |   /|\   
    |   / \   
    |
    """
]

slovo = "sklenik"

hadame = ["_"] * len(slovo)
print(hadame)

pokus = 0
uhodnuto = 0
iu = 0

#for pokus in range(len(umrlec)):
while iu < len(umrlec):
    if uhodnuto<len(slovo):
        pismeno = input("Ktere pismeno? ")
        if pismeno in slovo:
            hadame[slovo.index(pismeno)] = pismeno
            print(hadame)
            uhodnuto += 1
        else:
            print(umrlec[iu])
            iu += 1
    else:
        break