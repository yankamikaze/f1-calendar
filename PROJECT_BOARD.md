# 🏎️ F1 Calendar — Quadro do Projeto

## 📌 Epics
- **[API] Integração OpenF1** (Em andamento)

---

## 🏃 Sprint Atual: Sprint 3 — Conexão de Sessões e Investigação de Resultados
**Objetivo da Sprint:** Estruturar a busca de sessões de um Grande Prêmio e investigar os endpoints de resultados da OpenF1.

### Stories em Andamento / Planejamento:
- [ ] **F1-4 — [API] Buscar sessões do Grande Prêmio**
  - **Descrição:** Como usuário, quero consultar as sessões de um evento/meeting específico para saber os horários e tipos de treino/corrida.
  - **Subtarefas:**
    - [ ] Identificar parâmetros do endpoint `/sessions` na OpenF1
    - [ ] Implementar função `listar_sessoes(meeting_key)` em `openf1.py`
    - [ ] Tratar e filtrar os campos essenciais da sessão
    - [ ] Testar integração com `main.py`

- [ ] **F1-5 — [API] Buscar resultados das sessões**
  - **Descrição:** Como usuário, quero visualizar os resultados das sessões para acompanhar o desempenho dos pilotos.
  - **Subtarefas:**
    - [ ] Identificar endpoint de resultados na OpenF1
    - [ ] Implementar consulta aos resultados
    - [ ] Tratar os dados retornados
    - [ ] Tratar erros da API
    - [ ] Testar a função com uma sessão real

- [ ] **F1-6 — [API] Buscar canais de transmissão**
  - **Descrição:** Investigar viabilidade e fontes para exibição de canais de transmissão.

---

## ✅ Histórico de Sprints
- **Sprint 1 (Concluída):** Configuração inicial, estrutura do projeto e criação do repositório Git.
- **Sprint 2 (Concluída/Em validação):** Implementação de `listar_corridas(ano)` com tratamento de erros HTTP e filtro de campos do `/meetings`.