# Tabelas de Comparação

As tabelas abaixo comparam o tempo de execução da árvore B com outras estruturas,
como a árvore AVL e a lista encadeada. Foram usadas as mesmas entradas
para as operações de busca, inserção e remoção. As quantidades de entradas
correspondem ao número de IDs inseridos (10, 100 e 1000), enquanto as buscas e
remoções ocorreram em 6, 50 e 500 casos, respectivamente. Além disso, calculou-se o
tempo total das três funções e sua média. O gráfico a seguir compara o desempenho de
execução da árvore B com as outras estruturas.

### Quantidade de Entradas: 10

| Estrutura de Dados | Busca | Inserção | Remoção | Média | Total |
|--------------------|-------|----------|---------|-------|-------|
|      Árvore B      |0.000025|0.000022|0.000041|0.000088|0.000029|
|     Árvore AVL     |0.000008|0.000058|0.000036|0.000101|0.000034|
|   Lista Encadeada  |0.000005|0.000009|0.000007|0.000021|0.000007|

### Quantidade de Entradas: 100

| Estrutura de Dados | Busca | Inserção | Remoção | Média | Total |
|--------------------|-------|----------|---------|-------|-------|
|      Árvore B      |0.000335|0.000261|0.000346|0.000942|0.000314|
|     Árvore AVL     |0.000081|0.000553|0.000391|0.001025|0.000342|
|   Lista Encadeada  |0.000329|0.000588|0.000256|0.001173|0.000391|

### Quantidade de Entradas: 1000

| Estrutura de Dados | Busca | Inserção | Remoção | Média | Total |
|--------------------|-------|----------|---------|-------|-------|
|      Árvore B      |0.008891|0.004039|0.003223|0.016153|0.005384|
|     Árvore AVL     |0.001389|0.010116|0.006978|0.018483|0.006161|
|   Lista Encadeada  |0.045220|0.035778|0.020714|0.101712|0.033904|
