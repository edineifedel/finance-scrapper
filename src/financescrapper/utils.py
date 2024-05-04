from . import normalizer

def get_dict_papel_from_data_frame(df_fundamentus):
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