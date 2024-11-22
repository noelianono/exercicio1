def main():
    a = int(input('num A '))
    b = int(input('num B '))
    c = int(input('num C '))
    d = int(input('num D '))
    # Verificação das condições
    if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")
main()
