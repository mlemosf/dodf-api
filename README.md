# DODF API

Este projeto apresenta um serviço de API RESTful não-oficial para busca de informações do Diário Oficial do Distrito Federal (DODFe).
Este software é distribuído sem garantias.

## Instalação

Para instalar a API em seu próprio ambiente, realize a instalação utilizando ambiente virtual

1. Instalação das dependências:

Utilize a ferramenta de ambiente virtual de sua preferência. Neste projeto utilizei o virtualenv.

```shell
$ virtualenv venv
$ source venv/bin/activate
$ (venv) pip install -r requirements.txt
```

2. Execução da API

A api pode ser executada localmente para desenvolvimento:

```shell
$ fastapi dev main.py
```

A documentação da API poderá ser encontrada em http://localhost:8000.
