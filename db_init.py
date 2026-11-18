from pymongo import MongoClient
client = MongoClient("mongodb://localhost:")
db = client["char"]
def get_personnages():
    return list(db.personnages.find())
def get_ennemis():
    return list(db.ennemis.find())
def get_scores():
    return list(db.scores.find())