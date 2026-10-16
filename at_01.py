dist = input("digite a distância percorrida: ")

wage = float(dist)

if wage < 200:
    novo_wage = wage * 0.50
    print(f"{novo_wage:.2f}")
else: 
    novo_wage = wage * 0.45
    print(f"{novo_wage:.2f}")





