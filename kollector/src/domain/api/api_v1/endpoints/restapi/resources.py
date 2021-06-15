from flask import abort, jsonify
from flask_restful import Resource

from kollector.src.domain.models.models import Product # from pydaria.models import Product
# NO IMPORT DA LINHA 4 VER COMO ESTÃO OS ARQUIVOS DA API FASTAPI E SEPARAR MODELS COM NOME DE ARQUIVO E IMPORT DE ACORDO COM ARQUIVO MODEL SEPARADO


class ProductResource(Resource):
    def get(self):
        products = Product.query.all() or abort(204)
        return jsonify(
            {"products": [product.to_dict() for product in products]}
        )


class ProductItemResource(Resource):
    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first() or abort(404)
        return jsonify(product.to_dict())
