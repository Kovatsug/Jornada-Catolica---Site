from classes import *

def menu():
    options=["1. Add Santo", "2. Add Oração", "3. Add Milagre", "4. add sacramento", "5. add catecismo", "6. add liturgia"]
    for i in options:
        print(i)
    op=int(input("Escolha:   "))

    if op==1 :
        name=input("nome")
        return Santo(nome=name)
