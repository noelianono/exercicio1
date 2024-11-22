def calculo():
    cont = soma = val = total = 0
    for c in range(0, 4):
        y = int(input('Y: '))
        x = int(input('X: '))
        
        if y % 2 == 1: 
            soma += y
            cont += 1
        if x % 2 == 1:  
            val += x
            cont += 1
        total = soma + val
    print(f"Resultado: Y {soma} resultado X {val} Total {total} ")

calculo()