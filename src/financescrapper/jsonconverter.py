import json

def to_json_acao_resumo(papel_dict):
    json_base = {
        "papel": papel_dict.get("Papel", None),
        "cotacao": papel_dict.get("Cotacao", None),
        "empresa": papel_dict.get("Empresa", None),
        "pl": papel_dict.get("P_L", None),
        "lpa": papel_dict.get("LPA", None),
        "pvp": papel_dict.get("P_VP", None),
        "vpa": papel_dict.get("VPA", None),
        "margem_liquida": papel_dict.get("Marg_Liquida", None),
        "roic": papel_dict.get("ROIC", None),
        "dy": papel_dict.get("Div_Yield", None),
        "roe": papel_dict.get("ROE", None),
        "div_bruta_patrim": papel_dict.get("Div_Br_Patrim", None),
        "cres_rec_5a": papel_dict.get("Cres_Rec_5a", None),
        "receita_liquida": papel_dict.get("Receita_Liquida", None),
        "ebit": papel_dict.get("EBIT", None),
        "lucro_liquido": papel_dict.get("Lucro_Liquido", None),
        "patrim_liquido": papel_dict.get("Patrim_Liq", None),
        "disponibilidades": papel_dict.get("Disponibilidades", None),
        "div_liquida": papel_dict.get("Div_Liquida", None)
    }
    return json.dumps(json_base, ensure_ascii=False, indent=4)

def to_json_acao(papel_dict):
    json_base = {
        "papel": papel_dict.get("Papel", None),
        "cotacao": papel_dict.get("Cotacao", None),
        "tipo": papel_dict.get("Tipo", None),
        "data_ult_cot": papel_dict.get("Data_ult_cot", None),
        "empresa": papel_dict.get("Empresa", None),
        "min_52_sem": papel_dict.get("Min_52_sem", None),
        "setor": papel_dict.get("Setor", None),
        "max_52_sem": papel_dict.get("Max_52_sem", None),
        "subsetor": papel_dict.get("Subsetor", None),
        "vol_med_2m": papel_dict.get("Vol_med_2m", None),
        "valor_de_mercado": papel_dict.get("Valor_de_mercado", None),
        "ult_balanco_processado": papel_dict.get("Ult_balanco_processado", None),
        "valor_da_firma": papel_dict.get("Valor_da_firma", None),
        "nro_Acoes": papel_dict.get("Nro_Acoes", None),
        "oscilacoes": {
            "dia": papel_dict.get("Dia", None),
            "mes": papel_dict.get("Mes", None),
            "30_dias": papel_dict.get("30_dias", None),
            "12_meses": papel_dict.get("12_meses", None),
            "2024": papel_dict.get("2024", None),
            "2023": papel_dict.get("2023", None),
            "2022": papel_dict.get("2022", None),
            "2021": papel_dict.get("2021", None),
            "2020": papel_dict.get("2020", None),
            "2019": papel_dict.get("2019", None)
        },
        "indicadores_fundamentalistas": {
            "pl": papel_dict.get("P_L", None),
            "lpa": papel_dict.get("LPA", None),
            "pvp": papel_dict.get("P_VP", None),
            "vpa": papel_dict.get("VPA", None),
            "p_ebit": papel_dict.get("P_EBIT", None),
            "marg_bruta": papel_dict.get("Marg_Bruta", None),
            "psr": papel_dict.get("PSR", None),
            "marg_ebit": papel_dict.get("Marg_EBIT", None),
            "p_ativos": papel_dict.get("P_Ativos", None),
            "marg_liquida": papel_dict.get("Marg_Liquida", None),
            "p_cap_giro": papel_dict.get("P_Cap_Giro", None),
            "ebit_ativo": papel_dict.get("EBIT_Ativo", None),
            "p_ativ_circ_liq": papel_dict.get("P_Ativ_Circ_Liq", None),
            "roic": papel_dict.get("ROIC", None),
            "dy": papel_dict.get("Div_Yield", None),
            "roe": papel_dict.get("ROE", None),
            "ev_ebitda": papel_dict.get("EV_EBITDA", None),
            "liquidez_corr": papel_dict.get("Liquidez_Corr", None),
            "ev_ebit": papel_dict.get("EV_EBIT", None),
            "div_br_patrim": papel_dict.get("Div_Br_Patrim", None),
            "cres_rec_5a": papel_dict.get("Cres_Rec_5a", None),
            "giro_ativos": papel_dict.get("Giro_Ativos", None)
        },
        "dados_balanco_patrimonial": {
            "ativo": papel_dict.get("Ativo", None),
            "div_bruta": papel_dict.get("Div_Bruta", None),
            "disponibilidades": papel_dict.get("Disponibilidades", None),
            "div_liquida": papel_dict.get("Div_Liquida", None),
            "ativo_circulante": papel_dict.get("Ativo_Circulante", None),
            "patrim_liquido": papel_dict.get("Patrim_Liq", None)
        },
        "dados_demonstrativos_de_resultados": {
            "ultimos_12_meses": {
                "receita_liquida": papel_dict.get("Receita_Liquida", None),
                "ebit": papel_dict.get("EBIT", None),
                "lucro_liquido": papel_dict.get("Lucro_Liquido", None)
            }
        }
    }
    return json.dumps(json_base, ensure_ascii=False, indent=4)

