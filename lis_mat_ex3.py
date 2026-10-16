from random import randint, random

inteiros = [randint(0, 100) for _ in range(10)]
reais = [random() * 10 for _ in range(5)]
strings = ["Python", "Desenvolvimento", "Código", "Automação", "Dados", "Algoritmo", "Tecnologia"]

completa = [inteiros, reais, strings]

del inteiros
del reais
del strings

for lista in completa:
    for elemento in lista:
        print(elemento)
