# Fluxograma do Sistema

O fluxograma a seguir descreve o funcionamento do sistema interativo para manipulação de dados da Árvore B. A lógica do fluxo inicia com o usuário acessando o menu principal, onde são oferecidas diversas opções de operação. A partir da escolha do usuário, o sistema avalia a opção selecionada por meio de uma decisão condicional ("OPÇÃO?"). As opções disponíveis incluem:
- Inserir ID: Adiciona um novo registro à Árvore B.
- Buscar ID: Localiza e exibe um registro específico.
- Remover ID: Exclui um registro da árvore.
- Alterar Info: Permite modificar informações associadas a um ID existente.
- Exibir Tree: Mostra a estrutura atual da Árvore B.

As operações foram organizadas em dois subprocessos distintos:
- Consultar Dados: agrupa as ações de buscar um ID e exibir a estrutura da árvore. Essas operações não modificam a árvore, apenas acessam e exibem informações, por isso foram corretamente separadas em um subprocesso próprio de leitura/visualização.

- Manipular Dados: inclui as operações de inserir ID, remover ID e alterar informações. Todas essas ações envolvem modificações na estrutura da Árvore B, justificando seu agrupamento em um subprocesso específico de manipulação.

Se o usuário optar por “Sair”, o sistema finaliza o fluxo no bloco de término. Caso contrário, após a execução de qualquer uma das funções, o sistema retorna ao menu principal, permitindo a realização de novas operações. O uso correto dos símbolos no fluxograma — como elipses para início/fim, losango para decisão, paralelogramo para entrada/saída e retângulos (inclusive com borda dupla para subprocessos) — garante clareza e organização ao modelo. A separação entre leitura e manipulação de dados torna o sistema mais modular, facilitando tanto a manutenção quanto a compreensão do processo.

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1Ba3r4TCXhvFGZ33L_ezlTu_wjoulwlDS" height="400"  width="1100"/>
</p>
