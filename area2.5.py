import math

# Função para calcular a distância entre dois pontos
def calcular_distancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

distancia = calcular_distancia(x1, y1, x2, y2)

print(f"\n\nA distância entre os pontos ({x1} {y1}) e ({x2} {y2}) é: {distancia:.4f}")
