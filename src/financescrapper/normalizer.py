import unicodedata

def normalize_key(key):
    normalized_key = unicodedata.normalize('NFKD', key).encode('ASCII', 'ignore').decode('utf-8')
    normalized_key = normalized_key.strip('?').replace('.', '')
    normalized_key = normalized_key.replace(' / ', '_').replace(' ', '_').replace('/', '_')
    return normalized_key

# Função para normalizar os valores
def normalize_value(value):
    # Verificar se o valor é uma string
    if isinstance(value, str):
        # Tentar converter para número
        try:
            if ',' in value or '.' in value:
              normalized_value = float(value)
            else:
            # Converter para int
              normalized_value = int(value)
        except ValueError:
            # Se a conversão falhar, manter o valor original
            normalized_value = value.replace(',', '.')
    else:
        # Se o valor não for uma string, mantê-lo como está
        normalized_value = value
    return normalized_value