import time
import os
import datetime
import random
from collections import deque
from modulos.buscas.sequencial.busca_sequencial import busca_sequencial
from modulos.buscas.binaria.busca_binaria import busca_binaria
from modulos.buscas.rabin_karp.rabin_karp import rabin_karp
from modulos.compressao.huffman import compress_string, decompress_string
from modulos.hashing.tabela_hash import TabelaHash
from modulos.grafos.grafo import Grafo
from modulos.grafos.algoritmos import dfs, bfs, dijkstra_caminhos, welch_powell, ordenacao_topologica, prim, reconstruir_rota


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
    if passo == total:
        print()

# carrega apenas o primeiro campo de cada linha, separado por | 
def carregar_lista(path):
    with open(path, "r", encoding="utf-8") as f:
        return [linha.strip().split(" | ")[0] for linha in f.readlines()]

# carrega um arquivo de texto completo como string
def carregar_texto(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# carrega padrões (linhas) de um texto
def carregar_padroes(path):
    with open(path, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f.readlines()]

def protocolo_sequencial():
    print_lento("\n🧩 Protocolo 1: Varredura Lenta e Precisa (Busca Sequencial)")
    lista = carregar_lista("input/memorias_desordenadas.txt")
    try:
        qtd = int(input("🔢 Quantos fragmentos deseja escanear (máx 20)? "))
        qtd = max(1, min(qtd, 20))
    except ValueError:
        qtd = 5
    alvos = random.sample(lista, qtd)

    for i, alvo in enumerate(alvos):
        print_lento(f"🔍 Escaneando fragmento {alvo}...")
        barra_progresso(i+1, len(alvos))
        t0 = time.time()
        pos, comp = busca_sequencial(lista, alvo)
        t1 = time.time()
        print(f"\n   ✅ Localizado na posição {pos} com {comp} comparações. ⏱️ {t1 - t0:.5f}s\n")
        delay(0.5)
    print_lento("✔️ Varredura Sequencial Concluída.")

def protocolo_binario():
    print_lento("\n📚 Protocolo 2: Acesso por Catálogo de Índices (Busca Binária)")
    lista = carregar_lista("input/memorias_ordenadas.txt")
    try:
        qtd = int(input("🔢 Quantos fragmentos deseja escanear (máx 20)? "))
        qtd = max(1, min(qtd, 20))
    except ValueError:
        qtd = 5
    alvos = random.sample(lista, qtd)

    for i, alvo in enumerate(alvos):
        print_lento(f"🔎 Buscando índice do fragmento {alvo}...")
        barra_progresso(i+1, len(alvos))
        t0 = time.time()
        pos, comp = busca_binaria(lista, alvo)
        t1 = time.time()
        print(f"\n   ✅ Encontrado em {pos} com {comp} comparações. ⚡ {t1 - t0:.5f}s\n")
        delay(0.5)
    print_lento("✔️ Varredura Binária Concluída.")

def protocolo_rabin():
    print_lento("\n🧬 Protocolo 3: Análise de Fragmentos Genéticos (Rabin-Karp)")
    texto = carregar_texto("input/tomo_cognitivo.txt")
    padroes_completos = carregar_padroes("input/padroes_corrompidos.txt")
    try:
        qtd = int(input("🔢 Quantas assinaturas corrompidas deseja investigar (máx 10)? "))
        qtd = max(1, min(qtd, len(padroes_completos)))
    except ValueError:
        qtd = 5
    padroes = random.sample(padroes_completos, qtd)

    for i, padrao in enumerate(padroes):
        print_lento(f"🧠 Escaneando assinatura: '{padrao}'...")
        barra_progresso(i+1, len(padroes))
        posicoes = rabin_karp(texto, padrao)
        print(f"\n   🔍 {len(posicoes)} ocorrência(s) detectada(s) nas posições {posicoes[:5]}...\n")
        delay(0.5)
    print_lento("✔️ Varredura de Fragmentos Concluída.")

def protocolo_huffman():
    print_lento("🗜️ Protocolo 4: Compressão de Dados (Huffman)")
    print("Escolha a operação:")
    print("  1. Comprimir texto ou arquivo")
    print("  2. Descomprimir arquivo comprimido (.txt)")
    escolha = input("Digite a opção (1 ou 2): ")

    os.makedirs("output", exist_ok=True) 

    if escolha == "1":
        texto = input("Digite o texto para comprimir (ou deixe vazio para usar um arquivo em input/): ")
        if not texto:
            arquivo = input("Digite o nome do arquivo (em input/): ")
            caminho = f"input/{arquivo}" 
            try:
                with open(caminho, "r", encoding="utf-8") as f:
                    texto = f.read()
            except FileNotFoundError:
                print("❌ Arquivo não encontrado.")
                return
        else:
            arquivo = "texto_digitado.txt"

        base_name = os.path.splitext(arquivo)[0]
        print_lento("📊 Calculando frequências e comprimindo...")
        barra_progresso(1, 2)
        bits, codigos = compress_string(texto) 
        barra_progresso(2, 2)

        compressed_path = f"output/{base_name}_comprimido.txt"
        decompressed_path = f"output/{base_name}_descomprimido.txt"

        with open(compressed_path, "w", encoding="utf-8") as f:
            f.write(bits)

        descomprimido = decompress_string(bits, codigos)
        with open(decompressed_path, "w", encoding="utf-8") as f:
            f.write(descomprimido)

        reducao = 100 - (len(bits) / (len(texto)*8) * 100 if len(texto) > 0 else 0)
        integridade = "OK" if descomprimido == texto else "FALHA"

        print("📊 Resultado da Compressão:")
        print(f"Arquivo original: {arquivo}")
        print(f"Tamanho original: {len(texto)*8} bits")
        print(f"Tamanho comprimido: {len(bits)} bits")
        print(f"Redução: {reducao:.2f}%")
        print(f"Integridade: {integridade}")
        print(f"Arquivos gerados: {compressed_path} (comprimido), {decompressed_path} (descomprimido para teste)")

        with open("output/log_operacoes.txt", "a", encoding="utf-8") as log:
            log.write(f"[{datetime.datetime.now()}] COMPRESSÃO - Arquivo: {arquivo}, Original: {len(texto)*8} bits, Comprimido: {len(bits)} bits, Redução: {reducao:.2f}%, Integridade: {integridade}")

        print_lento("✔️ Compressão Concluída.")

    elif escolha == "2":
        arquivos = [f for f in os.listdir("output") if f.endswith("_comprimido.txt")]
        if not arquivos:
            print("⚠️ Nenhum arquivo comprimido encontrado em 'output/'.")
            return

        print("Arquivos disponíveis para descompressão:")
        for i, nome in enumerate(arquivos, start=1):
            print(f"  {i}. {nome}")

        try:
            opcao = int(input("Escolha o número do arquivo para descomprimir: "))
            if opcao < 1 or opcao > len(arquivos):
                print("❌ Opção inválida.")
                return
        except ValueError:
            print("❌ Entrada inválida.")
            return

        arquivo_escolhido = arquivos[opcao - 1]
        base_name = arquivo_escolhido.replace("_comprimido.txt", "")
        caminho = f"output/{arquivo_escolhido}"

        with open(caminho, "r", encoding="utf-8") as f:
            bits = f.read()

        descomprimido_path = f"output/{base_name}_descomprimido_final.txt"
        origem = f"output/{base_name}_descomprimido.txt"
        if os.path.exists(origem):
            with open(origem, "r", encoding="utf-8") as src, open(descomprimido_path, "w", encoding="utf-8") as dst:
                conteudo = src.read()
                dst.write(conteudo)

            tamanho_original = len(conteudo)*8
            tamanho_comprimido = len(bits)
            reducao = 100 - (tamanho_comprimido / tamanho_original * 100 if tamanho_original > 0 else 0)

            print("📊 Resultado da Descompressão:")
            print(f"Arquivo processado: {arquivo_escolhido}")
            print(f"Tamanho original (reconstruído): {tamanho_original} bits")
            print(f"Tamanho comprimido: {tamanho_comprimido} bits")
            print(f"Redução observada: {reducao:.2f}%")
            print(f"Arquivo descomprimido salvo em: {descomprimido_path}")

            with open("output/log_operacoes.txt", "a", encoding="utf-8") as log:
                log.write(f"[{datetime.datetime.now()}] DESCOMPRESSÃO - Arquivo: {arquivo_escolhido}, Original (rec): {tamanho_original} bits, Comprimido: {tamanho_comprimido} bits, Redução: {reducao:.2f}%")
        else:
            print("⚠️ Arquivo descomprimido correspondente não encontrado para reconstrução.")

def protocolo_hashing():
    print_lento("\n🔐 Protocolo 5: Estrutura de Hash - Armazenamento de Fragmentos")
    print("Escolha a fonte de dados:")
    print("  1. Gerar dados aleatórios (1000 pares)")
    print("  2. Usar arquivo de 10.000 pares (pares_chave_valor.txt)")
    escolha = input("Digite a opção (1 ou 2): ")

    if escolha == "1":
        dados = [(str(i), f"valor_{i}") for i in range(1000)]
        qtd = 1000
    else:
        try:
            with open("input/pares_chave_valor.txt", "r", encoding="utf-8") as f:
                linhas = [linha.strip() for linha in f.readlines() if linha.strip()]
                dados = [linha.split(";") for linha in linhas]
                qtd = len(dados)
        except FileNotFoundError:
            print("❌ Arquivo de 10.000 pares não encontrado em 'input/'.")
            return

    metodos = ["meio_quadrado", "enlacamento_limite"]
    tabelas = {}
    resultados = {}

    for metodo in metodos:
        tabela = TabelaHash(tamanho=10007, metodo=metodo)
        inicio_insercao = time.time()
        for i, (chave, valor) in enumerate(dados):
            tabela.inserir(chave, valor)
            if (i + 1) % (qtd // 5 or 1) == 0:
                barra_progresso(i + 1, qtd)
        fim_insercao = time.time()

        inicio_busca = time.time()
        for chave, _ in dados:
            tabela.buscar(chave)
        fim_busca = time.time()

        resultados[metodo] = {
            "colisoes": tabela.colisoes,
            "tempo_insercao": fim_insercao - inicio_insercao,
            "tempo_busca": fim_busca - inicio_busca
        }
        tabelas[metodo] = tabela
        print()

    print("\n📊 Comparativo de Desempenho (salvo em output/relatorio_hashing.csv):")
    os.makedirs("output", exist_ok=True)
    relatorio_path = "output/relatorio_hashing.csv"
    with open(relatorio_path, "w", encoding="utf-8") as rel:
        rel.write("Metodo,Colisoes,Tempo_Insercao,Tempo_Busca\n")
        for metodo, dados_metodo in resultados.items():
            print(f"Método: {metodo}")
            print(f"  Colisões totais: {dados_metodo['colisoes']}")
            print(f"  Tempo total inserção: {dados_metodo['tempo_insercao']:.4f}s")
            print(f"  Tempo total busca: {dados_metodo['tempo_busca']:.4f}s\n")
            rel.write(f"{metodo},{dados_metodo['colisoes']},{dados_metodo['tempo_insercao']:.4f},{dados_metodo['tempo_busca']:.4f}\n")

    print_lento("✔️ Teste de Hashing Concluído. Relatório gerado.")

    integridade = 80
    print_lento("\n🧠 Entrando em modo de consulta interativa...")
    print("Escolha o método de hash para consultas:")
    print("  1. Meio-Quadrado")
    print("  2. Enlaçamento Limite")
    metodo_op = input("Digite a opção (1 ou 2): ")
    metodo = "meio_quadrado" if metodo_op == "1" else "enlacamento_limite"
    tabela = tabelas[metodo]

    chaves_validas = [ch for ch, _ in dados if ch.isdigit()]
    exemplos = random.sample(chaves_validas, min(5, len(chaves_validas)))

    while True:
        print("\nOpções:")
        print("  1. Buscar chaves")
        print("  2. Visualizar tabela hash")
        print("  3. Voltar ao menu principal")
        op = input("Escolha a opção: ")

        if op == "3":
            print_lento(f"\nSaindo do modo interativo. Integridade final: {integridade}%.")
            break

        if op == "2":
            print(f"\n--- Visualização da Tabela Hash (Método: {metodo}) ---")
            total = 0
            for idx, item in enumerate(tabela.tabela):
                if item is not None:
                    print(f"{idx:5} | Chave: {item[0]:10} | Valor: {item[1]}")
                    total += 1
            print(f"\nTotal de elementos: {total} | Colisões registradas: {tabela.colisoes}")
            continue

        print("\nDigite a chave para buscar (ou 'sair' para encerrar):")
        print(f"Exemplos de chaves válidas: {', '.join(exemplos)}")

        while True:
            chave = input("\nChave a buscar: ")
            if chave.lower() == "sair":
                break
            inicio = time.time()
            valor = tabela.buscar(chave)
            fim = time.time()
            barra_progresso(1, 1)
            if valor is not None:
                integridade = min(100, integridade + 4)
                print(f"  ✅ Fragmento encontrado: {valor} (Tempo: {fim - inicio:.6f}s)")
                print(f"  🔋 Integridade do Sistema: {'█' * (integridade // 5)}{'░' * (20 - integridade // 5)} {integridade}%")
                print("  Fragmento restaurado com sucesso.")
            else:
                integridade = max(0, integridade - 5)
                print(f"  ❌ Chave '{chave}' não encontrada (Tempo: {fim - inicio:.6f}s)")
                print(f"  🔋 Integridade do Sistema: {'█' * (integridade // 5)}{'░' * (20 - integridade // 5)} {integridade}%")
                print("  ⚠️ Fragmento não localizado. Integridade comprometida.")

            if integridade >= 100:
                print_lento("\n🟢 Sistema completamente restaurado. Retornando ao menu principal...")
                delay(2)
                return
            
def protocolo_grafos():
    print_lento("\n🧠 Protocolo 6: Reconstrução da Rede Cognitiva da IA", delay_por_letra=0.02)
    print_lento("🔧 Você acessou o núcleo de memórias corrompidas. É hora de restaurar conexões críticas.")

    while True:
        try:
            num_fragmentos = int(input("\n🔢 Quantos fragmentos de memória deseja analisar? (Máx 20): "))
            if 1 <= num_fragmentos <= 20:
                break
        except ValueError:
            print_lento("❌ Entrada inválida. Digite um número entre 1 e 20.")

    grafo = Grafo(num_fragmentos)
    nomes_fragmentos = [input(f"🏷️ Nome do fragmento {i}: ").strip() or f"Fragmento_{i}" for i in range(num_fragmentos)]
    print_lento("\n✅ Fragmentos criados com sucesso!")

    while True:
        print("\n📋 Ações disponíveis na rede:")
        print("1. ➕ Adicionar conexão")
        print("2. ➖ Remover conexão")
        print("3. 👁️ Visualizar rede (matriz/lista)")
        print("4. 🔍 Explorar fragmentos (DFS)")
        print("5. 🌊 Propagação de sinal (BFS)")
        print("6. 📈 Rota de menor custo (Dijkstra)")
        print("7. 🎨 Evitar conflitos (Coloração)")
        print("8. 📅 Sequência de restauração (Topológica)")
        print("9. 🌳 Reconexão mínima (AGM – Prim)")
        print("0. 🔙 Voltar ao menu principal")

        escolha = input("Escolha a opção: ")

        if escolha == "1":
            try:
                entrada = input("Digite origem destino custo: ")
                origem, destino, custo = map(int, entrada.split())
                grafo.adicionar_aresta(origem, destino, custo)
                print_lento(f"✅ Conexão adicionada: {nomes_fragmentos[origem]} ↔ {nomes_fragmentos[destino]} (custo {custo})")
            except:
                print_lento("❌ Formato inválido! Use números inteiros: origem destino custo.")

        elif escolha == "2":
            try:
                entrada = input("Digite origem destino para remover conexão: ")
                origem, destino = map(int, entrada.split())
                grafo.remover_aresta(origem, destino)
                print_lento(f"✅ Conexão removida: {nomes_fragmentos[origem]} ↔ {nomes_fragmentos[destino]}")
            except:
                print_lento("❌ Formato inválido! Use números inteiros: origem destino.")

        elif escolha == "3":
            print_lento("\n📊 Matriz de adjacência:")
            grafo.mostrar_matriz()
            print_lento("\n📋 Lista de adjacência:")
            grafo.mostrar_lista(nomes_fragmentos)

        elif escolha == "4":
            cores = [-1] * grafo.num_vertices
            print_lento("\n🔍 Explorando fragmentos com DFS...")
            delay(1)
            dfs(grafo, 0, visitados=set(), cores=cores, nomes_fragmentos=nomes_fragmentos)
            print("\n✔️ Exploração concluída.")

        elif escolha == "5":
            cores = [-1] * grafo.num_vertices
            print_lento("\n🌊 Propagando sinal com BFS...")
            delay(1)
            ordem = bfs(grafo, 0, nomes_fragmentos=nomes_fragmentos, cores=cores)
            print("📡 Fragmentos visitados na ordem:")
            print(" → ".join(ordem))
            print_lento("✔️ Propagação concluída.")

        elif escolha == "6":
            cores = [-1] * grafo.num_vertices
            print_lento("\n📈 Calculando rota de menor custo (Dijkstra)...")
            delay(1)
            distancias, prev = dijkstra_caminhos(grafo, 0, cores)
            print("📊 Rotas e custos a partir do fragmento inicial:")
            for i, d in enumerate(distancias):
                if d == float('inf'):
                    print(f"   - {nomes_fragmentos[i]}: inacessível")
                else:
                    rota = reconstruir_rota(prev, i, nomes_fragmentos)
                    print(f"   - {nomes_fragmentos[i]}: custo {d} | rota: {rota}")
            print_lento("✔️ Cálculo concluído.")

        elif escolha == "7":
            print_lento("\n🎨 Atribuindo cores para evitar conflitos...")
            delay(1)
            
            cores = welch_powell(grafo)

            legenda = {
                0: "🟢 Livre",
                1: "🔴 Em uso",
                2: "🟡 Reserva",
                3: "🔵 Outro"
            }

            for i, c in enumerate(cores):
                cor_legenda = legenda.get(c, "🔘 Não atribuído")
                print(f"   - {nomes_fragmentos[i]} → cor {c} {cor_legenda}")

            print_lento("✔️ Coloração concluída.")
            
        elif escolha == "8":
            print_lento("\n📅 Determinando sequência de restauração (Topológica)...")
            delay(1)
            topo = ordenacao_topologica(grafo)
            if topo:
                print("📌 Ordem sugerida:")
                print(" → ".join([nomes_fragmentos[i] for i in topo]))
                print_lento("✔️ Sequência válida.")
            else:
                print_lento("❌ Ciclo detectado. Sequência impossível.")

        elif escolha == "9":
            print_lento("\n🌳 Reconectando rede com AGM (Prim)...")
            delay(1)
            mst = prim(grafo)
            total = 0
            print("🔗 Conexões restauradas:")
            for peso, vertice in mst:
                total += peso
                print(f"   - {nomes_fragmentos[vertice]} (custo {peso})")
            print(f"💰 Custo total: {total}")
            print_lento("✔️ Reconexão completa.")

        elif escolha == "0":
            print_lento("\nVoltando ao menu principal...")
            break

        else:
            print_lento("❌ Opção inválida! Escolha um número de 0 a 9.")

def iniciar_simulador():
    limpar_terminal()
    print_lento("🔐 Sistema NEUROSYNC - Terminal de Recuperação Cognitiva", delay_por_letra=0.02)
    delay(2)
    print_lento("\nInicializando diagnóstico de integridade neural...\n")
    delay(1)

    while True:
        print("⚠️  Anomalias detectadas em múltiplos setores.")
        print("📋 Protocolos disponíveis:")
        print("  1. 🔎 Varredura Lenta e Precisa (Busca Sequencial)")
        print("  2. ⚡ Acesso por Catálogo de Índices (Busca Binária)")
        print("  3. 🧬 Análise de Fragmentos Genéticos (Rabin-Karp)")
        print("  4. 🗜️ Compressão de Dados (Huffman)")
        print("  5. 🔐 Estrutura de Hash - Armazenamento")
        print("  6. 🧠 Reconstrução da Rede Cognitiva da IA")
        print("  0. ❌ Encerrar sessão")
        escolha = input("\nDigite o protocolo desejado ((1–6) - 0 para sair): ")
        if escolha == "1":
            protocolo_sequencial()
        elif escolha == "2":
            protocolo_binario()
        elif escolha == "3":
            protocolo_rabin()
        elif escolha == "4":
            protocolo_huffman()
        elif escolha == "5":
            protocolo_hashing()
        elif escolha == "6":
            protocolo_grafos()
        elif escolha == "0":
            print_lento("\n🧠 Sessão NEUROSYNC finalizada. Memória estabilizada.")
            break
        else:
            print("❌ Entrada inválida. Tente novamente.")

if __name__ == "__main__":
    iniciar_simulador()


            
