
def calcular_e_exibir():
    fun = int(input('salario '))
    h = int(input('horas '))
    n = int(input('Numero = '))
    s = fun / 30  
    d = s / 8
    e = d * h


    print(f"\n\n{n:>13}{'Numero = ':>26}{n:>2}\n")
    print(f"{s:14.2f}\n{e:14.2f}{'$':>18} {fun:2.2f}\n{d:14.2f}")
    




calcular_e_exibir()



