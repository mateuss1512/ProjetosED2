import heapq
from collections import defaultdict

class NoHuffman:
    def __init__(self, caractere, frequencia):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

def construir_arvore(texto):
    frequencias = defaultdict(int)
    for char in texto:
        frequencias[char] += 1

    heap = [NoHuffman(c, f) for c, f in frequencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        esq = heapq.heappop(heap)
        dir = heapq.heappop(heap)
        novo = NoHuffman(None, esq.frequencia + dir.frequencia)
        novo.esquerda = esq
        novo.direita = dir
        heapq.heappush(heap, novo)

    return heap[0] if heap else None

def gerar_codigos(no, prefixo="", codigos=None):
    if codigos is None:
        codigos = {}
    if no:
        if no.caractere is not None:
            codigos[no.caractere] = prefixo
        gerar_codigos(no.esquerda, prefixo + "0", codigos)
        gerar_codigos(no.direita, prefixo + "1", codigos)
    return codigos

def compress_string(texto):
    raiz = construir_arvore(texto)
    codigos = gerar_codigos(raiz)
    bits = "".join(codigos[c] for c in texto)
    return bits, codigos

def decompress_string(bits, codigos):
    inverso = {v: k for k, v in codigos.items()}
    atual = ""
    resultado = ""
    for bit in bits:
        atual += bit
        if atual in inverso:
            resultado += inverso[atual]
            atual = ""
    return resultado

def compress_file(entrada, saida):
    with open(entrada, "r", encoding="utf-8") as f:
        texto = f.read()
    bits, codigos = compress_string(texto)
    with open(saida, "w", encoding="utf-8") as f:
        f.write(bits)
    return len(texto), len(bits)

def decompress_file(entrada, saida, codigos):
    with open(entrada, "r", encoding="utf-8") as f:
        bits = f.read()
    texto = decompress_string(bits, codigos)
    with open(saida, "w", encoding="utf-8") as f:
        f.write(texto)
    return texto
