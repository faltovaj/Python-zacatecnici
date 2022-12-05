"""
Dalsi priklad na zelvi grafiku
Vykresleni spiraly s vyuzitim modulu turtle
V prubehu kresleni se meni barvy s vyuzitim modulu random
"""
# Nacteme moduly turtle a random
import turtle
import random

# t je objekt typu Turtle (zelva)
t = turtle.Turtle()
# Kurzor se bude vykreslovat jako zelva
t.shape('turtle')

barvy = ['red','green','blue','cyan','black','brown','yellow']
uhel = 30
for i in range(100):
    # Vybereme nahodne barvu, kterou budeme kreslit
    t.pencolor(random.choice(barvy))
    # pohyb dopredu o zvetsujici se cislo
    t.forward(2 + i/4)
    # otoceni po smeru hodinovych rucicek o zmensujici se uhel
    t.right(uhel - i/12)

# Ukonceni zelvy
turtle.done()