from fastapi import FastAPI


app = FastAPI()
pessoa = []

@app.get("/")
def root():
    return {"mensagem": "Olá, mundo!"
    }

@app.get("/pessoas")
def listar_pessoas ():
    return pessoa