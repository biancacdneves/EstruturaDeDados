import pytest from algoritmos.bubble_sort import bubble_sort from algoritmos.shell_sort import shell_sort from algoritmos.merge_sort import merge_sort from algoritmos.quick_sort import quick_sort 

data = [ {"status": "B", "data": "2025-01-02"}, {"status": "C", "data": "2025-01-03"}, {"status": "A", "data": "2025-01-01"} ] 

@pytest.mark.parametrize("func", [bubble_sort, shell_sort, merge_sort, quick_sort]) def test_sorting(func): entrada = data[:] resultado = func(entrada, chave="data") datas = [item["data"] for item in resultado] assert datas == sorted(datas) 
