# b-tree-performance-analysis-versus-other-data-structures

Este repositório contém a implementação, testes e resultados do artigo "Um Sistema de Gerenciamento de Desastres Ambientais utilizando Árvore B: Uma Análise Comparativa de Desempenho frente a Outras Estruturas de Dados", desenvolvido por Gregory Gabriel Ozaki Coelho e Rallyson Dos Santos Ferreira.

### 📌 Introdução
O trabalho propõe a implementação de uma Árvore B como estrutura de dados principal para o gerenciamento de registros de desastres ambientais, com foco na eficiência em operações de busca, inserção e remoção. A performance da Árvore B foi comparada com árvores AVL e listas encadeadas, demonstrando sua superioridade em cenários com grande volume de dados.

### 🛠️ Material e Métodos
- Linguagem: Python
- Ambiente: Windows (desktop e notebook)
- Ferramentas: Visual Studio Code, Draw.io

Implementações:
- Geração de IDs únicos baseados no tipo e data do desastre.
- Operações de inserção, busca e remoção com Árvore B.
- Scripts para medições de tempo de execução utilizando a biblioteca time.
- Comparações com árvore AVL e lista encadeada.

### 🔍 Resultados
Os testes revelaram que a Árvore B:
- Supera as demais estruturas em desempenho com grandes volumes de dados;
- Mantém o balanceamento eficiente após várias inserções e remoções;
- Tem desempenho inferior em pequenos conjuntos, mas se destaca em escalabilidade.

Para visualizar os gráficos, fluxograma do sistema e tabela de desempenho, acesse a 📂 pasta de resultados.

💻 Códigos
Todos os códigos-fonte das estruturas utilizadas nos testes estão disponíveis na 📂 pasta de código.

### 🔭 Trabalhos Futuros
- Desenvolvimento de uma interface gráfica para facilitar o uso por gestores e pesquisadores;
- Integração com banco de dados para persistência de informações e análise histórica;
- Expansão do sistema para diferentes contextos ambientais.
