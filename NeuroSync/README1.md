Projeto NEUROSYNC - Fase 2: Análise de Algoritmos de Busca
Este documento detalha a arquitetura, implementação e análise de desempenho dos algoritmos de busca desenvolvidos na Fase 2 do projeto NEUROSYNC. O objetivo desta fase é demonstrar e comparar a eficiência de diferentes algoritmos — Busca Sequencial, Busca Binária e Rabin-Karp — em cenários de busca de dados temáticos.

1. Arquitetura Geral do Projeto
O projeto foi estruturado de forma modular para separar a lógica dos algoritmos da sua execução e demonstração, facilitando a manutenção e os testes.

main.py: É o ponto de entrada principal do simulador interativo. Ele apresenta uma interface de linha de comando temática onde o usuário pode escolher qual "protocolo de recuperação" (algoritmo de busca) executar.

testes.py e neurosync_buscas.py: Scripts de teste para análise e demonstração.

testes.py executa uma demonstração de todos os algoritmos em dados simulados e reais, medindo o tempo e imprimindo a complexidade esperada.

neurosync_buscas.py realiza uma análise comparativa direta entre a busca sequencial e a binária para os mesmos alvos, exibindo os resultados lado a lado.

modulos/: Diretório que contém a implementação pura e reutilizável dos algoritmos.

buscas/sequencial/busca_sequencial.py: Módulo que contém a função busca_sequencial.

buscas/binaria/busca_binaria.py: Módulo que contém a função busca_binaria.

buscas/rabin_karp/rabin_karp.py: Módulo que contém a função rabin_karp para busca de substrings.

input/: Diretório que armazena todos os arquivos de dados.

memorias_desordenadas.txt: Contém 10.000 registros de memória em ordem aleatória.

memorias_ordenadas.txt: Contém os mesmos 10.000 registros, mas ordenados por ID.

anomalias_detectadas.txt: Lista de IDs a serem procurados nos testes.

padroes_corrompidos.txt: Lista de padrões de texto (substrings) a serem localizados no "tomo cognitivo".

2. Implementação e Integração dos Algoritmos
2.1. Busca Sequencial (busca_sequencial.py)
Implementação: A função busca_sequencial(lista, alvo) percorre a lista do início ao fim, comparando cada item com o alvo. Ela retorna o índice do item se encontrado (ou -1 se não) e o número total de comparações realizadas.

Integração: É utilizada no Protocolo 1 do main.py. Este protocolo simula uma "varredura lenta" e, apropriadamente, utiliza o arquivo memorias_desordenadas.txt, onde a busca sequencial é a única opção viável.

2.2. Busca Binária (busca_binaria.py)
Implementação: A função busca_binaria(lista, alvo) implementa uma estratégia de "dividir para conquistar". Ela exige que a lista esteja ordenada. A cada passo, ela compara o alvo com o elemento do meio da lista (meio = (inicio + fim) // 2) e descarta a metade da lista onde o alvo não pode estar, reduzindo drasticamente o espaço de busca.

Integração: É utilizada no Protocolo 2 do main.py, que simula um "acesso por catálogo". Este protocolo lê o arquivo memorias_ordenadas.txt, cumprindo o pré-requisito do algoritmo e garantindo sua máxima eficiência.

2.3. Rabin-Karp (rabin_karp.py)
Implementação: A função rabin_karp(texto, padrao) é projetada para encontrar todas as ocorrências de uma substring (padrao) dentro de um texto maior. Sua eficiência vem do uso de uma técnica de rolling hash, onde o valor de hash para a janela de busca é atualizado em tempo constante (hash_janela = (d * (hash_janela - ord(texto[i]) * h) + ord(texto[i + m])) % q) em vez de ser recalculado a cada passo. Para evitar falsos positivos devido a colisões de hash, uma comparação caractere a caractere é realizada sempre que os hashes coincidem.

Integração: É o núcleo do Protocolo 3 em main.py, simulando uma "análise de fragmentos genéticos". Ele busca pelos padrões definidos em padroes_corrompidos.txt dentro do arquivo tomo_cognitivo.txt, demonstrando sua capacidade de encontrar múltiplas ocorrências de pequenas assinaturas em um grande volume de dados.

3. Análise de Complexidade e Eficiência
A análise teórica e os resultados práticos observados nos scripts testes.py e main.py confirmam o comportamento esperado de cada algoritmo.

3.1. Busca Sequencial
Complexidade Teórica: O(n). No pior caso, o tempo de execução cresce de forma linear com o número de elementos (n) na lista.

Eficiência Observada: Nos testes, este algoritmo demonstrou ser significativamente lento para encontrar itens no final da lista, exigindo milhares de comparações. É prático apenas para listas pequenas ou quando a ordenação dos dados não é possível.

3.2. Busca Binária
Complexidade Teórica: O(log n). O tempo de execução cresce de forma logarítmica, o que a torna extremamente eficiente para grandes volumes de dados.

Eficiência Observada: Os testes confirmam sua superioridade. Em uma lista com 10.000 itens, a busca binária encontrou qualquer elemento em no máximo 14 comparações. O tempo de execução foi quase instantâneo. Seu principal custo é a necessidade de manter a lista sempre ordenada.

3.3. Rabin-Karp
Complexidade Teórica: O(n+m) em média, onde n é o comprimento do texto e m é o comprimento do padrão.

Eficiência Observada: O algoritmo se mostrou muito rápido para sua tarefa específica de localizar substrings. No protocolo_rabin de main.py, ele escaneia o "tomo cognitivo" e identifica rapidamente todas as ocorrências das assinaturas corrompidas, provando ser a ferramenta ideal para análise de padrões em grandes blocos de dados.