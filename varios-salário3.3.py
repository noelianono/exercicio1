def reajuste():
    mult = tot = aumento = 0
    salário = float(input('Salário '))
    aumento = int(input('Procentegem de '))
    mult = salário * aumento / 100
    tot = mult + salário
    print(f'A porcentagem é de {aumento} aumento de {mult:.2f} salário atual {tot:.2f} ') 
    if salário >= 0 and salário < 400.00:
        aumento = 15
    elif salário >= 400.01 and salário < 800.00:
        aumento = 12
    elif salário >= 800.01 and salário < 1200.00:
        aumento = 10
    elif salário >= 1200.01 and salário < 2000.00:
        aumento = 7
    else:
        aumento = 4
    

    
reajuste()
