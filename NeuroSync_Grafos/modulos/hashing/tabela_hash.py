def chave_para_int(chave):
    return sum(ord(c) for c in str(chave))

def hash_meio_quadrado(chave, tamanho):
    num = chave_para_int(chave)
    quadrado = num ** 2
    meio = str(quadrado).zfill(6)  
    inicio = len(meio)//2 - 1
    fim = inicio + 3
    return int(meio[inicio:fim]) % tamanho

def hash_enlacamento_limite(chave, tamanho):
    num = chave_para_int(chave)
    return num % tamanho

class TabelaHash:
    def __init__(self, tamanho=10007, metodo="meio_quadrado"):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.colisoes = 0
        self.metodo = metodo

    def _hash(self, chave):
        if self.metodo == "meio_quadrado":
            return hash_meio_quadrado(chave, self.tamanho)
        else:
            return hash_enlacamento_limite(chave, self.tamanho)

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        inicial = indice
        while self.tabela[indice] is not None:
            self.colisoes += 1
            indice = (indice + 1) % self.tamanho
            if indice == inicial:
                raise Exception("Tabela cheia")
        self.tabela[indice] = (chave, valor)

    def buscar(self, chave):
        indice = self._hash(chave)
        inicial = indice
        while self.tabela[indice] is not None:
            if self.tabela[indice][0] == chave:
                return self.tabela[indice][1]
            indice = (indice + 1) % self.tamanho
            if indice == inicial:
                break
        return None
