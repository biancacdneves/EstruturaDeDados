# Explicando o funcionamento da estrutura de dados em fila,

📌 Estrutura de Dados: 

Fila (Queue)

🔹 Introdução

A fila é uma estrutura de dados linear que segue o princípio FIFO (First In, First Out), ou seja, o primeiro a entrar é o primeiro a sair. Essa organização é muito comum no cotidiano, como em filas de banco, atendimentos médicos ou sistemas de impressão, onde o primeiro a chegar é o primeiro a ser atendido.

🔸 Princípio FIFO

A ideia básica é que os elementos são adicionados no final da fila e removidos do início, o que garante que os dados sejam processados de forma ordenada.

Exemplo no mundo real: Imagine uma fila em uma bilheteira. A pessoa que chegou primeiro será atendida antes da que chegou depois e ficou atrás na fila.

Da mesma forma, a estrutura de dados fila funciona exatamente com esse conceito de ordem de chegada.

🧠 Operações em Fila

As principais operações realizadas em uma fila são:

🔹 Enfileirar (Enqueue)

Essa operação adiciona um novo elemento ao final da fila. Em outras palavras, ela insere um item na última posição disponível da fila.

Exemplo:

Fila inicial: [10, 20, 30]
Operação: Enfileirar 40
Fila após a operação: [10, 20, 30, 40]

🔹 Desenfileirar (Dequeue)

A operação desenfileirar remove o primeiro elemento da fila, ou seja, o elemento que foi inserido primeiro. Após essa operação, a fila é reorganizada e o próximo elemento se torna o "início" da fila.

Exemplo:

Fila inicial: [10, 20, 30, 40]
Operação: Desenfileirar (remover o 10)
Fila após a operação: [20, 30, 40]
