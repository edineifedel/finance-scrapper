# Finance Scrapper

O Finance Scrapper é um projeto que realiza web scraping de sites como https://www.fundamentus.com.br e https://finviz.com e disponibiliza as informações através de APIs REST.

## Tecnologias Utilizadas

- Flask
- Pandas
- Docker

## Pré-Requisitos

- Docker

## Passos

1. **Build**
```bash
docker build -t finance-scrapper .
```

2. **Run**

```bash
docker run --rm -p 5000:5000 --name finance-scrapper finance-scrapper
```

## Exemplo de Uso para Ações

- GET `/papel/wege3?resumo=true`

## Exemplo de Saída

```json
{
  "papel": "WEGE3",
  "cotacao": 39.22,
  "empresa": "WEG SA ON N1",
  "pl": 28.72,
  "lpa": 1.37,
  "pvp": 9.49,
  "vpa": 4.13,
  "margem_liquida": "18.1%",
  "roic": "33.0%",
  "dy": "1.8%",
  "roe": "33.1%",
  "ev_ebitda": 20.15,
  "div_bruta_patrim": 2835060000,
  "cres_rec_5a": "26.5%",
  "receita_liquida": 32503600000,
  "ebit": 7329520000,
  "lucro_liquido": 5731670000
}
```

Também é possível obter informações sobre Fundos Imobiliários (FIIs):

## Exemplo de Uso para FIIs

- GET `/papel/hglg11?resumo=true`

## Exemplo de Saída para FIIs

```json
{
  "fii": "HGLG11",
  "cotacao": 164.21,
  "nome": "CSHG LOGÍSTICA - FUNDO DE INVESTIMENTO IMOBILIÁRIO - FII",
  "segmento": "Logística",
  "gestao": "Ativa",
  "ffo_yield": "5.74%",
  "dy": "7.9%",
  "p_vp": 1.04,
  "receita": 375829000,
  "ativos": 6322430000,
  "patrim_liquido": 5324770000,
  "vacancia_media": "7.5%"
}
```

Para acessar as informações completas de um papel:

- GET `/papel/wege3`
- GET `/papel/hglg11`


## Exemplo de Uso para Stocks e REITs

- GET `/ticker/msft`
- GET `/ticker/avb`

## Exemplo de Saída para Stocks e REITs

```json
{
   "index": "DJIA. NDX. S&P 500",
   "price": 406.66,
   "market_cap": "3022.42B",
   "forward_p_e": 30.46,
   "income": "86.18B",
   "sales": "236.58B",
   "dividend_ttm": "2.86 (0.70%)",
   "dividend_est": "2.95 (0.73%)",
   "dividend_ex_date": "May 15. 2024",
   "eps_next_y": 13.35,
   "eps_this_y": "20.25%",
   "peg": 2.17,
   "p_e": 35.24,
   "p_s": 12.78,
   "p_b": 11.94,
   "p_fcf": 42.83,
   "roe": "38.49%",
   "roi": "26.01%",
   "profit_margin": "36.43%",
   "gross_margin": "69.89%",
   "perf_year": "33.59%",
   "debt_eq": 0.42,
   "target_price": 479.04
}
```