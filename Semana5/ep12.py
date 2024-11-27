'''
Descrição
Faça um programa que leia um grafo ponderado e calcule uma árvore geradora mínima pelo algoritmo de Prim.

Entrada
Recebe n, m e r; n é o total de vértices, m o total de arcos e r é a raiz da árvore geradora mínima.
A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
(Os vértices são identificados de 0 até n-1.)

Saída
Imprime dois vetores.
Na primeira linha, o vetor das "chaves".
Na segunda linha, o vetor de "pai" (para representar a árvore).

Exemplo1

Entrada:
6 16 0
0 1 4
1 0 4
0 4 8
4 0 8
1 4 11
4 1 11
1 2 8
2 1 8
2 3 6
3 2 6
2 5 2
5 2 2
4 5 7
5 4 7
3 4 1
4 3 1

Saída: 
[0, 4, 8, 6, 1, 2]
[-1, 0, 1, 2, 3, 2] 
 
Exemplo2

Entrada:
9 28 0
0 1 4
1 0 4
0 8 8
8 0 8
1 8 11
8 1 11
1 2 8
2 1 8
2 3 7
3 2 7
2 5 4
5 2 4
2 7 2
7 2 2
3 4 9
4 3 9
3 5 14
5 3 14
4 5 10
5 4 10
5 6 2
6 5 2
6 7 6
7 6 6
6 8 1
8 6 1
7 8 7
8 7 7

Saída: 
[0, 4, 8, 7, 9, 4, 2, 2, 1]
[-1, 0, 1, 2, 3, 2, 5, 2, 6]
'''

def vazio (Q): 
    for i in Q:
        if i != 0:
            return False
    return True


def insere (Q, value, key):
    Q[key] = value
    return Q

def busca (Q, i): 
    if Q[i] != 0: 
        return True
    return False

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

n, m, s = (int(tmp) for tmp in input().split(" "))
adj = [[] for _ in range(n)]
for k in range(m):
  i, j, p = (int(tmp) for tmp in input().split(" "))
  adj[i].append((j, p))


chave = [0] * n
pai = [0] * n

for i in range (0, n):
  chave[i] = 9999999
  pai[i] = -1
chave[s] = 0

MST = [0] * n
Q = [0] * n
insere(Q, 1, 0)

print(adj)
while not vazio(Q):
    u = extraiMinimo (Q)[0]
    for i in adj[u]:
        v = i[0]
        w = i[1]
        if MST[v] == 0:
            MST[v] = 1
            chave[v] = w
            pai[v] = u
            insere(Q, w, v)
        elif MST[v] == 1 and  chave[v] > w:
            chave[v] = w
            pai[v] = u
        print(u, v, chave)
    MST[u] = 2
            
print (chave)
print (pai)