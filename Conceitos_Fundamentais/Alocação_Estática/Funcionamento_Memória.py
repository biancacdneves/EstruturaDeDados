class AlocacaoEstatica:
    def __init__(self, tamanho):
        # Aloca um "vetor" de tamanho fixo
        self.memoria = [None] * tamanho  # Inicializa com valores None, ocupando a memória de forma estática
    
    def alocar(self, indice, valor):
        if 0 <= indice < len(self.memoria):
            self.memoria[indice] = valor
        else:
            print("Índice fora dos limites da memória alocada.")

    def mostrar_memoria(self):
        print("Estado da memória:", self.memoria)

# Criando um objeto de alocação estática com tamanho 5
alocacao = AlocacaoEstatica(5)

# Alocando valores nas posições específicas
alocacao.alocar(0, 10)
alocacao.alocar(2, 20)
alocacao.alocar(4, 30)

# Mostrando o estado da memória
alocacao.mostrar_memoria()
