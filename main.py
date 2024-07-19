# Função principal
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    resposta = {
        'nome': 'API não oficial de cargos do DODFe',
        'autor': 'Matheus Fernandes <matheus@mail.matheuslemos.com>'
    }
    return resposta

@app.get('/api/v1/cargos/{ano}/{mes}')
def get_cargos(ano : int, mes : int):
    return {
        'mes': mes,
        'ano': ano
    }


