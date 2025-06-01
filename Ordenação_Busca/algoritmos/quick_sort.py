def quick_sort(lista, chave=None, reverso=False): if len(lista) <= 1: return lista 

def get_value(x): 
    return x[chave] if chave else x 
 
pivo = get_value(lista[0]) 
iguais = [x for x in lista if get_value(x) == pivo] 
menores = [x for x in lista if get_value(x) < pivo] if not reverso else [x for x in lista if get_value(x) > pivo] 
maiores = [x for x in lista if get_value(x) > pivo] if not reverso else [x for x in lista if get_value(x) < pivo] 
 
return quick_sort(menores, chave, reverso) + iguais + quick_sort(maiores, chave, reverso) 
  
