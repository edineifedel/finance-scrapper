from . import jsonconverter

import logging
import requests

def get_proventos(tipo, papel, data_inicio, data_fim):
    json_proventos = _get_proventos_from_status_invest(tipo, papel, data_inicio, data_fim)

    if (json_proventos is None):
        return None

    return jsonconverter.to_json_proventos(json_proventos)

def _get_proventos_from_status_invest(tipo, papel, data_inicio, data_fim):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    if tipo == 'acoes':
        url = 'https://statusinvest.com.br/acao/getearnings?IndiceCode=ibovespa&Filter={}&Start={}&End={}'.format(papel, data_inicio, data_fim)
        content = requests.get(url, headers=headers)
        return content.json()
    elif tipo == 'fiis':
        url = 'https://statusinvest.com.br/fii/getearnings?IndiceCode=ifix&Filter={}&Start={}&End={}'.format(papel, data_inicio, data_fim)
        content = requests.get(url, headers=headers)
        return content.json()
    else:
        return None