'''exemplificando como um código sem tratamento de estrutura de
 dados pode ser menos performático que um código com o tratamento correto.'''

import time

# Exemplo sem uso eficiente de estrutura de dados
def busca_sem_estrutura(lista, produto):
    for item in lista:
        if item == produto:
            return True
    return False

# Exemplo usando dicionário (estrutura otimizada para buscas)
def busca_com_estrutura(inventario, produto):
    return produto in inventario

# Criando um inventário grande (lista de produtos)
produtos = ["Produto " + str(i) for i in range(1, 1000000)]

# Testando tempo de busca em lista (O(n))
inicio = time.time()
busca_sem_estrutura(produtos, "Produto 999999")
fim = time.time()
print(f"Busca sem estrutura otimizada: {fim - inicio:.5f} segundos")

# Criando um dicionário como estrutura otimizada para buscas (O(1) em média)
inventario_dict = {f"Produto {i}": i for i in range(1, 1000000)}

# Testando tempo de busca em dicionário (O(1) em média)
inicio = time.time()
busca_com_estrutura(inventario_dict, "Produto 999999")
fim = time.time()
print(f"Busca com estrutura otimizada: {fim - inicio:.5f} segundos")
