import random

numero = random.randint(1, 10)

palpite = int(input("Adivinhe o número entre 1 e 10: "))

while palpite != numero:
    print("Errou! Tente novamente.")
    palpite = int(input("Adivinhe o número entre 1 e 10: "))

print("Parabéns! Você acertou!")
