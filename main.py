# Função principal
from fastapi import Depends, FastAPI, APIRouter
from utils.dodf import parse_data
from utils.auth import get_user
from utils.db import engine
from utils.models import Base
import json

Base.metadata.create_all(bind=engine)

app = FastAPI()
#router = APIRouter()

@app.get('/')
def read_root():
    resposta = {
        'nome': 'API não oficial de cargos do DODFe',
        'autor': 'Matheus Fernandes <matheus@mail.matheuslemos.com>',
        'docs': '/docs'
    }
    return resposta

@app.get('/api/v1/cargos/{ano}/{mes}/{dia}')
def get_cargos(ano : str, mes : str, dia: str, user : dict = Depends(get_user)):
    try:
        # Abre o arquivo do ano e mês correspondente
        conteudo = {}
        data = {}
        nome_arquivo = f'diarios/{ano}/{mes}/{dia}.json'
        with open(nome_arquivo, "r") as file:
            data = json.load(file)

            # Realiza o parse do arquivo e retorna nomeacoes e exoneracoes
            resultado = parse_data(data)
            return resultado
    except FileNotFoundError as e:
        resultado = {
            'codigo' : 404,
            'mensagem': 'Diário não encontrado para a data especificada.'
        }
        return resultado
    except Exception as e:
        print(str(e))
        resultado = {
            'codigo' : 500,
            'mensagem': str(e)
        }
        return resultado



