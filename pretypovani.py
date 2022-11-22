"""
cislo = input('Zadejte cislo ')
print('Typ: ', type(cislo))    # retezec
cislo = int(cislo)
print('Po pretypovani', type(cislo))
"""
"""
logic = input('Zadejte radu cisel, oddelujte mezerou ')
print(type(logic))
logic = logic.split()
print(logic, type(logic))

for i in range(len(logic)):
    logic[i] = int(logic[i])
logic = list(map(int, logic))
print(logic)
"""
# Pretypovani polozek seznamu pomoci map
#logic = list(map(int, input('Zadejte ').split()))

# Pretypovani polozek seznamu pomoci list of comprehension
logic = input('Zadejte ').split()
logic = [int(p) for p in logic]     # logic = [int(p) for p in input('Zadejte ').split()]

print(logic)