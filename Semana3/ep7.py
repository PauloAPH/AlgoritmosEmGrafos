# Descrição
# Faça um programa que faz a leitura de um grafo e imprime a expressão de parênteses dos componentes fortemente conexos.

# Entrada
# Recebe n, m: n é o total de vértices, m o total de arcos.
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime a expressão de parênteses dos componentes fortemente conexos.

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
# (2 2) (5 5) (0 0) (1 (3 (4 4) 3) 1)

import time

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

def traspose_adj_list(list_adj):
    n = len(list_adj)
    traspose = [[] for _ in range(n)]
    for i in range(n):
        for j in list_adj[i]:
            traspose[j].append(i)
    return traspose

def max_idx(list):
    return list.index(max(list))

def min_idx(lst):
    positive_values = [num for num in lst if num > 0]
    if not positive_values:
        return None  

    min_positive = min(positive_values)
    return lst.index(min_positive)

def imprime_parenteses(d, f):
    texto = ""
    min_d = min_idx(d)
    min_f = min_idx(f)
    while(min_d != None or min_f != None):
        if min_f == None:
            texto += "(" + str(min_d) + " "
            d[min_d] = -1
        elif min_d == None:
            texto += str(min_f) + ") "
            f[min_f] = -1
        elif(d[min_d] < f[min_f]):
            texto += "(" + str(min_d) + " "
            d[min_d] = -1
        else:
            texto += str(min_f) + ") "
            f[min_f] = -1
        min_d = min_idx(d)
        min_f = min_idx(f)
    print(texto)


def dfs(lista_adj, n, max_list):
    tempo = 1
    pilha = []
    d = [0] * n
    f = [0] * n
    for u in range(n):
        d[u] = -1
        f[u] = -1
    
    if max_list == None:
        max_list = list(range(n))
        u = 0
    else:
        u = max_idx(max_list) 
    
    pilha.append(u)
    d[u] = tempo
    max_list[u] = 0
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
                    u = max_idx(max_list)
                    d[u] = tempo
                    max_list[u] = 0
                    tempo += 1
                    pilha.append(u)
        else:
            pilha.append(node)
            u = node
            d[u] = tempo
            max_list[u] = 0
            tempo += 1
    return d, f


def main():
    n, m = (int(tmp) for tmp in input().split(" "))
    lista_adj = [[] for _ in range(n)]
    for k in range(m):
        i, j = (int(tmp) for tmp in input().split(" "))
        lista_adj[i].append(j)

    lista_t = traspose_adj_list(lista_adj)
    d, f = dfs(lista_adj, n, None)
    d2, f2 = dfs(lista_t, n, f)
    imprime_parenteses(d2, f2)
    
if __name__ == "__main__":
    main()
