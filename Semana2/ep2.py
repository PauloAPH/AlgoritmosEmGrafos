# Descrição
# Faça um programa que faz a leitura de um grafo e imprime as distâncias obtidas a partir de um vértice s, de acordo com uma visita BFS (ou busca em largura).

# Entrada
# Recebe n, m e s: n é o total de vértices, m o total de arcos e s o vértice inicial.
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime as distâncias obtidas a partir de s, pela busca BFS.

# Exemplo

# Entrada:
# 6 14 1
# 0 1
# 0 4
# 1 0
# 1 2
# 1 4
# 2 1
# 2 3
# 3 2
# 3 4
# 3 5
# 4 0
# 4 1
# 4 3
# 5 3

# Saída: 
# 1: 1 0 1 2 1 3 
 

# Insercao no fim.
def insere (Q, x):
  Q.append (x)

# Remove do inicio.
# Assume fila nao vazia.
def remove (Q):
  return Q.pop (0)

# Devolve verdadeiro se fila vazia.
def vazio (Q):
  return len (Q) == 0


n, m, s = (int(tmp) for tmp in input().split(" "))
adj = [[] for _ in range(n)]
for k in range(m):
  i, j = (int(tmp) for tmp in input().split(" "))
  adj[i].append(j)

# algoritmo BFS

# inicializacao
d = [0] * n
for v in range (n):
  d[v] = -1
d[s] = 0

Q = [s]

while not vazio (Q):
  u = remove (Q)
  for v in adj[u]:
    if d[v] == -1:
      d[v] = d[u] + 1
      insere (Q, v)

texto = str(s) + ": "
for j in d:
    texto += "%d " % j
print (texto)