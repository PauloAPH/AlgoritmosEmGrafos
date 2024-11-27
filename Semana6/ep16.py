'''
Descrição: Faça um programa que leia um grafo ponderado e dois vértices, s e t.
Calcule o primeiro caminho aumentante de um vértice s até um vértice t, usando uma busca em largura (BFS).
Calcule o resultado do primeiro aumento de fluxo, usando o caminho aumentante encontrado.
(Considere o fluxo inicial zero.)

Entrada: Recebe n, m, s e t; n é o total de vértices, m o total de arcos, s é a fonte e t é o sumidouro.A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco. (Os vértices são identificados de 0 até n-1.)

Saída:
Linha 1: imprima o caminho aumentante.
(O formato do caminho é i, j, peso.)
Linha 2: imprima a capacidade deste caminho.
Imprima também o resultado de aumentar o fluxo com este caminho aumentante:
Linha 3:  imprima a "matriz de fluxo".
Linha 4: imprima a matriz de adjacência da rede residual resultante (após o aumento do fluxo).

Exemplo:

Entrada:

6 9 0 5
0 1 16
0 2 13
1 3 12
2 1 4
2 4 14
3 2 9
3 5 20
4 3 7
4 5 4

Saída: 

[[0, 1, 16], [1, 3, 12], [3, 5, 20]]
12

[[0, 12, 0, 0, 0, 0], [0, 0, 0, 12, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 12], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

[[0, 4, 13, 0, 0, 0], [12, 0, 0, 0, 0, 0], [0, 4, 0, 0, 14, 0], [0, 12, 9, 0, 0, 8], [0, 0, 0, 7, 0, 4], [0, 0, 0, 12, 0, 0]]
'''


def list_to_matrix(adj):
    n = len(adj)

    matrix_adj = [[0 for col in range(n)] for row in range(n)]

    for i in range(n):
        for  j, peso in adj[i]:
            matrix_adj[i][j] = peso
    return matrix_adj

def insere (Q, x):
    Q.append (x)

def remove (Q):
    return Q.pop (0)

def vazio (Q):
    return len (Q) == 0

def bfs(adj, s):
    n = len(adj)
    d = [0] * n
    pai = [-1] * n
    for v in range (n):
        d[v] = -1
    d[s] = -1
    
    Q = [s]

    while not vazio (Q):
        u = remove (Q)
        for i in adj[u]:
            v = i[0]
            peso = i[1]
            if d[v] == -1:
                d[v] = d[u] + 1
                pai[v] = u
                insere (Q, v)

    return d, pai

def weight_edge(adj, i, j):
    for edge, weigth in adj[i]:
        if edge == j:
            return weigth

def caminho_aumentante(adj, s, t):
    d, bfs_pais = bfs(adj, s)
    filho = t
    pai = bfs_pais[filho]
    CA = []
    capacidade = weight_edge(adj, pai, filho)
    while pai != -1:
        peso = weight_edge(adj, pai, filho)
        CA.insert(0, [pai, filho, weight_edge(adj, pai, filho)])
        filho = pai
        pai = bfs_pais[filho]
        if peso < capacidade:
            capacidade = peso
    return CA, capacidade

def aumentaFluxo (adj, P, capacidade):
    n = len(adj)
    fluxo =  [[0 for col in range(n)] for row in range(n)]
    for i, j, peso in P:
        v = adj[i]
        if weight_edge(adj, i, j) > 0:
           fluxo[i][j] += capacidade
        else:
            fluxo[i][j] -= capacidade
    

    matrizAdjResidual = list_to_matrix(adj)
    for i in range (n):
        for j in range (n):
            if fluxo[i][j] > 0:
                matrizAdjResidual[j][i] = fluxo[i][j]
                matrizAdjResidual[i][j] = weight_edge(adj, i, j) - fluxo[i][j]
    return fluxo, matrizAdjResidual

def main():
    n, m, s, t = (int(tmp) for tmp in input().split(" "))
    adj = [[] for _ in range(n)]
    for k in range(m):
        i, j, p = (int(tmp) for tmp in input().split(" "))
        adj[i].append((j, p))
    caminho, capacidade = caminho_aumentante(adj, s, t)
    fluxo, residual = aumentaFluxo(adj, caminho, capacidade)
    print(caminho)
    print(capacidade)
    print(fluxo)
    print(residual)
    
if __name__ == "__main__":
    main()