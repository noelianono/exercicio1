def lista():
    soma = t = 0
    adiciona = dict()
    ab = list()
    for c in range(0, 2):
        adiciona['peças'] = int(input('peças '))
        adiciona['cod'] = int(input('cod '))
        adiciona['valor'] = float(input('valores '))
        ab.append(adiciona.copy())
        soma =  adiciona['valor'] * 5.30
    
             

        print(f'\n\n{adiciona['peças']} {soma:25.2f}\n {adiciona['cod']}\n {adiciona['valor']}')
                
            
lista()
