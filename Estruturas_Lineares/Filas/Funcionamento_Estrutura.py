'''exemplificando o funcionamento da estrutura de dados.'''

class FilaDeCinema:
    def __init__(self):
        self.fila = []

    # Adiciona uma pessoa à fila (entrarNaFila)
    def entrar_na_fila(self, pessoa):
        self.fila.append(pessoa)
        print(f"{pessoa} entrou na fila do cinema.")

    # Remove e retorna a primeira pessoa da fila (atenderCliente)
    def atender_cliente(self):
        if self.esta_vazia():
            print("A fila está vazia. Nenhuma pessoa para entrar.")
            return None
        pessoa_atendida = self.fila.pop(0)
        print(f"{pessoa_atendida} entrou na sala de cinema.")
        return pessoa_atendida

    # Consulta a próxima pessoa da fila (proximoCliente)
    def proximo_cliente(self):
        if self.esta_vazia():
            print("A fila está vazia.")
            return None
        print(f"Próximo a entrar: {self.fila[0]}")
        return self.fila[0]

    # Verifica se a fila está vazia
    def esta_vazia(self):
        return len(self.fila) == 0

    # Retorna o tamanho da fila
    def tamanho_da_fila(self):
        print(f"Total de pessoas na fila: {len(self.fila)}")
        return len(self.fila)

    # Exibe o estado atual da fila
    def mostrar_fila(self):
        print("Fila atual:", self.fila)


# Exemplo de uso
fila_cinema = FilaDeCinema()

# Pessoas chegando na fila
fila_cinema.entrar_na_fila("Pessoa 1")
fila_cinema.entrar_na_fila("Pessoa 2")
fila_cinema.entrar_na_fila("Pessoa 3")

# Consultar próxima pessoa
fila_cinema.proximo_cliente()

# Atender uma pessoa
fila_cinema.atender_cliente()

# Mostrar fila atual
fila_cinema.mostrar_fila()

# Atender mais pessoas
fila_cinema.atender_cliente()
fila_cinema.atender_cliente()

# Tentar atender quando a fila está vazia
fila_cinema.atender_cliente()

# Checar o tamanho da fila
fila_cinema.tamanho_da_fila()
