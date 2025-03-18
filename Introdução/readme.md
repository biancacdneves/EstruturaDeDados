📌 Estruturas de Dados Lineares: Listas, Pilhas e Filas

🔹 Contribuidores

▪ Bianca Neves
▪ Davi Mendes
▪ Enzo Coletto

🔹 Introdução:

Estruturas de dados lineares são fundamentais para a organização e manipulação de dados em programação. Elas permitem armazenar dados de maneira ordenada e realizar operações como inserção, remoção, acesso e busca de forma eficiente. Três das estruturas lineares mais comuns são:

Listas: Sequências ordenadas de elementos.
Pilhas (Stacks): Seguem o princípio LIFO (Last In, First Out).
Filas (Queues): Seguem o princípio FIFO (First In, First Out).
Essas estruturas de dados são utilizadas em uma ampla gama de algoritmos e aplicações, desde o gerenciamento de memória até sistemas de navegação e pesquisa de dados.

🧠 O que são Estruturas de Dados Lineares?


Estruturas de dados lineares organizam os elementos de maneira sequencial, ou seja, cada elemento possui um único sucessor (exceto o último) e um único predecessor (exceto o primeiro). O principal objetivo é garantir que os dados sejam acessados e manipulados de forma ordenada e eficiente.

🔹 Tipos de Estruturas Lineares:


Listas: Armazenam elementos de forma sequencial, com a possibilidade de acesso aleatório aos elementos.
Pilhas: Seguem o princípio LIFO, onde o último elemento inserido é o primeiro a ser removido.
Filas: Seguem o princípio FIFO, onde o primeiro elemento inserido é o primeiro a ser removido.

🔹 Listas: Sequências Ordenadas

As listas são coleções ordenadas de elementos, onde cada item pode ser acessado por seu índice. Elas podem ser implementadas como arrays ou listas encadeadas, dependendo da linguagem e da necessidade.

🔸 Principais Operações em Listas

Inserção: Adicionar um elemento à lista.
Remoção: Remover um elemento da lista.
Acesso: Acessar um elemento pelo índice.
Busca: Procurar por um elemento na lista.
Exemplo de Lista em Python:
python
Copiar
# Criando uma lista
lista = [1, 2, 3, 4]

# Inserindo um elemento no final
lista.append(5)

# Removendo um elemento específico
lista.remove(3)

# Acessando o elemento no índice 2
print(lista[2])  # Output: 4

# Verificando se um elemento está na lista
print(5 in lista)  # Output: True
🔹 Pilhas: Último a Entrar, Primeiro a Sair (LIFO)

A pilha é uma estrutura de dados que segue o princípio LIFO (Last In, First Out), ou seja, o último elemento inserido é o primeiro a ser removido. As pilhas são amplamente utilizadas em algoritmos de recursão e no gerenciamento de chamadas de funções.

🔸 Principais Operações em Pilhas


Push: Inserir um elemento no topo da pilha.

Pop: Remover o elemento do topo da pilha.

Topo: Acessar o topo da pilha sem remover.

Vazia: Verificar se a pilha está vazia.

Exemplo de Pilha em Python:


python
Copiar
# Criando uma pilha
pilha = [1, 2, 3]

# Push: inserindo no topo
pilha.append(4)

# Pop: removendo o topo
topo = pilha.pop()

# Acessando o topo
print(pilha[-1])  # Output: 3

# Verificando se a pilha está vazia
print(len(pilha) == 0)  # Output: False

🔹 Filas: Primeiro a Entrar, Primeiro a Sair (FIFO)
A fila segue o princípio FIFO (First In, First Out), onde o primeiro elemento inserido é o primeiro a ser removido. As filas são utilizadas em sistemas de gerenciamento de tarefas, como em impressoras ou processos de execução de programas.

🔸 Principais Operações em Filas
Enqueue: Inserir um elemento no final da fila.
Dequeue: Remover um elemento do início da fila.
Frente: Acessar o primeiro elemento da fila.
Vazia: Verificar se a fila está vazia.
Exemplo de Fila em Python:
python
Copiar
from collections import deque

# Criando uma fila
fila = deque([1, 2, 3])

# Enqueue: inserindo no final
fila.append(4)

# Dequeue: removendo do início
primeiro = fila.popleft()

# Acessando o primeiro elemento
print(fila[0])  # Output: 2

# Verificando se a fila está vazia
print(len(fila) == 0)  # Output: False

🚀 Conclusão
Listas são usadas para armazenar sequências de dados ordenados, com acesso direto aos elementos.
Pilhas seguem a ordem LIFO, sendo úteis para algoritmos que precisam de operações de última entrada, primeira saída.
Filas seguem a ordem FIFO, comumente usadas em sistemas de gerenciamento de tarefas e recursos.
Essas estruturas são essenciais para a manipulação eficiente de dados e podem ser adaptadas conforme as necessidades do problema que está sendo resolvido.
