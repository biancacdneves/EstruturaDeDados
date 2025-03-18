# explicando o funcionamento da estrutura de dados das pilhas,

#Pilha (Stacks)

Em um array, é possível utilizar funções próprias para manipular elementos em qualquer posição da lista. Porém, há situações (veremos exemplos mais adiante) onde é desejável mais controle sobre as operações que podem ser feitas na estrutura. Aí entra a implementação de estruturas de dados como a pilha (stack) e a fila (queue).

A pilha é uma estrutura de dados que, assim como o array, é similar a uma lista. O paradigma principal por trás da pilha é o LIFO - Last In, First Out, ou “o último a entrar é o primeiro a sair”, em tradução livre.

Para entendermos melhor o que significa isso, pense em uma pilha de livros ou de pratos. Ao empilharmos livros, por exemplo, o primeiro livro a ser retirado da pilha é obrigatoriamente o último que foi colocado; se tentarmos retirar o último livro da pilha, tudo vai desabar. Ou seja, o último livro a ser empilhado é o primeiro a ser retirado.

Abstraindo este princípio para código, percebe-se que há apenas dois métodos possíveis para manipular os dados de uma pilha: 1) inserir um elemento no topo da pilha e 2) remover um elemento do topo da pilha.

Ao contrário do array, as linguagens de programação normalmente não têm métodos nativos para criação e manipulação de pilhas. Porém, é possível usar métodos de array para a implementação de pilhas.

#Usos

Um dos exemplos mais conhecidos do uso de pilhas é a call stack (pilha de chamadas) em um programa em execução. Quando um programa chama funções ou métodos, a ordem de execução segue o princípio da pilha, com cada chamada sendo empilhada e executada de acordo com essa estrutura.

Outro exemplo cotidiano que utiliza pilhas é o mecanismo de "voltar" e "avançar" páginas nos navegadores (geralmente representado pelas setas para a esquerda e direita). À medida que navegamos, os endereços das páginas visitadas são empilhados, e quando usamos a função "voltar", o último endereço visitado (o que está no topo da pilha) é o primeiro a ser exibido novamente.
