intervalo1 = 0  # [0-25]

intervalo2 = 0  # [26-50]

intervalo3 = 0  # [51-75]

intervalo4 = 0  # [76-100]

while True:
    
    n = int(input("Digite um número: "))
    
    if n < 0:
     
        break
    
    if n >= 0 and n <= 25:
      
        intervalo1 += 1
    
    elif n >= 26 and n <= 50:
      
        intervalo2 += 1
    
    elif n >= 51 and n <= 75:
        
        intervalo3 += 1
    
    elif n >= 76 and n <= 100:
       
        intervalo4 += 1

print("Resultados:")

print("[0-25]:", intervalo1)

print("[26-50]:", intervalo2)

print("[51-75]:", intervalo3)

print("[76-100]:", intervalo4)
















