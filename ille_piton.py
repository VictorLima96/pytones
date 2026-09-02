def obter_procedencia(code):

    if code == 1:
        return "Sul"
    elif code == 2:
        return "Norte"
    elif code == 3:
            return "Leste"
    elif code == 4:
            return "Oeste"
    elif code in (5, 6):
            return "Nordeste"
    elif code in (7, 8, 9):
            return "Sudeste"
    elif code in range(10, 21):
            return "Centro-Oeste"
    elif code in range(25, 31):
            return "Nordeste 2"
    else:
        return "Importado"

def principal():
    try:
        preco = float(input("Digite o preço do produto: "))
        if preco < 0:
            print("Preço não pode ser negativado.")
            return

        code = int(input("Digite o código de origem: ").strip())
        procedencia = obter_procedencia(code)
        print(f"Preço: R$ {preco:.2f} | Procedência: {procedencia}")

    except ValueError:
        print("Entrada inválida. Digite valores numéricos corretamente.")

if __name__ == "__main__":
    principal()