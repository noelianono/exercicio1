def main():
    num = float(input('numero '))
    if num >= 25 and num < 50:
        print(f'{num} Está entre 25 e 50')
    elif num < 25:
        print('Está entre 25 a 0')
    elif num >= 75 and num < 100:
        print('Você está entre 75 e 100')
    else:
        print('Está fora ')

main()
