def dia_por_numero_if(n):
    if n == 1:
        return "Domingo"
    elif n == 2:
        return "Segunda"
    elif n == 3:
        return "Terça"
    elif n == 4:
        return "Quarta"
    elif n == 5:
        return "Quinta"
    elif n == 6:
        return "Sexta"
    elif n == 7:
        return "Sábado"
    else:
        return "Número inválido"


def dia_por_numero_mapa(n):
    if n < 1:
        return "Número inválido"
    dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
    return dias[(n - 1) % 7]


if __name__ == "__main__":
    s = input("Digite um número (1-7): ")
    try:
        n = int(s)
    except ValueError:
        print("Entrada inválida: digite um número inteiro.")
    else:
        print(dia_por_numero_if(n))