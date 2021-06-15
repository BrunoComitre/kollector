from flask_mongoengine import MongoEngine
#from flask_sqlalchemy import SQLAlchemy

db = MongoEngine()
# db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
# def init_app(app):
#     db.init_app(app)
    
# FAZER O CÓDIGO ACIMA PARA O MONGO E TROCAR O NOME DOS ARQUIVOS.PY PARA DATABASES

