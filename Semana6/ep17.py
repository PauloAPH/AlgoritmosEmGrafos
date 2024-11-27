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
    """
    Converte uma lista de adjacência em matrix de adjacência

    Args:
        adj (list): Lista de adjacência.

    Returns:
        list: Matrix de adjacência.
    """
    n = len(adj)

    matrix_adj = [[0 for col in range(n)] for row in range(n)]

    for i in range(n):
        for  j, peso in adj[i]:
            matrix_adj[i][j] = peso
    return matrix_adj

def insere (queue, x):
    """
    Insere no topo da pilha
    """
    queue.append (x)

def remove (queue):
    """
    Remove e retorna o topo da pilha
    """
    return queue.pop (0)

def vazio (queue):
    """
    Verifica se a pilha é vazia
    """
    return len (queue) == 0

def bfs(adj, s):
    """
    Executa Breadth-First Search (BFS) em um grafo.
    
    Arg: Um grafo representado por uma lista de adjacencia e um vértice inicial s.
    
    Return: Uma lista d de distancia em relação a s, e uma lista dos nós pais.
    """
    n = len(adj)
    d = [0] * n
    pai = [-1] * n
    for v in range (n):
        d[v] = -1
    d[s] = -1
    q = [s]

    while not vazio (q):
        u = remove (q)
        for i in adj[u]:
            v = i[0]
            peso = i[1]
            if d[v] == -1:
                d[v] = d[u] + 1
                pai[v] = u
                insere (q, v)
    return d, pai

def weight_edge(adj, i, j):
    """
    Retorna o peso da aresta entre i e j, no grafo adj.
    """
    for edge, weigth in adj[i]:
        if edge == j:
            return weigth
    return -1

def change_weigth(adj, i, j, weigth):
    """
    Altera o peso da aresta entre i e j, no grafo adj.
    """
    v = adj[i]
    for k in range(len(v)):
        a, peso = v[k]
        if a == j:
            adj[i][k] = (j, weigth)


def caminho_aumentante(adj, s, t):
    """
    Calcula o caminho aumentante e capacidade entre s e t em um grafo adjacência

    Arg: Um grafo representado por uma lista de adjacencia e um vértice inicial s e final t.
    
    Returns:
        - cam_aumentante: Uma lista do caminho contendo os tuplas contendo os vértices i e j.
        - capacidade: Capacidade máxima do caminho.

    """
    d, bfs_pais = bfs(adj, s)
    filho = t
    pai = bfs_pais[filho]
    cam_aumentante = []
    capacidade = weight_edge(adj, pai, filho)
    while pai != -1:
        peso = weight_edge(adj, pai, filho)
        cam_aumentante.insert(0, [pai, filho, weight_edge(adj, pai, filho)])
        filho = pai
        pai = bfs_pais[filho]
        capacidade = min(capacidade, peso)
    return cam_aumentante, capacidade

def aumenta_fluxo(adj, cam_aumentante, fluxo, capacidade):
    """
    Calcula a matrix de fluxo e residual.

    Arg:
        - adj: Grafo representado como lista de adjacência
        - cam_aumentante: Caminho aumentante, representado com lista de tuplas de vértices
        - fluxo: fluxo atual do grafo, representando como matrix de adjácencia.
        - capacidade: Capacidade do caminho
    
    Returns:
        - fluxo: fluxo atualizado do grafo, representando como matrix de adjácencia.
        - matriz_adj_residual: Matrix dos residos.
        - residual: Lista de adjácencia com os residos.

    """
    n = len(adj)
    for i, j, peso in cam_aumentante:
        if weight_edge(adj, i, j) > 0:
            fluxo[i][j] += capacidade
        else:
            fluxo[i][j] -= capacidade
    matriz_adj_residual = list_to_matrix(adj)

    residual = adj.copy()

    for i in range (n):
        for j in range (n):
            if fluxo[i][j] > 0:
                matriz_adj_residual[j][i] = fluxo[i][j]
                matriz_adj_residual[i][j] = weight_edge(adj, i, j) - fluxo[i][j]
                change_weigth(residual, i, j, weight_edge(adj, i, j) - fluxo[i][j])
    return fluxo, matriz_adj_residual, residual

def ford_fulkerson(adj, s, t):
    """
    Executado o algoritimo de Ford Fulkerson em um grafo:

    Args: Grafo representado como lista de adj, vértices inicial s e final t.

    Returns: Fluxo máximo do grafo e Matrix de Residuos.
    """
    n = len(adj)
    fluxo =  [[0 for col in range(n)] for row in range(n)]

    caminho_a, capacidade = caminho_aumentante(adj, s, t)

    while capacidade > 0:
        print(capacidade)
        fluxo, matrix_residual, residual = aumenta_fluxo(adj, caminho_a, fluxo, capacidade)
        caminho_a, capacidade = caminho_aumentante(residual, s, t)
    return fluxo, matrix_residual


def main():
    """
    Main
    """
    n, m, s, t = (int(tmp) for tmp in input().split(" "))
    adj = [[] for _ in range(n)]
    for k in range(m):
        i, j, p = (int(tmp) for tmp in input().split(" "))
        adj[i].append((j, p))
    fluxo, residual = ford_fulkerson(adj, s, t)
    print(fluxo)
    print(residual)

if __name__ == "__main__":
    main()
