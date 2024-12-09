"""
Descrição: Faça um programa que leia um grafo ponderado e calcule um corte mínimo: você pode usar o algoritmo de Ford-Fulkerson para calcular o fluxo máximo de um vértice s até um vértice t.

Entrada: Recebe n, m, s e t; n é o total de vértices, m o total de arcos, s é a fonte e t é o sumidouro.
A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
(Os vértices são identificados de 0 até n-1.)

Saída: Imprime a matriz de fluxo e a matriz de adjacência da rede residual, obtidas pelo algoritmo de Ford-Fulkerson.
Finalmente, imprime o valor da capacidade de um corte mínimo e uma matriz de adjacência para indicar quais arcos pertencem ao corte mínimo encontrado.

Exemplo

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
[[0, 12, 11, 0, 0, 0], [0, 0, 0, 12, 0, 0], [0, 0, 0, 0, 11, 0], [0, 0, 0, 0, 0, 19], [0, 0, 0, 7, 0, 4], [0, 0, 0, 0, 0, 0]]
[[0, 4, 2, 0, 0, 0], [12, 0, 0, 0, 0, 0], [11, 4, 0, 0, 3, 0], [0, 12, 9, 0, 7, 1], [0, 0, 11, 0, 0, 0], [0, 0, 0, 19, 4, 0]]
23
[[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0]]
"""


def matriz_to_list(matriz):
    """
    Converte uma matrix de adjacência em lista de adjacência.

    Args:
        list: Matrix de adjacência.
        

    Returns:
        adj (list): Lista de adjacência.
    """
    n = len(matriz)
    adj = [[] for _ in range(n)]
    for i in range (n):
        for j in range (n):
            if matriz[i][j] != 0:
                adj[i].append((j, matriz[i][j]))
    return adj


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
    atingiveis = [0] * n

    for v in range (n):
        d[v] = -1


    d[s] = -1
    q = [s]

    while not vazio (q):
        u = remove (q)
        for v, peso in adj[u]:
            if d[v] == -1:
                atingiveis[u] = 1
                d[v] = d[u] + 1
                pai[v] = u
                insere (q, v)
    return d, pai, atingiveis

def bfs_matriz(matriz_adj, s):
    """
    Executa Breadth-First Search (BFS) em um grafo.
    
    Arg: Um grafo representado por uma matriz de adjacencia e um vértice inicial s.
    
    Return: Uma lista d de distancia em relação a s, e uma lista dos nós pais.
    """

    adj = matriz_to_list(matriz_adj)


    n = len(adj)
    d = [0] * n
    pai = [-1] * n
    atingiveis = [0] * n

    for v in range (n):
        d[v] = -1


    d[s] = -1
    q = [s]

    while not vazio (q):
        u = remove (q)
        atingiveis[u] = 1
        for v, peso in adj[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                pai[v] = u
                insere (q, v)
    return d, pai, atingiveis

def weight_edge(adj, i, j):
    """
    Retorna o peso da aresta entre i e j, no grafo adj.
    """
    for edge, weigth in adj[i]:
        if edge == j:
            return weigth
    return -1

def change_weigth(l_adj, i, j, weigth):
    """
    Altera o peso da aresta entre i e j, no grafo adj.
    """
    v = l_adj[i]
    for k in range(len(v)):
        a, peso = v[k]
        if a == j:
            if weigth == 0:
                l_adj[i].remove((a, peso))
            else:
                l_adj[i][k] = (j, weigth)
            return

def copy_list_adj(l_adj):
    """
    Retorna uma copia da lista de adj
    """
    l = len(l_adj)
    new_l_adj = [[] for _ in range(l)]
    for i in range(l):
        new_l_adj[i] = l_adj[i].copy()
    return new_l_adj


def caminho_aumentante(adj, s, t):
    """
    Calcula o caminho aumentante e capacidade entre s e t em um grafo adjacência

    Arg: Um grafo representado por uma lista de adjacencia e um vértice inicial s e final t.
    
    Returns:
        - cam_aumentante: Uma lista do caminho contendo os tuplas contendo os vértices i e j.
        - capacidade: Capacidade máxima do caminho.

    """
    d, bfs_pais, a = bfs(adj, s)
    filho = t
    pai = bfs_pais[filho]
    cam_aumentante = []
    capacidade = weight_edge(adj, pai, filho)

    while pai != -1:
        peso = weight_edge(adj, pai, filho)
        cam_aumentante.insert(0, [pai, filho, weight_edge(adj, pai, filho)])
        filho = pai
        pai = bfs_pais[filho]
        if peso < capacidade:
            capacidade = peso
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
    
    residual = copy_list_adj(adj)

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
        fluxo, matrix_residual, residual = aumenta_fluxo(adj, caminho_a, fluxo, capacidade)   
        caminho_a, capacidade = caminho_aumentante(residual, s, t)

    return fluxo, matrix_residual, residual

def matriz_corte(matriz_adj, atingiveis):
    """
    Calcula a matriz de corte

    Args: Grafo representado como matriz de adj, e lista de vértices atingiveis.

    Returns: Matriz de corte e capcidade do corte minimo.
    """
    n = len(matriz_adj)
    m_corte = [[0 for col in range(n)] for row in range(n)]

    soma = 0
    for i in range(n):
        for j in range(n):
            if matriz_adj[i][j] > 0 and atingiveis[i] != atingiveis[j]:
                m_corte[i][j] = 1
                if atingiveis[i] and not atingiveis[j]:
                    soma += matriz_adj[i][j]
    return soma, m_corte

def main():
    """
    Main
    """
    n, m, s, t = (int(tmp) for tmp in input().split(" "))
    adj = [[] for _ in range(n)]
    for k in range(m):
        i, j, p = (int(tmp) for tmp in input().split(" "))
        adj[i].append((j, p))

    fluxo, m_residual, residual_list = ford_fulkerson(adj, s, t)
    d, pais, atingiveis = bfs_matriz(m_residual, s)

    matriz_adj = list_to_matrix(adj)
    soma, m_corte = matriz_corte(matriz_adj, atingiveis)

    print(fluxo)
    print(m_residual)
    print (soma)
    print (m_corte)   

if __name__ == "__main__":
    main()
