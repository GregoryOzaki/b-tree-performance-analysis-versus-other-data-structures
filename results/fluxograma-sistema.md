# Fluxograma do Sistema

O fluxograma a seguir representa o funcionamento de um sistema interativo voltado para o gerenciamento de dados em uma Árvore B. O processo tem início com o usuário acessando o menu principal, onde são apresentadas diversas opções de operação. A escolha do usuário é avaliada por meio de um bloco de decisão (“OPÇÃO?”), que direciona o fluxo conforme a funcionalidade selecionada. As opções disponíveis incluem:
- Inserir ID: adiciona um novo registro à Árvore B.
- Buscar ID: localiza e exibe um registro específico.
- Remover ID: exclui um registro existente da árvore.
- Alterar Info: modifica informações associadas a um ID.
- Exibir Tree: mostra visualmente a estrutura atual da Árvore B.
-Sair: encerra o sistema.

As funcionalidades foram organizadas em dois subprocessos distintos, com o objetivo de tornar o sistema mais modular e claro:
- Consultar Dados: agrupa as ações de buscar ID e exibir a árvore, que não alteram a estrutura de dados, apenas acessam e apresentam informações.
- Manipular Dados: concentra as ações de inserção, remoção e alteração de informações, que envolvem mudanças diretas na estrutura da Árvore B.

Ao selecionar "Sair", o sistema finaliza o processo. Para todas as demais opções, após a execução da operação correspondente, o fluxo retorna ao menu, permitindo que novas ações sejam realizadas. O fluxograma utiliza corretamente os símbolos padrão: elipses para início e fim, losango para decisão, paralelogramo para entrada/saída e retângulos (com borda dupla nos subprocessos) para representar as atividades. Essa estrutura contribui para uma visualização clara, organizada e de fácil entendimento, além de reforçar a distinção entre operações de leitura e de manipulação de dados.


<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1Ba3r4TCXhvFGZ33L_ezlTu_wjoulwlDS" height="500"  width="1100"/>
</p>
