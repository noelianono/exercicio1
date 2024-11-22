def main():
    media = cont = 0 
    for c in range(4):
        nota = float(input('valores '))
        cont += nota
    media  = cont / 4       
    print(f'{cont} Media é {media}')
    if media >= 5 and media < 7:
        print(f' Recuperação ')
    elif media < 5:
        print(f'Reprovado')
    elif media >= 7:
        print('Aprovado ')
    


main()
