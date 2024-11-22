def calcular_salario_comissao():
    v = soma = total = 0
    n = input("vendedor: ")
    s = float(input("salário fixo: "))
    for c in range(0,2):
        v = float(input("total de vendas no mês: "))
        soma = soma + v
        comissao = soma * 15 / 100
        total = s + comissao

    print(f"\n\n{n:>10}\n{s:>10}{'Total R$':>20} {total:>2}\n{soma:10.2f}\n ")

calcular_salario_comissao()
