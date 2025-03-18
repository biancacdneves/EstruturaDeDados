'''exemplificando o funcionamento da estrutura de dados.'''
class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = [
            {"tarefa": "Lavar a louça", "prioridade": 3, "feito": False},
            {"tarefa": "Arrumar o quarto", "prioridade": 1, "feito": False},
            {"tarefa": "Limpar o banheiro", "prioridade": 2, "feito": False},
        ]
    
    # Função para adicionar uma nova tarefa
    def adicionar_tarefa(self, tarefa, prioridade):
        self.tarefas.append({"tarefa": tarefa, "prioridade": prioridade, "feito": False})
        print(f"Tarefa \"{tarefa}\" adicionada.")

    # Função para remover uma tarefa concluída
    def remover_tarefa(self, tarefa):
        tarefa_encontrada = next((t for t in self.tarefas if t["tarefa"] == tarefa), None)
        if tarefa_encontrada:
            self.tarefas.remove(tarefa_encontrada)
            print(f"Tarefa \"{tarefa}\" removida.")
        else:
            print(f"Tarefa \"{tarefa}\" não encontrada.")
    
    # Função para marcar uma tarefa como feita
    def marcar_tarefa_como_feita(self, tarefa):
        tarefa_encontrada = next((t for t in self.tarefas if t["tarefa"] == tarefa), None)
        if tarefa_encontrada:
            tarefa_encontrada["feito"] = True
            print(f"Tarefa \"{tarefa}\" marcada como feita.")
        else:
            print(f"Tarefa \"{tarefa}\" não encontrada.")
    
    # Função para listar tarefas pendentes
    def listar_tarefas_pendentes(self):
        print("Tarefas Pendentes:")
        for t in self.tarefas:
            if not t["feito"]:
                print(f"- {t['tarefa']}")
    
    # Função para ordenar tarefas por prioridade
    def ordenar_tarefas_por_prioridade(self):
        self.tarefas.sort(key=lambda t: t["prioridade"])
        print("Tarefas ordenadas por prioridade:")
        for t in self.tarefas:
            print(f"- {t['tarefa']} (Prioridade: {t['prioridade']})")
    
    # Função para listar todas as tarefas
    def listar_tarefas(self):
        print("Todas as Tarefas:")
        for t in self.tarefas:
            status = "Feita" if t["feito"] else "Pendente"
            print(f"- {t['tarefa']} (Prioridade: {t['prioridade']}, Status: {status})")


# Exemplo de uso das funções
gerenciador = GerenciadorDeTarefas()

# Listar todas as tarefas
gerenciador.listar_tarefas()

# Adicionar uma nova tarefa
gerenciador.adicionar_tarefa("Passar roupa", 2)

# Marcar uma tarefa como feita
gerenciador.marcar_tarefa_como_feita("Arrumar o quarto")

# Listar tarefas pendentes
gerenciador.listar_tarefas_pendentes()

# Remover uma tarefa
gerenciador.remover_tarefa("Lavar a louça")

# Ordenar tarefas por prioridade
gerenciador.ordenar_tarefas_por_prioridade()

# Listar todas as tarefas novamente
gerenciador.listar_tarefas()