def to_json_fii_resumo(papel_dict):
    json_base = {
        "fii": papel_dict.get("FII", None),
        "cotacao": papel_dict.get("Cotacao", None),
        "nome": papel_dict.get("Nome", None),
        "segmento": papel_dict.get("Segmento", None),
        "gestao": papel_dict.get("Gestao", None),
        "ffo_yield": papel_dict.get("FFO_Yield", None),
        "dy": papel_dict.get("Div_Yield", None),
        "p_vp": papel_dict.get("P_VP", None),
        "receita": papel_dict.get("Receita", None),
        "ativos": papel_dict.get("Ativos", None),
        "patrim_liquido": papel_dict.get("Patrim_Liquido", None),
        "vacancia_media": papel_dict.get("Vacancia_Media", None)
    }
    return json.dumps(json_base, ensure_ascii=False, indent=4)


def to_json_fii(papel_dict):
    json_base = {
        "fii": papel_dict.get("FII", None),
        "cotacao": papel_dict.get("Cotacao", None),
        "nome": papel_dict.get("Nome", None),
        "data_ult_cot": papel_dict.get("Data_ult_cot", None),
        "mandato": papel_dict.get("Mandato", None),
        "min_52_sem": papel_dict.get("Min_52_sem", None),
        "segmento": papel_dict.get("Segmento", None),
        "max_52_sem": papel_dict.get("Max_52_sem", None),
        "gestao": papel_dict.get("Gestao", None),
        "vol_$_med_(2m)": papel_dict.get("Vol_med_2m", None),
        "valor_de_mercado": papel_dict.get("Valor_de_mercado", None),
        "nro_cotas": papel_dict.get("Nro_Cotas", None),
        "relatorio": papel_dict.get("Relatorio", None),
        "ult_info_trimestral": papel_dict.get("Ult_Info_Trimestral", None),
        "oscilacoes": {
            "dia": papel_dict.get("Dia", None),
            "mes": papel_dict.get("Mes", None),
            "30_dias": papel_dict.get("30_dias", None),
            "12_meses": papel_dict.get("12_meses", None),
            "2024": papel_dict.get("2024", None),
            "2023": papel_dict.get("2023", None),
            "2022": papel_dict.get("2022", None),
            "2021": papel_dict.get("2021", None),
            "2020": papel_dict.get("2020", None),
            "2019": papel_dict.get("2019", None)
        },
        "indicadores": {
            "ffo_yield": papel_dict.get("FFO_Yield", None),
            "ffo_cota": papel_dict.get("FFO_Cota", None),
            "dy": papel_dict.get("Div_Yield", None),
            "dividendo_cota": papel_dict.get("Dividendo_cota", None),
            "p_vp": papel_dict.get("P_VP", None),
            "vp_cota": papel_dict.get("VP_Cota", None),
        },
        "resultado": {
            "ultimos_12_meses": {
                "receita": papel_dict.get("Receita", None),
                "venda_de_ativos": papel_dict.get("Venda_de_ativos", None),
                "ffo": papel_dict.get("FFO", None),
                "rend_distribuido": papel_dict.get("Rend_Distribuido", None),
            }
        },
        "balanco_patrimonial": {
            "ativos": papel_dict.get("Ativos", None),
            "patrim_liquido": papel_dict.get("Patrim_Liquido", None),
        },
        "imoveis": {
            "qtd_imoveis": papel_dict.get("Qtd_imoveis", None),
            "area_(m2)": papel_dict.get("Area_m2", None),
            "cap_rate": papel_dict.get("Cap_Rate", None),
            "qtd_Unidades": papel_dict.get("Qtd_Unidades", None),
            "aluguel_m2": papel_dict.get("Aluguel_m2", None),
            "vacancia_media": papel_dict.get("Vacancia_Media", None),
            "imoveis_pl_do_fii": papel_dict.get("Imoveis_PL_do_FII", None),
            "preco_do_m2": papel_dict.get("Preco_do_m2", None),
        }
    }
    return json.dumps(json_base, ensure_ascii=False, indent=4)