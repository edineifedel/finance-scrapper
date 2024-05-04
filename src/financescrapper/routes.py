# -*- coding: utf-8 -*-

from . import fundamentus
from . import finviz

from flask import Blueprint, request, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return 'Finance Scrapper'

@main_bp.route('/papel/<papel>', methods=['GET'])
def papel(papel):
    resumo = request.args.get('resumo', default=False, type=bool)
    dados_papel = fundamentus.get_papel(papel, resumo)

    if dados_papel is None:
        return jsonify({'error': 'Não foi possível obter os dados do papel.'}), 404

    return dados_papel

@main_bp.route('/ticker/<ticker>', methods=['GET'])
def ticker(ticker):
    dados_ticker = finviz.get_ticker(ticker)

    if dados_ticker is None:
        return jsonify({'error': 'Não foi possível obter os dados do ticker.'}), 404

    return dados_ticker