from . import jsonconverter
from . import utils

import logging
import requests
import pandas as pd

INDEX_TABLE_FUNDAMENTALIST_FINVIZ = 6

def get_ticker(ticker):
    df_finviz = _get_html_data_frame_finviz(ticker)

    if (df_finviz is None):
        return None

    data_dict = utils.get_dict_papel_from_data_frame(df_finviz)

    return jsonconverter.to_json_ticker(data_dict)

def _get_html_data_frame_finviz(ticker):
    try:
        url = 'https://finviz.com/quote.ashx?t={}'.format(ticker)
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
        content = requests.get(url, headers=headers)
        lista_df = pd.read_html(content.text)
        return lista_df[INDEX_TABLE_FUNDAMENTALIST_FINVIZ]
    except Exception:
        return None
