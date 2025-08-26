import heapq
from collections import deque

# -----------------------
# Algoritmos de Navegação
# -----------------------

def dfs(grafo, vertice, visitados=None, cores=None, nomes_fragmentos=None):
    if visitados is None:
        visitados = set()
    if cores[vertice] != -1:
        return
    visitados.add(vertice)
    if nomes_fragmentos:
        print(nomes_fragmentos[vertice], end=" → ")
    for vizinho, _ in grafo.lista_adj[vertice]:
        if vizinho not in visitados and cores[vizinho] == -1:  
            dfs(grafo, vizinho, visitados, cores, nomes_fragmentos)


def bfs(grafo, vertice_inicial, nomes_fragmentos=None, cores=None):
    visitados = [False] * grafo.num_vertices
    fila = deque([vertice_inicial])
    visitados[vertice_inicial] = True
    ordem = []
    while fila:
        vertice = fila.popleft()
        if cores[vertice] != -1:  
            continue
        ordem.append(vertice)
        for vizinho, _ in grafo.lista_adj[vertice]:
            if not visitados[vizinho] and cores[vizinho] == -1:  
                fila.append(vizinho)
                visitados[vizinho] = True
    if nomes_fragmentos:
        return [nomes_fragmentos[v] for v in ordem]
    return ordem


# -----------------------
# Algoritmo de Dijkstra
# -----------------------

def dijkstra_caminhos(grafo, origem, cores):
    n = grafo.num_vertices
    distancias = [float('inf')] * n
    prev = [None] * n
    distancias[origem] = 0

    heap = [(0, origem)]

    while heap:
        try:
            distancia_atual, vertice_atual = heapq.heappop(heap)
        except IndexError:
            break

        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo.lista_adj[vertice_atual]:
            if cores[vizinho] != -1: 
                continue
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                prev[vizinho] = vertice_atual
                heapq.heappush(heap, (nova_distancia, vizinho))

    return distancias, prev

def reconstruir_rota(prev, destino, nomes_fragmentos):
    rota = []
    v = destino
    while v is not None:
        rota.append(nomes_fragmentos[v])
        v = prev[v]
    rota.reverse()
    return " → ".join(rota)

# -----------------------
# Algoritmos de Otimização
# -----------------------

def welch_powell(grafo):
    grau = [(i, len(grafo.lista_adj[i])) for i in range(grafo.num_vertices)]
    grau.sort(key=lambda x: x[1], reverse=True) 

    cores = [-1] * grafo.num_vertices  

    for vertice, _ in grau:
        vizinhos = set()
        for vizinho, _ in grafo.lista_adj[vertice]:
            if cores[vizinho] != -1:
                vizinhos.add(cores[vizinho])
        cor = 0
        while cor in vizinhos:  
            cor += 1
        cores[vertice] = cor  

    return cores

def ordenacao_topologica(grafo):
    grau_entrada = [0] * grafo.num_vertices
    for i in range(grafo.num_vertices):
        for vizinho, _ in grafo.lista_adj[i]:
            grau_entrada[vizinho] += 1
    fila = deque([i for i in range(grafo.num_vertices) if grau_entrada[i] == 0])
    resultado = []
    while fila:
        vertice = fila.popleft()
        resultado.append(vertice)
        for vizinho, _ in grafo.lista_adj[vertice]:
            grau_entrada[vizinho] -= 1
            if grau_entrada[vizinho] == 0:
                fila.append(vizinho)
    if len(resultado) != grafo.num_vertices:
        return None  # ciclo detectado
    return resultado

def prim(grafo):
    mst = []
    visitados = [False] * grafo.num_vertices
    heap = [(0, 0)]  # peso, vertice
    while heap:
        peso, vertice = heapq.heappop(heap)
        if visitados[vertice]:
            continue
        visitados[vertice] = True
        mst.append((peso, vertice))
        for vizinho, peso_aresta in grafo.lista_adj[vertice]:
            if not visitados[vizinho]:
                heapq.heappush(heap, (peso_aresta, vizinho))
    return mst
