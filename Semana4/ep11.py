# Descrição
# Faça um programa que faz a leitura de um grafo ponderado.
# O programa deve imprimir na tela a matriz de distâncias e a matriz "PI" dos caminhos mínimos obtidos pelo algoritmo de Floyd-Warshall.

# Entrada
# Recebe n e m; n é o total de vértices e m o total de arcos.
# A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime as distâncias e os caminhos mínimos obtidos pelo algoritmo de Floyd-Warshall.

# Exemplo
# Entrada:

# 5 9
# 0 1 3
# 0 2 8
# 0 4 -4
# 1 3 1
# 1 4 7
# 2 1 4
# 3 0 2
# 3 2 -5
# 4 3 6

# Saída: 
# [[ 0  1 -3  2 -4]
#  [ 3  0 -4  1 -1]
#  [ 7  4  0  5  3]
#  [ 2 -1 -5  0 -2]
#  [ 8  5  1  6  0]]
# [[-1  2  3  4  0]
#  [ 3 -1  3  1  0]
#  [ 3  2 -1  1  0]
#  [ 3  2  3 -1  0]
#  [ 3  2  3  4 -1]]
 
import numpy as np
 
def imprime_matrix(matrizAdj, n):
    for i in range (0, n):
        saida = ""
        for j in range (0, n):
            if matrizAdj[i][j] >= INF:
                saida += "INF "
            else:
                saida += "%d " % matrizAdj[i][j]
        print (saida)

n, m = (int(tmp) for tmp in input().split(" "))
INF = 999999
matrizAdj = [[INF for col in range(n)] for row in range(n)]
for i in range (0, n):
  matrizAdj[i][i] = 0
for i in range (0, m):
  i, j, peso = (int(tmp) for tmp in input().split(" "))
  matrizAdj[i][j] = peso

d = [[row[:] for row in matrizAdj],[row[:] for row in matrizAdj]]
pai = [[row[:] for row in matrizAdj],[row[:] for row in matrizAdj]]
for i in range (0, n):
  for j in range (0, n):
    if i == j:
        pai[0][i][j] = -1
        pai[1][i][j] = -1
    elif matrizAdj[i][j] < INF:
        pai[0][i][j] = i
        pai[1][i][j] = i

print(np.copy(pai[0]))

for k in range(n):
   for i in range(n):
      for j in range(n):
        d[k%2][i][j] = d[(k-1)%2][i][j]
        pai[k%2][i][j] = pai[(k-1)%2][i][j]
        if d[(k-1) % 2][i][k-1] + d[(k-1) %2 ][k-1][j] < d[(k-1) % 2][i][j]:
            d[k % 2][i][j] = d[(k-1) % 2][i][k-1] + d[(k-1) % 2][k-1][j]
            pai[k % 2][i][j] = pai[(k-1) % 2][k-1][j]

print(np.copy(d[k%2]))
print(np.copy(pai[k%2]))

