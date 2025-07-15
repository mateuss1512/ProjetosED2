
import time

def busca_sequencial(lista, alvo):
    comparacoes = 0
    for i, item in enumerate(lista):
        comparacoes += 1
        if alvo in item:
            return i, comparacoes
    return -1, comparacoes

def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    comparacoes = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if alvo in lista[meio]:
            return meio, comparacoes
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes

def carregar_lista(path):
    with open(path, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f.readlines()]

def executar_buscas():
    mem_desordenada = carregar_lista("input/memorias_desordenadas.txt")
    mem_ordenada = carregar_lista("input/memorias_ordenadas.txt")
    anomalias = carregar_lista("input/anomalias_detectadas.txt")

    print("\n🧠 Iniciando análise de anomalias...")
    
    print(f"{'ID':<10} {'SEQ_POS':>8} {'SEQ_COMP':>10} {'SEQ_TIME':>10} | {'BIN_POS':>8} {'BIN_COMP':>10} {'BIN_TIME':>10}")
    print("-" * 70)

    for id_anomalia in anomalias:
        start_seq = time.time()
        pos_s, comps_s = busca_sequencial(mem_desordenada, id_anomalia)
        end_seq = time.time()

        start_bin = time.time()
        pos_b, comps_b = busca_binaria(mem_ordenada, id_anomalia)
        end_bin = time.time()

        print(f"{id_anomalia:<10} {pos_s:>8} {comps_s:>10} {end_seq - start_seq:>10.6f} | {pos_b:>8} {comps_b:>10} {end_bin - start_bin:>10.6f}")

if __name__ == "__main__":
    executar_buscas()
