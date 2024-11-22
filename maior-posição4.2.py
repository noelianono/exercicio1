def main():
    valores = []

    for i in range(100):
        valores.append(int(input()))

    # Encontra o maior valor e sua posição (index + 1 para ser 1 baseado)
    maior_valor = max(valores)
    posiçao = valores.index(maior_valor) + 1  # Para ajustar a posição para começar de 1

    # Exibe o maior valor e sua posição
    print(f'\n\n{maior_valor} Na posição',end=' ')
    print(posiçao)
main()
