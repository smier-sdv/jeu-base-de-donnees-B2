from db_init import *
from utils import *


def créer_équipe(liste_personnages_db):
    # créer un nouveau dictionnaire pour l'équipe
    equipe = []
    # tant que l'équipe n'est pas complète:
    while not est_équipe_complète(equipe):
        # déterminer la liste des personnages disponibles
        personnages_disponibles = determiner_personnages_disponibles(liste_personnages_db,equipe)
        # construire la liste des options à afficher disponibles
        options_affichables = construire_options_affichables(personnages_disponibles)
        # récupérer un choix valide
        choix = récupérer_choix_utilisateur(options_affichables)
        # ajouter le personnage choisi à l'équipe index = choix -1
        equipe.append(personnages_disponibles[choix-1])
    # retourner l'équipe
    return equipe


def afficher_equipe(equipe):
    print("Voici votre équipe :")
    construire_options_affichables(equipe)
    return


def est_équipe_complète(equipe):
    # si longueur de équipe égale à 3
    if len(equipe) == 3:
        return True
    return False


def determiner_personnages_disponibles(liste_personnages_db, equipe):
    # créer la liste des personnages disponibles
    personnages_disponibles = []
    # pour chaque personnage dans la liste des personnages de la DB 
    for personnage in liste_personnages_db:
        # si le personnage n'est pas dans l'équipe 
        if personnage not in equipe:
            # l'ajouter à la liste des personnages disponibles
            personnages_disponibles.append(personnage)
    # renvoyer la liste des personnages disponibles
    return personnages_disponibles





"""
# Ancien modèle pour les personnages et les ennemis
personnages = {
        "Guerrier" : {"PV": 100, "ATK": 15, "DEF": 10},
        "Mage" : {"PV": 80, "ATK": 20, "DEF": 5},
        "Archer" : {"PV": 90, "ATK": 18, "DEF": 7},
        "Voleur" : {"PV": 85, "ATK": 22, "DEF": 8},
        "Paladin" : {"PV": 110, "ATK": 14, "DEF": 12},
        "Sorcier" : {"PV": 70, "ATK": 25, "DEF": 3},
        "Chevalier" : {"PV": 120, "ATK": 17, "DEF": 15},
        "Moine" : {"PV": 95, "ATK": 19, "DEF": 9},
        "Berserker" : {"PV": 105, "ATK": 23, "DEF": 6},
        "Chasseur" : {"PV": 100, "ATK": 16, "DEF": 11}
    }

enemy_list = {
        "Gobelin" : {"PV": 50, "ATK": 10, "DEF": 5},
        "Orc" : {"PV": 120, "ATK": 20, "DEF": 8},
        "Dragon" : {"PV": 200, "ATK": 30, "DEF": 20},
        "Zombie" : {"PV": 70, "ATK": 12, "DEF": 6},
        "Troll" : {"PV": 200, "ATK": 25, "DEF": 15},
        "Spectre" : {"PV": 100, "ATK": 18, "DEF": 10},
        "Golem" : {"PV": 200, "ATK": 28, "DEF": 25},
        "Vampire" : {"PV": 150, "ATK": 22, "DEF": 12},
        "Loup-garou" : {"PV": 180, "ATK": 25, "DEF": 18},
        "Squelette" : {"PV": 90, "ATK": 15, "DEF": 7}
    }
"""