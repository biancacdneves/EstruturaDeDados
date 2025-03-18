Problema Prático: Gerenciamento de Pedidos em um Restaurante
Descrição do Problema
Em um restaurante, vários clientes fazem pedidos ao longo do dia. Cada pedido deve ser processado na ordem em que é recebido, considerando que o tempo de preparo pode variar para cada um. O desafio é garantir que um pedido posterior não seja atendido antes de um anterior, mantendo a ordem de chegada.

Para resolver esse problema, a solução ideal é utilizar uma fila. Com essa estrutura de dados, o restaurante pode organizar os pedidos de maneira que o primeiro pedido a chegar seja o primeiro a ser processado e entregue, seguindo o princípio FIFO (First-In, First-Out), ou seja, o pedido mais antigo é sempre atendido primeiro.

Como a Estrutura de Dados Fila Resolve o Problema
Adição de Pedidos (Enfileirar): Cada novo pedido é inserido no final da fila, aguardando ser processado.
Processamento de Pedidos (Desenfileirar): O pedido que está no início da fila é o primeiro a ser processado e entregue ao cliente.
Verificação de Fila Vazia: Quando todos os pedidos são atendidos, o sistema pode verificar se a fila está vazia, garantindo que não há mais pedidos a serem processados.
Ao usar uma fila, o restaurante pode garantir que os pedidos serão atendidos na ordem correta, otimizando o atendimento e evitando confusão. Isso torna o gerenciamento de pedidos mais eficiente e organizado.

# Sistema de Gerenciamento de Pedidos em um Restaurante

## Descrição do Problema

Este problema envolve a simulação de um sistema de gerenciamento de pedidos em um restaurante. O restaurante deve garantir que os pedidos sejam atendidos na ordem de chegada dos clientes, ou seja, o primeiro pedido a entrar na fila deve ser o primeiro a ser atendido.

O sistema deve ser capaz de:
- Adicionar novos pedidos à fila.
- Processar os pedidos na ordem de chegada.
- Verificar se a fila está vazia quando não houver mais pedidos para atender.

Resolução do Problema:

A estrutura de dados **Fila (Queue)** é ideal para este tipo de problema. A fila segue o princípio FIFO e garante que o primeiro pedido a ser feito será o primeiro a ser atendido.

Funcionamento do Sistema:

1. **Enfileirar (Adicionar Pedido)**: Quando um cliente faz um pedido, ele é adicionado ao final da fila de pedidos.
2. **Desenfileirar (Processar Pedido)**: O pedido no início da fila é o primeiro a ser processado e entregue ao cliente.
3. **Verificação de Fila Vazia**: O sistema pode verificar se a fila está vazia para saber quando não há mais pedidos para processar.

 Estrutura de Dados Usada:
 

- **Fila (Queue)**: Usada para organizar os pedidos na ordem de chegada.
  - **Operações**:
    - `enqueue(pedido)`: Adiciona um pedido ao final da fila.
    - `dequeue()`: Remove o pedido que está no início da fila e o processa.

Implementação:


A implementação do problema pode ser encontrada no arquivo `sistema_pedidos.py`.
