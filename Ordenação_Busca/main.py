import json from busca import buscar_encomenda from algoritmos.merge_sort import merge_sort 

Carrega os dados de encomendas 

def carregar_encomendas(caminho="encomendas.json"): with open(caminho, "r") as f: return json.load(f) 

Exibe o histórico ordenado 

def exibir_historico(historico): for evento in historico: print(f"{evento['data']} - {evento['status']}") 

if name == "main": encomendas = carregar_encomendas() codigo = input("Digite o código de rastreamento: ") encomenda = buscar_encomenda(codigo, encomendas) 

if encomenda: 
    print(f"\nHistórico da encomenda {codigo}:") 
    historico_ordenado = merge_sort(encomenda["historico"], chave="data", reverso=True) 
    exibir_historico(historico_ordenado) 
else: 
    print("Encomenda não encontrada.") 
