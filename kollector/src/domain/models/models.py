import datetime
from uuid import uuid4

from app import db
from flask_mongoengine.wtf import model_form


class Note(db.Document):
    content = db.StringField(required=True, max_length=140)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)

    def __repr__(self):
        return self.content


NoteForm = model_form(Note)

## models pydaria
from pydaria.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Product(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Numeric())
    description = db.Column(db.Text)


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
