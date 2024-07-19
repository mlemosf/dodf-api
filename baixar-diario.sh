#!/bin/bash
# Cronjob para baixar o diario no início do dia

URL=https://www.dodf.df.gov.br/index/jornal-json
ANO=$(date '+%Y')
MES=$(date '+%m')
DIA=$(date '+%d')
PASTA_SCRIPT="$(dirname "$(readlink -f "$0")")"
PASTA_DESTINO=${PASTA_SCRIPT}/diarios/${ANO}/${MES}

# Cria a pasta
mkdir -p ${PASTA_DESTINO}

# Baixa o diario para a pasta de destino
curl -o ${PASTA_DESTINO}/${DIA}.json ${URL}


