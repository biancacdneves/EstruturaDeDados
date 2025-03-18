Problema Prático: Gerenciamento de Pedidos em um Restaurante
Descrição do Problema
Em um restaurante, vários clientes fazem pedidos ao longo do dia. Cada pedido deve ser processado na ordem em que é recebido, considerando que o tempo de preparo pode variar para cada um. O desafio é garantir que um pedido posterior não seja atendido antes de um anterior, mantendo a ordem de chegada.

Para resolver esse problema, a solução ideal é utilizar uma fila. Com essa estrutura de dados, o restaurante pode organizar os pedidos de maneira que o primeiro pedido a chegar seja o primeiro a ser processado e entregue, seguindo o princípio FIFO (First-In, First-Out), ou seja, o pedido mais antigo é sempre atendido primeiro.

Como a Estrutura de Dados Fila Resolve o Problema
Adição de Pedidos (Enfileirar): Cada novo pedido é inserido no final da fila, aguardando ser processado.
Processamento de Pedidos (Desenfileirar): O pedido que está no início da fila é o primeiro a ser processado e entregue ao cliente.
Verificação de Fila Vazia: Quando todos os pedidos são atendidos, o sistema pode verificar se a fila está vazia, garantindo que não há mais pedidos a serem processados.
Ao usar uma fila, o restaurante pode garantir que os pedidos serão atendidos na ordem correta, otimizando o atendimento e evitando confusão. Isso torna o gerenciamento de pedidos mais eficiente e organizado.
