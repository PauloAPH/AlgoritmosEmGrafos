# Descrição
# Faça um programa que faz a leitura de um grafo e imprime os instantes de descoberta e de finialização para cada vértice do grafo, de acordo com uma visita DFS (ou busca em profundidade).

# Entrada
# Recebe n, m: n é o total de vértices, m o total de arcos (o vértice inicial sempre será o vértice 0).
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime os instantes (descoberta e finalização) obtidos pela busca DFS.

# Exemplo
# Entrada:
# 6 8
# 0 1
# 0 3
# 1 4
# 2 4
# 2 5
# 3 1
# 4 3
# 5 5
# Saída: 
# [1, 2, 9, 4, 3, 10]
# [8, 7, 12, 5, 6, 11]

def not_visited(neighbors, d):
    for i in neighbors:
        if d[i] == -1:
            return i
    return -1

def is_all_nodes_visited(d):
    for i in range(len(d)):
        if d[i] == -1:
            return i
    return -1


def main():
    n, m = (int(tmp) for tmp in input().split(" "))
    lista_adj = [[] for _ in range(n)]
    for k in range(m):
        i, j = (int(tmp) for tmp in input().split(" "))
        lista_adj[i].append(j)


    # inicializacao
    d = [0] * n
    f = [0] * n
    for u in range(n):
        d[u] = -1
        f[u] = -1
    
    tempo = 1
    pilha = []
    u = 0
    pilha.append(u)
    d[u] = tempo
    tempo += 1
    
    while(len(pilha) != 0):
        node = not_visited(lista_adj[u], d)
        if node == -1:
            f[u] = tempo
            tempo += 1
            pilha.pop()
            if len(pilha) != 0:
                u = pilha[-1]
            else:
                node = is_all_nodes_visited(d)
                if node != -1:
                    u = node
                    d[u] = tempo
                    tempo += 1
                    pilha.append(u)
        else:
            pilha.append(node)
            u = node
            d[u] = tempo
            tempo += 1
    print (d)
    print (f)


if __name__ == "__main__":
    main()