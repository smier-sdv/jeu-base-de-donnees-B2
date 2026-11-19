from pymongo import MongoClient
from pymongo.errors import PyMongoError

client = MongoClient("mongodb://localhost:27017")
db = client["bdd_jeu_b2"]

def get_personnages():
    return list(db.personnages.find())

def get_ennemis():
    return list(db.ennemis.find())

def get_scores():
    return list(db.scores.find())