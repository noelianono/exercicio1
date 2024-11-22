def calculo():
    X = int(input(" X: "))
    Y = int(input("Y: "))
    inicio = min(X, Y)
    fim = max(X, Y)
    for num in range(inicio + 1, fim):
        if num % 5 == 2 or num % 5 == 3:
            print(num)
calculo()