
# 🧠 **NeuroSync – Reconstrução da Rede Cognitiva da IA**

**Projeto desenvolvido para a disciplina Estruturas de Dados II: O Mestre dos Algoritmos**

---

## 📌 **Tema do Projeto e Justificativa**

### 💡 **Ideia Principal**
*NeuroSync* é um simulador onde o usuário atua como um técnico responsável pela **recuperação cognitiva** de uma **inteligência artificial** com **memórias corrompidas**. O objetivo é restaurar as conexões entre fragmentos de memória, utilizando **estruturas de dados** e **algoritmos clássicos** de **grafos**, **buscas**, **compressão de dados** e **hashing**.

### 🎯 **Por que esse tema?**
- A ideia é criativa e imersiva, proporcionando uma experiência **interativa** e **desafiadora**.
- Permite a **aplicação prática** de **algoritmos de grafos**, como **buscas** (DFS/BFS), **caminhos ótimos** (Dijkstra), **algoritmos de coloração**, **compressão de dados** (Huffman) e **hashing**.
- Proporciona uma **representação visual e prática** de grafos e memórias, além de manipular a **eficiência** de diferentes algoritmos aplicados em situações do mundo real.

---

## 🛠️ **Funcionalidades Principais**

- **🔍 Recuperação de Fragmentos**: Algoritmos de **DFS** e **BFS** para explorar e restaurar fragmentos de memória.
- **📉 Caminhos Ótimos**: Aplicação do **Dijkstra** para encontrar as rotas de **menor custo** entre os fragmentos de memória.
- **🎨 Evitar Conflitos de Restauração**: Uso de **coloração de grafos** para garantir que memórias adjacentes não sejam restauradas simultaneamente.
- **📅 Sequência de Restauração**: **Ordenação topológica** para determinar a ordem ideal de restauração dos fragmentos.
- **🌳 Reconexão Mínima**: Implementação do **algoritmo de Prim** para restaurar todas as conexões de forma eficiente e sem sobrecarga.
- **🔐 Integração com o Sistema de Hash**: Armazenamento e busca de fragmentos utilizando **estruturas de hash**.

---

## 📚 **Integração com a Ementa da Disciplina**

| **Tópico**                      | **Aplicação no NeuroSync** |
|----------------------------------|----------------------------|
| **Busca Sequencial / Binária**  | Localização de fragmentos de memória |
| **Algoritmos de Grafos (DFS/BFS)** | Exploração de redes de fragmentos de memória |
| **Algoritmos de Caminhos Ótimos** | Cálculo de rotas de **menor custo** entre fragmentos (Dijkstra) |
| **Coloração de Grafos**         | Garantir que **fragmentos adjacentes** não sejam restaurados simultaneamente |
| **Ordenação Topológica**       | Definir a ordem ideal de restauração de fragmentos com dependências |
| **Algoritmos Gulosos**          | Alocação eficiente de recursos durante a restauração |
| **Algoritmos de Reconexão (Prim)** | Reconexão mínima da rede de memória com **custo mínimo** |
| **Programação Dinâmica**        | Restauração ideal de sequências danificadas de fragmentos |
| **Teoria da Complexidade / NP** | Análise da eficiência dos algoritmos aplicados na reconstrução |
| **Hashing**                     | Armazenamento eficiente e busca de fragmentos de memória |

---

## 🧪 **Tecnologias Utilizadas**

- **Linguagem:** Python 3.x
- **Bibliotecas Principais:**
  - **`heapq`, `collections`** – Estruturas de dados auxiliares
  - **`networkx`** – Manipulação e visualização de grafos
  - **`matplotlib`** – Visualizações gráficas simples
  - **`zlib`** – Compressão de dados
  - **Funções manuais** – Implementações de **Dijkstra**, **DFS**, **BFS**, **Prim**, **Welch-Powell (Coloração)**, **Ordenação Topológica** e **Reconstrução de Memórias**.

---

## 📃 **Licença**

Projeto acadêmico — restrito à disciplina de **Estruturas de Dados II**  
© 2025 – Mateus Teixeira Silva
