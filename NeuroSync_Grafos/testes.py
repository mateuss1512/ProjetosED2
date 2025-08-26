
import time
from modulos.buscas.sequencial.busca_sequencial import busca_sequencial
from modulos.buscas.binaria.busca_binaria import busca_binaria
from modulos.buscas.rabin_karp.rabin_karp import rabin_karp

def medir_tempo_busca(funcao_busca, lista, alvo, nome_algoritmo, big_o_teorico):
    print(f"\n⏱️ {nome_algoritmo}")
    inicio = time.time()
    pos, comps = funcao_busca(lista, alvo)
    fim = time.time()
    print(f"🔹 Resultado: posição = {pos}, comparações = {comps}")
    print(f"⏳ Tempo: {(fim - inicio):.6f}s")
    print(f"📈 Complexidade esperada: {big_o_teorico}")

def carregar_lista(path):
    with open(path, "r", encoding="utf-8") as f:
        return [linha.strip().split(" | ")[0] for linha in f.readlines()]

def carregar_texto(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def carregar_padroes(path):
    with open(path, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f.readlines()]

def demo_algoritmos():
    print("🔬 DEMONSTRAÇÃO DE ALGORITMOS E ANÁLISE DE COMPLEXIDADE")

    lista_pequena = ["ID_0001", "ID_0002", "ID_0003", "ID_0004", "ID_0005"]
    lista_grande = [f"ID_{i:04}" for i in range(2000)]

    medir_tempo_busca(busca_sequencial, lista_grande, "ID_1456", "Busca Sequencial (simulada)", "O(n)")
    medir_tempo_busca(busca_binaria, sorted(lista_grande), "ID_1456", "Busca Binária (simulada)", "O(log n)")

    texto_demo = "ABC ABCDAB ABCDABCDABDE códigoX sombra_CK erro_773 sombra_CK"
    padrao = "sombra_CK"
    print(f"\n🧠 Rabin-Karp (simulado) - padrão = '{padrao}'")
    inicio = time.time()
    posicoes = rabin_karp(texto_demo, padrao)
    fim = time.time()
    print(f"🔹 Ocorrências em: {posicoes}")
    print(f"⏳ Tempo: {(fim - inicio):.6f}s")
    print(f"📈 Complexidade esperada: O(n + m)")

    print("\n📁 Testes com arquivos reais")

    lista_d = carregar_lista("input/memorias_desordenadas.txt")
    medir_tempo_busca(busca_sequencial, lista_d, "ID_01456", "Busca Sequencial (arquivo)", "O(n)")

    lista_o = carregar_lista("input/memorias_ordenadas.txt")
    medir_tempo_busca(busca_binaria, lista_o, "ID_01456", "Busca Binária (arquivo)", "O(log n)")

    texto_real = carregar_texto("input/tomo_cognitivo.txt")
    padroes = carregar_padroes("input/padroes_corrompidos.txt")
    for padrao in padroes:
        print(f"\n🔍 Rabin-Karp (arquivo) - padrão = '{padrao}'")
        inicio = time.time()
        posicoes = rabin_karp(texto_real, padrao)
        fim = time.time()
        print(f"🔹 Ocorrências encontradas: {len(posicoes)} em {posicoes}")
        print(f"⏳ Tempo: {(fim - inicio):.6f}s")
        print(f"📈 Complexidade esperada: O(n + m)")

if __name__ == "__main__":
    demo_algoritmos()
