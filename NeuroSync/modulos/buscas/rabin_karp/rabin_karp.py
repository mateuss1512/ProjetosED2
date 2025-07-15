
def rabin_karp(texto, padrao):
    d = 256  
    q = 101  

    n = len(texto)
    m = len(padrao)
    h = 1
    hash_padrao = 0
    hash_janela = 0
    resultado = []

    if m > n:
        return []

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        hash_padrao = (d * hash_padrao + ord(padrao[i])) % q
        hash_janela = (d * hash_janela + ord(texto[i])) % q

    for i in range(n - m + 1):
        if hash_padrao == hash_janela:
            if texto[i:i + m] == padrao:
                resultado.append(i)

        if i < n - m:
            hash_janela = (d * (hash_janela - ord(texto[i]) * h) + ord(texto[i + m])) % q
            if hash_janela < 0:
                hash_janela += q

    return resultado
