# Arquivo para acessar a API do dodf e parsear o resultado
import json
from bs4 import BeautifulSoup

def read_file(filename):
    # Read file .json on current folder and store on data dict
    data = {}
    with open(filename, "r") as file:
        data = json.load(file)

    return data

# Formata o resultado em uma lista de objetos com o formato:
# {"nome": "Nome", "matrícula": "12345", "simbolo": "CNE-05"}
#def monta_dicionario_exonerados(lista):
#    #print(lista)
#    # Remove stop words e vai montado o dicionário
#    # Find the element in a python list of strings which contains the string 'asdf'
#    nome = lista[0].replace('EXONERAR', '')
#    #cargo = format_element(find_string(lista, 'cargo'), ' ')
#    #matricula = lista[2].replace('matrícula ','')
#    matricula = format_element(find_string(lista, 'matrícula'), 'matrícula ')
#    simbolo = format_element(find_string(lista, 'Símbolo'), 'Símbolo ')
#
#    dicionario = {
#        'nome': nome,
#        'matricula': matricula,
#        'simbolo': simbolo
#    }
#    return dicionario
        

def extrai_texto(texto, termo):
    # Use BeautifulSoup to extract the <p> tag in a string
    lista = []
    soup = BeautifulSoup(texto)
    pessoas = soup.select(f':-soup-contains-own("{termo}")')
    if pessoas:
        for p in pessoas:
            pessoa = str(p.get_text('p'))
            lista.append(pessoa)

    return lista
            
def parse_data(data):
    dicionario = {}
    # Gets the the 'texto' section of each part
    secoes = data['json']['INFO']
    for secao in secoes.keys():
        dicionario[secao] = {}
        elementos = secoes[secao]
        for elemento in elementos.keys():
            dicionario[secao][elemento] = {}
            #formata_elemento(elementos[elemento])
            documentos = elementos[elemento]
            for documento in documentos:
                dicionario[secao][elemento][documento] = {}
                partes = documentos[documento]
                for parte in partes.keys():
                    texto = partes[parte]['texto']

                    # Extrai exonerados
                    exonerados = extrai_texto(texto, 'EXONERAR')
                    nomeados = extrai_texto(texto, 'NOMEAR')

                    # Monta um dicionário
                    dicionario[secao][elemento][documento][parte] = {}
                    if exonerados:
                        dicionario[secao][elemento][documento][parte]['exoneracoes'] = exonerados
                    if nomeados:
                        dicionario[secao][elemento][documento][parte]['nomeacoes'] = nomeados
                        break
                    else:
                        del dicionario[secao][elemento]
                        break
            

    return dicionario
            
def main(*args, **kwargs):
    filename = kwargs.get('filename')
    print('a')
    data = read_file(filename)
    parsed = parse_data(data)
    parsed_json = json.dumps(parsed)
    return parsed_json

#print(main('./file.json'))
