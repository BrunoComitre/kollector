from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash

from kollector.src.extensions.utils.database import db # from pydaria.ext.database import db
from kollector.src.domain.models.models import User # from pydaria.models import User
# NO IMPORT DA LINHA 5 VER COMO ESTÃO OS ARQUIVOS DA API FASTAPI E SEPARAR MODELS COM NOME DE ARQUIVO E IMPORT DE ACORDO COM ARQUIVO MODEL SEPARADO

def verify_login(user):
    """Valida o usuario e senha para efetuar o login"""
    username = user.get('username')
    password = user.get('password')
    if not username or not password:
        return False
    existing_user = User.query.filter_by(username=username).first()
    if not existing_user:
        return False
    if check_password_hash(existing_user.password, password):
        return True
    return False


def create_user(username, password):
    """Registra um novo usuario caso nao esteja cadastrado"""
    if User.query.filter_by(username=username).first():
        raise RuntimeError(f'{username} ja esta cadastrado')
    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return user


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
