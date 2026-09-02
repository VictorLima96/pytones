maior = 0

for i in range(1, 7):
	while True:
		try:
			num = int(input(f"Digite o {i}º número inteiro positivo: "))
		except ValueError:
			print("Erro! Digite um número inteiro.")
			continue
		if num > 0:
			break
		print("Erro! O número precisa ser positivo, caba.")
	if num > maior:
		maior = num

print(f"\nO maior número lido foi: {maior}")