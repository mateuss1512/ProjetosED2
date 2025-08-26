def busca_sequencial(lista, alvo):
    comparacoes = 0
    for i, item in enumerate(lista):
        comparacoes += 1
        if item == alvo:
            return i, comparacoes
    return -1, comparacoes
