# explicando o funcionamento da estrutura de dados em fila,

A fila possui uma estrutura similar à pilha, mas com uma diferença conceitual fundamental: ela segue o princípio FIFO - First In, First Out, ou seja, "o primeiro a entrar, é o último a sair".

Um exemplo comum seria uma fila em uma bilheteira. A pessoa que chegou primeiro será atendida antes da que chegou depois e ficou atrás na fila. A estrutura de dados fila segue exatamente esse mesmo conceito.

Dessa forma, as operações que podem ser realizadas em uma fila são apenas duas: 1) adicionar um elemento no final da fila e 2) remover um elemento do início da fila.

#As principais operações da estrutura de dados lineares são:

Enfileirar (Enqueue):
Neste caso, esta operação adiciona um novo elemento no final da fila. Em outras palavras, insere um item na última posição.
Exemplo:
Fila inicial: [10, 20, 30]
Operação: Enfileirar 40.
Fila após a operação: [10, 20, 30, 40]

Desenfileirar (Dequeue):
Neste caso, esta operação remove o elemento da frente da fila (ou seja, o primeiro elemento a ser inserido). A fila é ajustada, e o próximo elemento se torna o "início" da fila.
Exemplo:
Fila inicial: [10, 20, 30, 40]
Operação: Desenfileirar (remover o 10).
Fila após a operação: [20, 30, 40]
