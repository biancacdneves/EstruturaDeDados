def merge_sort(lista, chave=None, reverso=False): if len(lista) <= 1: return lista 

def get_value(x): 
    return x[chave] if chave else x 
 
meio = len(lista) // 2 
esquerda = merge_sort(lista[:meio], chave, reverso) 
direita = merge_sort(lista[meio:], chave, reverso) 
 
resultado = [] 
i = j = 0 
 
while i < len(esquerda) and j < len(direita): 
    a = get_value(esquerda[i]) 
    b = get_value(direita[j]) 
    if (a < b and not reverso) or (a > b and reverso): 
        resultado.append(esquerda[i]) 
        i += 1 
    else: 
        resultado.append(direita[j]) 
        j += 1 
 
resultado.extend(esquerda[i:]) 
resultado.extend(direita[j:]) 
return resultado 
  
