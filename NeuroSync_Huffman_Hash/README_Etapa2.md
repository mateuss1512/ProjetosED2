# 🧠 NeuroSync – Etapa 2: Otimização e Armazenamento Inteligente

**Projeto desenvolvido para a disciplina Estruturas de Dados II – Continuação do desafio "O Mestre dos Algoritmos"**

---

## 📌 Etapa 2 – Foco e Objetivo

Nesta etapa, o **NeuroSync** evolui de um simples reparador de memórias para um **sistema otimizado de compressão e armazenamento**, trabalhando com **compressão de dados (Huffman)** e **tabelas hash avançadas** para garantir desempenho e organização dos fragmentos cognitivos.

O objetivo foi:
- **Reduzir o espaço ocupado por dados corrompidos ou restaurados** (compressão).
- **Organizar e permitir acesso rápido a milhares de fragmentos (pares chave-valor)** usando **funções de hash** robustas.

---

## 🛠️ Funcionalidades Desenvolvidas na Etapa 2

### **1. Compressão de Dados (Protocolo 4 – Huffman)**
- O usuário pode **comprimir textos ou arquivos** (da pasta `input/`).
- Gera automaticamente:
  - Arquivo comprimido (`*_comprimido.txt`)
  - Arquivo descomprimido (`*_descomprimido.txt`) para teste de integridade.
- Mostra:
  - Tamanho original e comprimido.
  - Percentual de redução.
  - Confirmação de integridade.
- Opção de **descomprimir arquivos existentes** listando automaticamente os comprimidos em `output/`.

---

### **2. Estrutura de Hash (Protocolo 5 – Meio-Quadrado e Enlaçamento Limite)**
- Implementação de **duas funções de hash**:
  - **Meio-Quadrado:** Eleva a chave ao quadrado, extrai dígitos centrais para gerar o índice.
  - **Enlaçamento Limite:** Usa módulo (`chave % tamanho`) como índice.
- **Tabela Hash com sondagem linear** para resolução de colisões.
- Permite:
  - Inserção e busca de milhares de pares chave-valor.
  - Comparação de desempenho entre os métodos (colisões, tempos de inserção e busca).
  - Geração automática de **relatório CSV** (`relatorio_hashing.csv`).

---

### **3. Interatividade e Simulação**
- Após o benchmark, o usuário entra em **modo interativo**:
  - Escolhe qual função de hash usar.
  - Busca por fragmentos com feedback narrativo e barra de integridade dinâmica.
  - Integridade do sistema sobe +4% por acerto e desce -5% por erro.
  - Ao atingir **100% de integridade**, retorna automaticamente ao menu.
  - Exemplos de chaves válidas são exibidos para auxiliar o usuário.
- **Opção extra:** Visualizar toda a **tabela hash**, mostrando índices, chaves, valores e colisões.

---

## 📂 Estrutura do Projeto

```
NeuroSync/
├── main.py                # Menu principal (Protocolos 1 a 5)
├── modulos/
│   ├── buscas/            # Algoritmos de busca (Sequencial, Binária, Rabin-Karp)
│   ├── compressao/        # Algoritmo de Huffman
│   └── hashing/           # Funções e tabela hash
├── input/                 # Arquivos de entrada (textos, pares de teste)
├── output/                # Arquivos comprimidos, descomprimidos e relatórios
└── README.md
```

---

## 🧪 Tecnologias e Bibliotecas

- **Python 3.12**
- **Estruturas e bibliotecas:**
  - `heapq` e `collections` – para Huffman.
  - `time` e `os` – para medições e manipulação de arquivos.
  - `random` – geração e amostragem de chaves.
- **Padrão narrativo e imersivo:** Estilo “console neural” com barras de progresso e integridade.

---

## 📊 Como Executar e Testar a Etapa 2

1. **Executar o menu principal:**
   ```bash
   python main.py
   ```
2. **Selecionar o protocolo desejado:**
   - `4` para **Compressão Huffman**
   - `5` para **Tabela Hash**
3. **Seguir as instruções interativas no terminal**:
   - No **Protocolo 4**, comprimir/descomprimir textos.
   - No **Protocolo 5**, rodar benchmarks, buscar chaves, visualizar a tabela e restaurar a integridade do sistema.

---

## 🎯 Próximos Passos

Na próxima etapa, o **NeuroSync** evoluirá com **programação dinâmica e algoritmos gulosos**, otimizando decisões estratégicas de reparo e organização de memórias.

---
