def buscar_encomenda(codigo, lista_encomendas): for encomenda in lista_encomendas: if encomenda["codigo"] == codigo: return encomenda return None 
