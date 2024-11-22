def calculo():
    div = 0
    y = int(input('y: '))
    x = int(input('x: '))
    div = y % x
    if div == 0:
        print("divisao impossivel")
    else:
        print(f"{div:.1f}")

    

calculo()