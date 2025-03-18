import ctypes

# Exemplo 1: Usando listas (alocação dinâmica implícita)
n = 5
lista_dinamica = [i for i in range(n)]  # Python aloca memória automaticamente
print("Lista Dinâmica:", lista_dinamica)

# Exemplo 2: Usando ctypes para alocação manual
tamanho = 5
array_c = (ctypes.c_int * tamanho)()  # Aloca memória para um array de 5 inteiros

# Preenchendo o array
for i in range(tamanho):
    array_c[i] = i * 10

print("Array dinâmico alocado manualmente:", [array_c[i] for i in range(tamanho)])
