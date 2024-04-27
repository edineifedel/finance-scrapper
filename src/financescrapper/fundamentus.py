from . import normalizer
from . import jsonconverter

import logging
import requests
import pandas as pd

def get_papel(papel, simplificado):
    df_fundamentus = _get_html_data_frame_fundamentus(papel)

    if (df_fundamentus is None):
        return None

    data_dict = _get_dict_papel_from_data_frame(df_fundamentus)
    logging.info(data_dict)

    return _to_json(data_dict, simplificado)

def _get_dict_papel_from_data_frame(df_fundamentus):
    data_dict = {}
    for index, row in df_fundamentus.iterrows():
        row = row.dropna()
        if len(row) > 0:
            keys = row.iloc[::2].tolist()
            values = row.iloc[1::2].tolist()
            for key, value in zip(keys, values):
                normalized_key = normalizer.normalize_key(key)
                if normalized_key not in data_dict:
                    data_dict[normalized_key] = normalizer.normalize_value(value)
    return data_dict

def _get_html_data_frame_fundamentus(papel):
    try:
        url = 'http://fundamentus.com.br/detalhes.php?papel={}'.format(papel)
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
        content = requests.get(url, headers=headers)
        lista_df = pd.read_html(content.text, decimal=",", thousands='.')
        return pd.concat(lista_df, axis=0, ignore_index=True)
    except Exception:
        return None
    
def _to_json(papel_dict, simplificado):
    if (simplificado):
        return jsonconverter.to_json_simplificado(papel_dict)
    else:
        return jsonconverter.to_json(papel_dict)