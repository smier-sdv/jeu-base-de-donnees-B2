from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["bdd_jeu_b2"]



def get_personnages():
    return list(db.personnages.find({},{id:0}))

def get_ennemis():
    return list(db.ennemis.find())

def get_scores():
    return list(db.scores.find())