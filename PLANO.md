# 📚 Plano de Estudo: API de Cadastro de Pessoas com FastAPI

> Este arquivo guarda tudo que foi combinado na conversa de planejamento (28/10/2026).
> Serve para continuar o estudo em qualquer computador, de onde parou.

---

## 🎯 Objetivo

Aprender a construir uma **API REST do zero**, passo a passo, construindo uma **API de cadastro de pessoas**.

O foco principal é **aprender**. O repositório também serve como **material de consulta** e como **projeto para mostrar no GitHub**.

## 🧑‍🏫 Como vamos trabalhar

- **Estilo videoaula**: o professor (Claude) explica **como a API funciona por dentro** (cliente/servidor, HTTP, portas, o que o framework faz), não só a sintaxe do Python
- **Um passo por vez**: explica o conceito, o aluno faz e conta o resultado
- **Nada de código pronto para copiar.** O professor explica, desafia o aluno a escrever a peça e depois revisa
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
- [x] `.gitignore` criado pelo aluno (`.venv/`, `__pycache__/`, `*.pyc`)
- [x] Aula 2: ambiente virtual (`python -m venv .venv` + ativar com `.\.venv\Scripts\Activate.ps1`), FastAPI instalado (`pip install "fastapi[standard]"`) e `requirements.txt` com `fastapi[standard]`
- [x] **Aula 3: primeira rota** (concluída em 31/10/2026)
  - [x] Teoria: servidor fica esperando requisições, endereço `127.0.0.1` + porta `8000`, caminho da requisição (navegador → Uvicorn → FastAPI → resposta), papel do Uvicorn x FastAPI (ASGI), o objeto `app`
  - [x] Peça 1: `from fastapi import FastAPI`
  - [x] Peça 2: `app = FastAPI()` (classe é o molde, os parênteses constroem a instância, como `list()`)
  - [x] Teoria: decorators montam a "tabela de rotas" do `app`, a função da rota retorna um dicionário que vira JSON com status 200
  - [x] Peça 3: `@app.get("/")` + função `root()` retornando `{"mensagem": "Olá, mundo!"}`
  - [x] Servidor ligado com `fastapi dev main.py` (recarrega sozinho ao salvar), testado em `http://127.0.0.1:8000` e em `/docs`
  - 🐛 **Erro que apareceu:** o dicionário ficou numa linha e o `return` sozinho em outra. A função devolveu `None`, que virou `null` no JSON, com status `200 OK`. Lição: o `return` devolve o que está **do lado dele**, e código sem erro não quer dizer código certo
- [ ] Anotação da Aula 3 em `aulas/03-primeira-rota.md` (o aluno escreve, com as próprias palavras)
- [ ] **👉 Próximo passo, Aula 4:** listar e cadastrar pessoas (`GET /pessoas` e `POST /pessoas`), guardando numa lista Python na memória

### Ao voltar a estudar

1. Ative a `.venv` (aparece `(.venv)` no terminal):
   - **Linux/macOS:** `source .venv/bin/activate`
   - **Windows (PowerShell):** `.\.venv\Scripts\Activate.ps1`
2. Em outro computador, crie a `.venv` antes (`python -m venv .venv`), ative e rode `pip install -r requirements.txt`
3. Ligue o servidor com `fastapi dev main.py`

### Como continuar em outro computador

```powershell
git clone https://github.com/jvitorsantoss/estudo-api-python.git
cd estudo-api-python
claude
```

Depois diga ao Claude: *"leia o PLANO.md e vamos continuar de onde paramos"*.
