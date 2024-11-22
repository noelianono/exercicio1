def main():
    salário = float(input('valor salário '))
    porcen = int(input('porcentagem de aumento '))
    reajuste = salário * porcen / 100
    adic = reajuste + salário
    print(f'\n\nantgigo {salário:.2f}\n valor do reajuste {reajuste:.2f}\n novo salário {adic:.2f}') 

main()
