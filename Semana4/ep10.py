# Descrição

# Faça um programa que faz a leitura de um grafo ponderado e um vértice inicial.
# O programa deve imprimir na tela os caminhos mínimos obtidos pelo algoritmo de Dijkstra.

# Entrada
# Recebe n, m e s; n é o total de vértices, m o total de arcos e s é o vértice inicial.
# A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime os caminhos mínimos obtidos pelo algoritmo de Dijkstra.

# Exemplo

# Entrada:
# 5 10 0
# 0 1 10
# 0 4 5
# 1 2 1
# 1 4 2
# 2 3 4
# 3 2 6
# 3 0 7
# 4 1 3
# 4 2 9
# 4 3 2
 
# Saída: 
# [0, 8, 9, 7, 5] 
# [-1, 4, 1, 4, 0] 

# Descrição

# Faça um programa que faz a leitura de um grafo ponderado e um vértice inicial.
# O programa deve imprimir na tela os caminhos mínimos obtidos pelo algoritmo de Dijkstra.

# Entrada
# Recebe n, m e s; n é o total de vértices, m o total de arcos e s é o vértice inicial.
# A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime os caminhos mínimos obtidos pelo algoritmo de Dijkstra.

# Exemplo

# Entrada:
# 5 10 0
# 0 1 10
# 0 4 5
# 1 2 1
# 1 4 2
# 2 3 4
# 3 2 6
# 3 0 7
# 4 1 3
# 4 2 9
# 4 3 2
 
# Saída: 
# [0, 8, 9, 7, 5] 
# [-1, 4, 1, 4, 0] 

def vazio (Q): 
    for i in Q:
        if i != 0:
            return False
    return True


def insere (Q, value, key):
    Q[key] = value
    return Q

def busca (Q, i): 
    if Q[i] == 1: 
        return 1
    return 0

def extraiMinimo (Q):
    idx = minimo(Q)
    value = Q[idx]
    Q[idx] = 0
    return idx, value


def minimo (Q):
    min = 999999
    min_idx = 0
    count = 0
    for i in Q:
        if i < min and i != 0:
            min = i
            min_idx = count
        count += 1
    return min_idx

def relax(u, v, d, pai, w, Q):
    if d[u] + w < d[v]:
        d[v] = d[u] + w
        pai[v] = u
        insere(Q, d[v], v)
        

n, m, s = (int(tmp) for tmp in input().split(" "))
adj = [[] for _ in range(n)]
for k in range(m):
  i, j, p = (int(tmp) for tmp in input().split(" "))
  adj[i].append((j, p))

d = [0] * n
pai = [0] * n
for i in range (0, n):
  d[i] = 9999999
  pai[i] = -1
d[s] = 0
Q = [9999] * n
insere(Q, 0, 1)
while not vazio(Q):
    u = extraiMinimo (Q)[0]
    for i in adj[u]:
        v = i[0]
        w = i[1]
        relax(u, v, d, pai, w, Q)
            

print (d)
print (pai)