# Descrição
# Faça um programa que faz a leitura de um grafo e imprime a matriz de distâncias obtidas por buscas em largura (BFS).

# Entrada
# Recebe n, m: n é o total de vértices, m o total de arcos.
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)
 
# Saída
# Imprime a matriz de distâncias obtidas por buscas BFS.

# Exemplo
# Entrada:
# 6 14
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
# 0: 0 1 2 2 1 3 
# 1: 1 0 1 2 1 3 
# 2: 2 1 0 1 2 2 
# 3: 2 2 1 0 1 1 
# 4: 1 1 2 1 0 2 
# 5: 3 3 2 1 2 0


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



def bfs(g, start_node):
    d = [0] * len(g)
    for v in range (len(g)):
        d[v] = -1
    d[start_node] = 0

    Q = [start_node]
    while not vazio (Q):
        u = remove (Q)
        for v in g[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                insere (Q, v)
    return d

def main():
    n, m = (int(tmp) for tmp in input().split(" "))
    adj = [[] for _ in range(n)]
    for k in range(m):
        i, j = (int(tmp) for tmp in input().split(" "))
        adj[i].append(j)
    matriz_dist = []
    for i in range(n):
        matriz_dist.append( bfs(adj, i) )
    
    # imprime a matriz
    for i in range(n):
        msg = "%d: " % i
        for j in range(n):
            msg += "%d " % matriz_dist[i][j]
        print (msg)   

if __name__ == "__main__":
    main()