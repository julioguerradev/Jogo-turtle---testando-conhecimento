# 00 - Importando a biblioteca
from turtle import Turtle
# 01 - Definindo a turtle
t = Turtle()

# 02 - Definindo velocidade;
t.speed(1)  # Velocidade que varia de 1 a 10.


#_________________EXTRA________________#
#Instruções:
print('Instruções: \n Para que comece a jogar é importante que entenda que a quantidade de pixels que irá andar será definida no início e executada em cada comando posterior. \n poderá altera-los após responder se deseja continuar')

# 03 - Colocando em loop;
continuar = input('Deseja se movimentar ? \n ("N" = Não "S" = Sim): ')
while True:
    if continuar == 'S':
        # 04 - Definindo a distância;
        distancia = int(input('Digite quantos pixels deseja percorrer: '))

# 05 - Definindo rotação para a direita;
        direita = int(
            input('Quantos graus deseja se mover para a direita ? '))
# 06 - Executando o comando;
        t.right(direita)
        if direita > 0:
            t.forward(distancia)
        else:
            continue

# 07 - Definindo rotação para a esquerda;
        esquerda = int(
            input('Quantos graus deseja se mover para a esquerda ? '))
# 08 - Executando o comando;
        t.left(esquerda)
        if esquerda > 0:
            t.forward(distancia)
        else:
            continue

# 9 - Definindo movimentação para trás;
        back = int(input('Quantos pixels deseja se mover para trás ? '))
# 10 - Executando o comando;
        t.backward(back)

# 11 - Deseja continuar ?
        continuar = input('Deseja continuar?  \n ("N" = Não "S" = Sim): ')
    elif continuar == 'N':
        break
    else:
        print('Por favor digite uma das alternativas')
