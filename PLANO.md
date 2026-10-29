# 📚 Plano de Estudo: API de Cadastro de Pessoas com FastAPI

> Este arquivo guarda tudo que foi combinado na conversa de planejamento (28/10/2026).
> Serve para continuar o estudo em qualquer computador, de onde parou.

---

## 🎯 Objetivo

Aprender a construir uma **API REST do zero**, passo a passo, construindo uma **API de cadastro de pessoas**.

O foco principal é **aprender**. O repositório também serve como **material de consulta** e como **projeto para mostrar no GitHub**.

## 🧑‍🏫 Como vamos trabalhar

- **Um passo por vez**: o professor (Claude) explica o porquê, o aluno digita e conta o resultado
- **O aluno escreve o código.** O Claude revisa e corrige junto
- Sem explicação básica de terminal, só o que importa para a API
- **Cada passo concluído vira um commit** com mensagem clara
- Depois de cada aula, o aluno escreve uma anotação **com as próprias palavras** na pasta `aulas/`

## 🛠️ Tecnologias

| O quê | Escolha | Por quê |
|---|---|---|
| Linguagem | Python 3.14 | Escolha do aluno (nível médio) |
| Framework | FastAPI | Moderno, rápido, gera a documentação `/docs` sozinho |
| Servidor | Uvicorn (vem com `fastapi[standard]`) | Roda a API |
| Validação | Pydantic (vem com o FastAPI) | Garante que os dados recebidos estão certos |
| Versionamento | Git + GitHub | Salvar o progresso e montar portfólio |
| Banco de dados | SQLite (Aula 7), **biblioteca a decidir** | Ver abaixo |

## 📋 O que a API vai fazer

O recurso principal é a **pessoa**. Os campos são uma proposta inicial e podem mudar durante as aulas:

| Campo | Tipo | Obrigatório | Exemplo |
|---|---|---|---|
| `id` | número | gerado pela API | `3` |
| `nome` | texto | sim | `"Maria Silva"` |
| `idade` | número | sim | `28` |
| `email` | texto | não | `"maria@email.com"` |

### Rotas planejadas

| Método | Rota | O que faz |
|---|---|---|
| `POST` | `/pessoas` | ➕ Cadastrar uma pessoa |
| `GET` | `/pessoas` | 📋 Listar todas as pessoas |
| `GET` | `/pessoas/{id}` | 🔍 Buscar uma pessoa pelo ID |
| `PUT` | `/pessoas/{id}` | ✏️ Atualizar os dados de uma pessoa |
| `DELETE` | `/pessoas/{id}` | ❌ Remover uma pessoa |

## 🗺️ Trilha de aulas

1. **O que é uma API?** HTTP, métodos, JSON, status codes
2. **Ambiente virtual e instalação do FastAPI**
3. **Primeira rota**, o "Olá, mundo"
4. **Listar e cadastrar pessoas** (GET e POST), guardando numa lista Python, na memória
5. **Buscar, atualizar e remover** (GET por ID, PUT, DELETE) + erro 404 quando a pessoa não existe
6. **Validação de dados com Pydantic**: idade não pode ser negativa, nome não pode ser vazio...
7. **Salvando em banco de dados (SQLite)**: até aqui, se o servidor para, as pessoas cadastradas somem. Nesta aula elas passam a ficar salvas

**Ideias para depois da trilha:** testes automatizados, filtros (ex.: buscar por nome), usuários e login.

### Decisão em aberto: como acessar o SQLite (Aula 7)

Fica para decidir **quando chegar na Aula 7**, com o CRUD já funcionando na memória:

- **A) SQLModel** ⭐ *recomendação do professor*: do mesmo criador do FastAPI, quase não precisa escrever SQL e reaproveita os modelos Pydantic da Aula 6
- **B) SQLAlchemy puro**: o padrão do mercado, mas tem mais código repetido
- **C) sqlite3 com SQL à mão**: ensina SQL, mas dá muito trabalho manual

## 📁 Como o repositório vai ficar

```
estudo-api-python/
├── README.md         ← vitrine do projeto (a criar)
├── PLANO.md          ← este arquivo
├── aulas/            ← anotações do aluno, uma por aula
│   ├── 01-....md
│   └── ...
├── main.py           ← a API
└── .gitignore
```

Cada arquivo em `aulas/` traz: **o que** foi feito, **por que**, os **comandos** usados e os **erros** que apareceram e como foram resolvidos.

---

## 📍 Onde paramos

- [x] Aula 1: O que é uma API (HTTP, métodos, CRUD, status codes)
- [x] Planejamento do projeto (este arquivo)
- [x] Repositório no GitHub (público): https://github.com/jvitorsantoss/estudo-api-python
- [ ] **Próximo passo, Aula 2:** criar o ambiente virtual → `python -m venv .venv`

### Como continuar em outro computador

```powershell
git clone https://github.com/jvitorsantoss/estudo-api-python.git
cd estudo-api-python
claude
```

Depois diga ao Claude: *"leia o PLANO.md e vamos continuar de onde paramos"*.
