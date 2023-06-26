# Contrua um algoritmo que calcule a quantidade de latas de tintas necessárias e o custo para pintar tanques cilíndricos de combustível, 
# em que são fornecidos a altura e o raio da base. 

# Considere que:
# a lata de tinta custa R$ 50,00 e que cada lata contém 5 litros de tinta.
# Cada litro de tinta pinta 3 metros quadrados.
# Dados de entrada: altura (H) e raio da base (R)
# Dados de saída: custo (C) e quantidade de latas (QTDE)

# Importando a biblioteca math
import math

# Definindo a função para calcular a área do cilindro
def area_cilindro(raio, altura):
    area = 2 * math.pi * raio * altura
    return area

# Definindo a função para calcular a quantidade de latas
def qtde_latas(area):
    qtde = area / 15
    return qtde

# Definindo a função para calcular o custo
def custo_latas(qtde):
    custo = qtde * 50
    return custo

# Definindo a função para imprimir os resultados
def imprimir_resultados(area, qtde, custo):
    print(f'A área do cilindro é: {area:.2f} m²')
    print(f'A quantidade de latas necessárias é: {qtde:.2f} latas')
    print(f'O custo total é: R$ {custo:.2f}')

# Função principal
def main():
    # Entrada de dados
    raio = float(input('Digite o raio da base do cilindro: '))
    altura = float(input('Digite a altura do cilindro: '))

    # Processamento
    area = area_cilindro(raio, altura)
    qtde = qtde_latas(area)
    custo = custo_latas(qtde)

    # Saída de dados
    imprimir_resultados(area, qtde, custo)

# Chamando a função principal
main()

# Fim do programa