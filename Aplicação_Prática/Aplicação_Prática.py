class Fila:
    def __init__(self):
        # A fila é inicializada como uma lista vazia
        self.fila = []

    # Adiciona um pedido à fila
    def adicionar_pedido(self, pedido):
        self.fila.append(pedido)
        print(f"Pedido '{pedido}' adicionado à fila.")

    # Processa o primeiro pedido da fila
    def processar_pedido(self):
        if self.esta_vazia():
            print("Não há pedidos na fila para processar.")
            return None
        pedido_processado = self.fila.pop(0)  # Remove o primeiro pedido
        print(f"Pedido '{pedido_processado}' foi processado e entregue ao cliente.")
        return pedido_processado

    # Verifica se a fila está vazia
    def esta_vazia(self):
        return len(self.fila) == 0

    # Exibe o estado atual da fila
    def mostrar_fila(self):
        if self.esta_vazia():
            print("A fila de pedidos está vazia.")
        else:
            print("Pedidos na fila:", self.fila)


# Simulação do sistema de gerenciamento de pedidos
def sistema_de_pedidos():
    fila_pedidos = Fila()

    # Pedidos chegando ao restaurante
    fila_pedidos.adicionar_pedido("Pedido 1: Pizza")
    fila_pedidos.adicionar_pedido("Pedido 2: Hambúrguer")
    fila_pedidos.adicionar_pedido("Pedido 3: Sushi")

    # Exibindo a fila de pedidos
    fila_pedidos.mostrar_fila()

    # Processando o primeiro pedido
    fila_pedidos.processar_pedido()

    # Exibindo a fila após o processamento do pedido
    fila_pedidos.mostrar_fila()

    # Processando os próximos pedidos
    fila_pedidos.processar_pedido()
    fila_pedidos.processar_pedido()

    # Tentando processar quando a fila está vazia
    fila_pedidos.processar_pedido()


# Executando o sistema de pedidos
sistema_de_pedidos()

