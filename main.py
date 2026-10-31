from fastapi import FastAPI


app = FastAPI()
pessoas = []

@app.get("/")
def root():
    return {"mensagem": "Olá, mundo!"
    }

@app.get("/pessoas")
def listar_pessoas ():
    return pessoas

@app.post("/pessoas")
def cadastrar_pessoas(pessoa: dict):
    pessoas.append(pessoa)
    return pessoa