🚛 Sistema de Rastreamento Logístico com Busca e Ordenação

### 📌 Aplicação Prática

Este projeto demonstra o uso de estruturas de dados e algoritmos fundamentais (busca e ordenação) aplicados a um sistema de rastreamento de entregas e rotas logísticas. A proposta é desenvolver uma aplicação interativa via console, simulando funcionalidades reais de sistemas usados por empresas de transporte e logística.

---

### 🎯 Problema Prático Escolhido

*Rastreamento e Otimização de Rotas Logísticas*

O sistema permite que operadores logísticos e motoristas realizem as seguintes operações:

* Cadastro de centros de distribuição, rotas entre locais e entregas.
* Busca de melhores caminhos entre pontos (utilizando algoritmos como Dijkstra).
* Visualização de rotas ordenadas por tempo, distância ou custo.
* Listagem de entregas ordenadas por prioridade, data ou destino.
* Busca de entregas por código, destino ou status.

---

### 🛠 Estrutura de Dados Utilizada

* Arrays/Vetores para armazenar:

  * Locais de entrega e centros de distribuição.
  * Tabela de rotas entre locais (grafo com pesos).
  * Lista de entregas com dados como código, destino, prioridade e status.

* Algoritmos:

  * *Busca*: Dijkstra para encontrar a rota ótima entre dois pontos.
  * *Ordenação*: Bubble Sort/Insertion Sort aplicados a listas de entregas por múltiplos critérios.
💡 Justificativa

O uso de arrays com redimensionamento manual, somado à implementação explícita de algoritmos, reforça o entendimento de manipulação direta de dados, controle de complexidade e a sinergia entre ordenação e busca no contexto logístico.

---

 🚀 Funcionalidades Implementadas

 🗂 Cadastros

* cadastrarLocal(): Adiciona um centro de distribuição ou cidade.
* cadastrarRota(): Registra uma rota entre dois locais com tempo estimado, distância e custo.
* cadastrarEntrega(): Adiciona uma nova entrega ao sistema com informações como código, destino e prioridade.

 📡 Rastreamento e Consulta

* buscarMelhorRota(origem, destino, criterio): Utiliza o algoritmo de Dijkstra para buscar a melhor rota conforme o critério selecionado (tempo, distância ou custo).
* listarRotasOrdenadas(origem): Lista rotas a partir de um local, ordenadas por critério.
* listarEntregas(): Permite listar todas as entregas com ordenação por:

  * Prioridade
  * Data prevista de entrega
  * Destino

 🔎 Buscas

* Entregas por código
* Entregas com status pendente, entregue ou em rota
* Rotas disponíveis para determinado local
* Local por nome

 ❌ Remoções

* removerEntrega(codigo)
* removerLocal(nome): Remove um local e todas as rotas associadas a ele.

---

🧩 Exemplo de Uso

<b>=== MENU PRINCIPAL ===
1 - Cadastrar

2 - Rastrear

3 - Visualizar

4 - Remover

0 - Sair

Escolha: 1

--- Menu Cadastrar ---
1 - Cadastrar Local

2 - Cadastrar Rota entre Locais

3 - Cadastrar Entrega

0 - Voltar
Escolha: 1

Nome do Local: Centro SP
Tipo (Centro de Distribuição / Cidade): Centro de Distribuição
Local cadastrado com sucesso!

Escolha: 2
Origem: Centro SP

Destino: Cidade RJ

Distância (km): 450

Tempo estimado (h): 6

Custo (R$): 120.00

Rota registrada com sucesso!

Escolha: 3
Código da entrega: E123

Destino: Cidade RJ

Data prevista: 2025-06-05

Prioridade (1-Alta, 2-Média, 3-Baixa): 1

Entrega E123 registrada com sucesso!

Escolha: 2

--- Menu Rastrear ---
1 - Buscar melhor rota

2 - Listar entregas por prioridade

0 - Voltar

Escolha: 1

Origem: Centro SP

Destino: Cidade RJ

Critério (tempo / distância / custo): tempo

Melhor rota encontrada: Centro SP → Cidade RJ

Tempo estimado: 6h

Escolha: 3

--- Menu Visualizar ---
1 - Listar Entregas

2 - Buscar Entrega por Código

3 - Ver Rotas a partir de um Local

Escolha: 1

Critério de ordenação: prioridade

Entregas listadas com sucesso:

[E123] → Cidade RJ | Prioridade: Alta | Status: Pendente

Escolha: 4
Código da entrega: E123

Entrega E123 removida com sucesso.



---

📃 Considerações Finais

Este projeto reforça a sinergia entre algoritmos de *busca de caminho (ex: Dijkstra)* e *ordenadores (como Bubble Sort)* aplicados a um problema real. A interação entre esses algoritmos permite:

* Rastrear eficientemente a entrega com menor custo ou tempo.
* Priorizar tarefas de entrega conforme urgência e localização.
* Otimizar rotas a partir de dados armazenados manualmente em estruturas controladas.
