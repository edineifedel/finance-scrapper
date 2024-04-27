import unicodedata

def normalize_key(key):
    normalized_key = unicodedata.normalize('NFKD', key).encode('ASCII', 'ignore').decode('utf-8')
    normalized_key = normalized_key.strip('?').replace('.', '')
    normalized_key = normalized_key.replace(' / ', '_').replace(' ', '_').replace('/', '_')
    return normalized_key

def normalize_value(value):
    if isinstance(value, str):
        if value.isdigit():
            return int(value)
        try:
            return float(value.replace(',', '.'))
        except ValueError:
            return value.replace(',', '.')
    return value