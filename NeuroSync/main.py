
import time
import os
import sys
import random
from modulos.buscas.sequencial.busca_sequencial import busca_sequencial
from modulos.buscas.binaria.busca_binaria import busca_binaria
from modulos.buscas.rabin_karp.rabin_karp import rabin_karp

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def delay(ms=1.0):
    time.sleep(ms)

def print_lento(texto, delay_por_letra=0.01):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay_por_letra)
    print()

def barra_progresso(passo, total, largura=40):
    progresso = int((passo / total) * largura)
    barra = '█' * progresso + '-' * (largura - progresso)
    print(f"\r⏳ Progresso: |{barra}| {passo}/{total}", end='', flush=True)

def carregar_lista(path):
    with open(path, "r", encoding="utf-8") as f:
        return [linha.strip().split(" | ")[0] for linha in f.readlines()]

def carregar_texto(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def carregar_padroes(path):
    with open(path, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f.readlines()]

def exibir_opcoes_disponiveis(lista, titulo="IDs disponíveis para análise"):
    print(f"\n📂 {titulo}:")
    for i in range(0, len(lista), len(lista)//3)[:5]:
        print(f"   🧠 {lista[i]}")
    print()

def protocolo_sequencial():
    print_lento("\n🧩 Protocolo 1: Varredura Lenta e Precisa (Busca Sequencial)")
    lista = carregar_lista("input/memorias_desordenadas.txt")
    alvos = ['ID_00647', 'ID_06192', 'ID_03339', 'ID_08400', 'ID_08402']  
    exibir_opcoes_disponiveis(lista)

    for i, alvo in enumerate(alvos):
        print_lento(f"🔍 Escaneando fragmento {alvo}...")
        barra_progresso(i+1, len(alvos))
        t0 = time.time()
        pos, comp = busca_sequencial(lista, alvo)
        t1 = time.time()
        print(f"\n   ✅ Fragmento localizado na posição {pos}, com {comp} comparações.")
        print(f"   ⏱️ Tempo: {t1 - t0:.5f}s\n")
        delay(0.5)

def protocolo_binario():
    print_lento("\n📚 Protocolo 2: Acesso por Catálogo de Índices (Busca Binária)")
    lista = carregar_lista("input/memorias_ordenadas.txt")
    alvos = ['ID_06753', 'ID_00381', 'ID_00928', 'ID_05288', 'ID_00001']  
    exibir_opcoes_disponiveis(lista)

    for i, alvo in enumerate(alvos):
        print_lento(f"🔎 Buscando índice do fragmento {alvo}...")
        barra_progresso(i+1, len(alvos))
        t0 = time.time()
        pos, comp = busca_binaria(lista, alvo)
        t1 = time.time()
        print(f"\n   ✅ Encontrado em {pos}, {comp} comparações.")
        print(f"   ⚡ Tempo: {t1 - t0:.5f}s\n")
        delay(0.5)

def protocolo_rabin():
    print_lento("\n🧬 Protocolo 3: Análise de Fragmentos Genéticos (Rabin-Karp)")
    texto = carregar_texto("input/tomo_cognitivo.txt")
    padroes_completos = carregar_padroes("input/padroes_corrompidos.txt")
    try:
        qtd_input = int(input("🔢 Quantas assinaturas corrompidas deseja investigar? (1-10)"))
        qtd = max(1, min(qtd_input, len(padroes_completos)))
    except ValueError:
        qtd = 5
    padroes = random.sample(padroes_completos, qtd)

    print("🧬 Padrões a serem analisados:")
    for padrao in padroes:
        print(f"   🧠 '{padrao}'")
    print()

    for i, padrao in enumerate(padroes):
        print_lento(f"🧠 Escaneando assinatura: '{padrao}'...")
        barra_progresso(i+1, len(padroes))
        posicoes = rabin_karp(texto, padrao)
        print(f"\n   🔍 {len(posicoes)} ocorrência(s) detectada(s) nas posições {posicoes[:5]}...")
        delay(0.5)

def iniciar_simulador():
    limpar_terminal()
    print_lento("🔐 Sistema NEUROSYNC - Terminal de Recuperação Cognitiva", delay_por_letra=0.02)
    delay(1)
    print_lento("\nInicializando diagnóstico de integridade neural...\n")
    delay(2)
    print("⚠️  Anomalias detectadas em 3 setores principais.")
    print("📋 Protocolos disponíveis:")
    print("  1. 🔎 Varredura Lenta e Precisa (Busca Sequencial)")
    print("  2. ⚡ Acesso por Catálogo de Índices (Busca Binária)")
    print("  3. 🧬 Análise de Fragmentos Genéticos (Rabin-Karp)")
    print("  0. ❌ Encerrar sessão")

    while True:
        escolha = input("\nDigite o protocolo desejado (1–3): ")
        if escolha == "1":
            protocolo_sequencial()
        elif escolha == "2":
            protocolo_binario()
        elif escolha == "3":
            protocolo_rabin()
        elif escolha == "0":
            print_lento("\n🧠 Sessão NEUROSYNC finalizada. Memória estabilizada.")
            break
        else:
            print("❌ Entrada inválida. Tente novamente.")

if __name__ == "__main__":
    iniciar_simulador()