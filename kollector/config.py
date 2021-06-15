import os

from dotenv import load_dotenv
from pymongo import MongoClient


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "never talk to you"
    MONGODB_SETTINGS = {
        'db': 'notes',
        'host': 'mongodb://mongodb:27017/notes'
    }
