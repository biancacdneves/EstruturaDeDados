# 📌 Variáveis, Tipos de Dados e Alocação de Memória

## 🔹 Introdução
Variáveis e tipos de dados são conceitos fundamentais na programação. Toda variável ocupa um espaço na memória e seu tamanho depende do tipo de dado que ela armazena. Compreender como a alocação de memória funciona ajuda a escrever códigos mais eficientes.

---

## 🧠 O que é uma Variável?
Uma variável é um espaço na memória que armazena um valor e pode ser alterado durante a execução do programa. Cada variável possui:
- **Nome**: Identificador usado para acessar o valor.
- **Tipo de dado**: Define o formato e tamanho do dado armazenado.
- **Valor**: O dado armazenado na variável.

Exemplo em Python:
```python
idade = 25  # "idade" é uma variável do tipo inteiro (int)
```

Exemplo em C:
```c
int idade = 25;  // "idade" ocupa 4 bytes na memória
```

---

## 🔹 Tipos de Dados e Alocação de Memória
Os tipos de dados determinam o espaço alocado na memória para armazenar valores. Cada linguagem tem sua forma de gerenciar isso.

### 🔹 Tipos de Dados em C e Sua Memória
| Tipo de Dado | Tamanho Aproximado |
|-------------|------------------|
| `char`      | 1 byte           |
| `int`       | 4 bytes          |
| `float`     | 4 bytes          |
| `double`    | 8 bytes          |

Exemplo:
```c
char letra = 'A';   // Ocupa 1 byte
int numero = 100;    // Ocupa 4 bytes
float preco = 10.5;  // Ocupa 4 bytes
```

### 🔹 Tipos de Dados em Python
Em Python, os tipos de dados são gerenciados dinamicamente e ocupam mais memória do que em C devido ao gerenciamento interno.

| Tipo de Dado | Exemplo |
|-------------|--------|
| `int`       | `idade = 25` |
| `float`     | `altura = 1.75` |
| `str`       | `nome = "Alice"` |
| `bool`      | `ativo = True` |

Python aloca memória dinamicamente e faz gerenciamento automático de memória com o **Garbage Collector**.

---

## 🔥 Como a Alocação de Memória Funciona?
A memória de um programa é dividida em:
1. **Stack (Pilha)**: Armazena variáveis locais e tem alocação automática.
2. **Heap**: Armazena variáveis alocadas dinamicamente com `malloc` (C) ou listas/objetos (Python).

### 📌 Exemplo de Alocação Estática vs Dinâmica em C
```c
int x = 10;  // Alocação estática (Stack)
int *ptr = (int *) malloc(sizeof(int)); // Alocação dinâmica (Heap)
```

### 📌 Alocação Dinâmica em Python
```python
lista = [1, 2, 3, 4]  # Lista alocada dinamicamente na Heap
```

---

## 🚀 Conclusão
- **Variáveis ocupam espaço na memória**, e seu tamanho depende do tipo de dado.
- Em linguagens como **C, a alocação é manual**, enquanto em **Python é automática**.
- **Entender alocação de memória melhora a eficiência do programa** e evita desperdício de recursos.




