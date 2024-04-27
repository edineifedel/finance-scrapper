# -*- coding: utf-8 -*-

from . import fundamentus

from flask import Blueprint, request, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return 'Fundamentus!'

@main_bp.route('/papel/<papel>', methods=['GET'])
def papel(papel):
    simplificado = request.args.get('simplificado', default=False, type=bool)
    dados_papel = fundamentus.get_papel(papel, simplificado)

    if dados_papel is None:
        return jsonify({'error': 'Não foi possível obter os dados do papel.'}), 404

    return dados_papel