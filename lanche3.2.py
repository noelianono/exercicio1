def calcular():
    total = 0
    opção = {
    1: 4.00,   # Cachorro Quente
    2: 4.50,   # X-Salada
    3: 5.00,   # X-Bacon
    4: 2.00,   # Torrada Simples
    5: 1.50    # Refrigerante
    }
    codigo = int(input("código do item: "))
    quantidade = int(input("quantidade do item: "))
    if codigo in opção:
        total = opção[codigo] * quantidade
        print(f"Total: R$ {total:.2f}")
    else:
        print("Código inválido.")

calcular()