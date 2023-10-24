from random import randint

numero = randint(0,5)
print("")
print("Irei sortear um número entre 0 e 5.")
print("")
usuario = int(input("Chute esse número: "))

if usuario == numero:
    print("Acertou.")
else:
    print("Errou.")