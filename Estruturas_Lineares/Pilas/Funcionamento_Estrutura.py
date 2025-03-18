'''exemplificando o funcionamento da estrutura de dados.'''

class Pilha:
    def __init__(self):
        self.itens = []
    
    # Adicionar elemento ao topo da pilha
    def empilhar(self, elemento):
        self.itens.append(elemento)
    
    # Remover elemento do topo da pilha
    def desempilhar(self):
        if self.esta_vazia():
            print("A pilha está vazia!")
            return None
        return self.itens.pop()
    
    # Ver o elemento no topo sem remover
    def topo(self):
        return None if self.esta_vazia() else self.itens[-1]
    
    # Verificar se a pilha está vazia
    def esta_vazia(self):
        return len(self.itens) == 0
    
    # Retornar o tamanho da pilha
    def tamanho(self):
        return len(self.itens)


class GerenciadorDeLimpeza:
    def __init__(self):
        self.acao_atual = ""
        self.pilha_undo = Pilha()  # Pilha para ações desfeitas
        self.pilha_redo = Pilha()  # Pilha para ações refeitas
    
    # Função para realizar uma nova ação de limpeza
    def realizar_acao(self, acao):
        self.pilha_undo.empilhar(self.acao_atual)  # Salva o estado anterior
        self.acao_atual = acao
        self.pilha_redo = Pilha()  # Limpa a pilha de redo ao realizar uma nova ação
        print(f"Ação realizada: {self.acao_atual}")
    
    # Função para desfazer a última ação
    def desfazer(self):
        if not self.pilha_undo.esta_vazia():
            self.pilha_redo.empilhar(self.acao_atual)  # Salva o estado atual antes de desfazer
            self.acao_atual = self.pilha_undo.desempilhar()
            print(f"Ação desfeita: {self.acao_atual}")
        else:
            print("Nada para desfazer.")
    
    # Função para refazer a última ação
    def refazer(self):
        if not self.pilha_redo.esta_vazia():
            self.pilha_undo.empilhar(self.acao_atual)  # Salva o estado antes de refazer
            self.acao_atual = self.pilha_redo.desempilhar()
            print(f"Ação refeita: {self.acao_atual}")
        else:
            print("Nada para refazer.")


# Exemplo de uso
gerenciador = GerenciadorDeLimpeza()

gerenciador.realizar_acao("Limpar o chão")  # Ação realizada: Limpar o chão
gerenciador.realizar_acao("Lavar os pratos")  # Ação realizada: Lavar os pratos
gerenciador.desfazer()  # Ação desfeita: Limpar o chão
gerenciador.desfazer()  # Ação desfeita: 
gerenciador.refazer()  # Ação refeita: Limpar o chão
gerenciador.refazer()  # Ação refeita: Lavar os pratos
gerenciador.refazer()  # Nada para refazer.
