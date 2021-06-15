##APP.PY PYDARIA
from flask import Flask

from kollector.src.extensions.utils import configuration # É O MESMO QUE: from pydaria.ext import configuration


def minimal_app(**config): # SÓ LÊ AS CONFIGURAÇÕES # USADO APENAS PARA TESTES
    app = Flask(__name__)
    configuration.init_app(app, **config) #ONINITAPP É DO FLASK ADMIN PARA CRIAR DA BASE DE DADOS NA PÁGINA
    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    return app

#### AQUI NO EXEMPLO ORIGINAL QUE USAVA ESSE TINHA CIRCULAR IMPORT POIS IMPORTAVA APP
# from flask import Flask
# # from flask_mongoengine import MongoEngine # FAZER O MESMO DA LINHA 9  NO MONGOENGINE
# from config import Config


# app = Flask(__name__)
# # db = MongoEngine()

# def create_app():
#     app.config.from_object(Config)

#     from app.api import api_bp
#     app.register_blueprint(api_bp, url_prefix='/v1')
    
#     db.init_app(app)

#     return app


# from . import models
