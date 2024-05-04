from . import normalizer
from . import jsonconverter
from . import utils

import logging
import requests
import pandas as pd

def get_papel(papel, resumo):
    df_fundamentus = _get_html_data_frame_fundamentus(papel)

    if (df_fundamentus is None):
        return None

    data_dict = utils.get_dict_papel_from_data_frame(df_fundamentus)

    return _to_json(data_dict, resumo)

def _get_html_data_frame_fundamentus(papel):
    try:
        url = 'http://fundamentus.com.br/detalhes.php?papel={}'.format(papel)
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
        content = requests.get(url, headers=headers)
        lista_df = pd.read_html(content.text, decimal=",", thousands='.')
        return pd.concat(lista_df, axis=0, ignore_index=True)
    except Exception:
        return None
    
def _to_json(papel_dict, resumo):
    if is_fii(papel_dict):
        return jsonconverter.to_json_fii(papel_dict, resumo)
    else:
        return jsonconverter.to_json_acao(papel_dict, resumo)

def is_fii(papel_dict):
    return 'FII' in papel_dict