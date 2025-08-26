class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz_adj = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.lista_adj = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, origem, destino, peso=1):
        self.matriz_adj[origem][destino] = peso
        self.matriz_adj[destino][origem] = peso
        self.lista_adj[origem].append((destino, peso))
        self.lista_adj[destino].append((origem, peso))

    def remover_aresta(self, origem, destino):
        self.matriz_adj[origem][destino] = 0
        self.matriz_adj[destino][origem] = 0
        self.lista_adj[origem] = [x for x in self.lista_adj[origem] if x[0] != destino]
        self.lista_adj[destino] = [x for x in self.lista_adj[destino] if x[0] != origem]

    def mostrar_matriz(self):
        for linha in self.matriz_adj:
            print(linha)

    def mostrar_lista(self, nomes_vertices=None):
        for i, lista in enumerate(self.lista_adj):
            if nomes_vertices:
                conexoes = ", ".join([f"{nomes_vertices[v]}({p})" for v, p in lista])
                print(f"{nomes_vertices[i]}: {conexoes}")
            else:
                print(f"{i}: {lista}")
