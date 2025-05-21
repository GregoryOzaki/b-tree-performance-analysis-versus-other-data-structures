# Fluxograma do Sistema

O fluxograma a seguir descreve o funcionamento do sistema interativo para manipulação de dados em uma Árvore B. A lógica do fluxo inicia com o usuário acessando o menu principal, onde são oferecidas diversas opções de operação. A partir da escolha do usuário, o sistema avalia a opção selecionada por meio de uma decisão condicional ("OPÇÃO?"). As opções disponíveis incluem:
- Inserir ID: Adiciona um novo registro à Árvore B.
- Buscar ID: Localiza e exibe um registro específico.
- Remover ID: Exclui um registro da árvore.
- Alterar Info: Permite modificar informações associadas a um ID existente.
- Exibir Tree: Mostra a estrutura atual da Árvore B.

Todas essas operações — com exceção de "Buscar ID" e "Exibir Tree" — envolvem chamadas à rotina de manipulação dos dados da Árvore B, que é o componente central do sistema responsável pelas atualizações na estrutura. Caso o usuário escolha a opção "Sair", o sistema encerra o fluxo com um nó de fim. Se qualquer outra opção for escolhida e concluída, o sistema retorna ao menu principal, permitindo novas interações.

![Fluxograma do Sistema](https://drive.google.com/uc?export=view&id=1ACzUtPHLP3U4XHIP-2tzsTza6icKIcm6)
