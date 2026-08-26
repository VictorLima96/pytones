perg_wage = input("Digite o salário do funcionário: ")

wage = float(perg_wage)

if wage > 1250:
    novo_wage = wage * 1.10
    print(f"Novo salário: {novo_wage}")
else: 
    novo_wage = wage * 1.15
    print(f"Novo salário: {novo_wage}")