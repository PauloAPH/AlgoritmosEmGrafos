# Descrição
# Faça um programa que faz a leitura de um grafo e imprime na tela as listas de adjacências do seu grafo transposto.

# Entrada
# Recebe n e m; n é o total de vértices e m o total de arcos.
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime as listas de adjacência do grafo transposto.

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
# 0: 
# 1: 0 3 
# 2: 
# 3: 0 4 
# 4: 1 2 
# 5: 2 5 

# Versao2: com listas de adjacencias

def traspose_adj_list(list_adj):
    n = len(list_adj)
    traspose = [[] for _ in range(n)]
    for i in range(n):
        for j in list_adj[i]:
            traspose[j].append(i)
    return traspose

def imprime_list_adj(lista_adj):
    for i in range (len(lista_adj)):
        texto = "%d: " % i
        for j in lista_adj[i]:
            texto += "%d " % j
        print (texto)    


# leitura dos dados de entrada do EP
n, m = (int(tmp) for tmp in input().split(" "))
matrizAdj = [[0 for col in range(n)] for row in range(n)]
adj = [[] for _ in range(n)]
for i in range (0, m):
    i, j = (int(tmp) for tmp in input().split(" "))
    adj[i].append(j)
    matrizAdj[i][j] = 1

  
adj_t = traspose_adj_list(adj)
imprime_list_adj(adj_t)