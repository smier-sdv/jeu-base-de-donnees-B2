from db_init import *

class Character:

    def __init__(self, nom, pv, atk):
        self.nom = nom
        self.pv = pv
        self.atk = atk
        self.life_state = True

def convertir_db_liste(liste_db):
    """Convertir une collection de la db en liste exploitable pour les personnages et les ennemis"""
    # On crée une nouvelle liste pour les personnages
    nouvelle_liste_personnages = []
    # On récupère les attributs de chaque personnage dans des valeurs
    for perso in liste_db: 
        liste_perso = []
        nom = perso['NOM']
        pv = perso['PV']
        atk = perso['ATK']
        defe = perso['DEF']
        # on fait une liste d'attributs
        liste_perso = [nom, pv, atk, defe]
        #print(liste_perso)
        #print(" ")
        # On ajoute la liste qui représente un personnage à une liste de tous les personnages
        nouvelle_liste_personnages.append(liste_perso)
    #print(nouvelle_liste_personnages)
    return nouvelle_liste_personnages


def de_liste_a_dictionnaire(liste_personnages):
    """Récupère une liste de personnages ou d'ennemis dans le format de convertir_db_liste et le transforme en dictionnaire pour récupérer la structure initiale de mes personnages et ennemis"""
    # On crée un dictionnaire vide pour ajouter tous les personnages
    dictionnaire_personnages = {}
    # On parcoure la liste de personnages donnée pour récupérer les attributs
    for liste_stats in liste_personnages:
        nom = liste_stats[0]
        pv = liste_stats[1]
        atk = liste_stats[2]
        defe = liste_stats[3]
        # on réorganise les informations sous forme de dictionnaire
        dictionnaire_personnages[nom] = {"NOM":nom,"PV":pv, "ATK":atk, "DEF":defe}

    # Test pour afficher le nouveau dictionnaire
    #for nom, stats in dictionnaire_personnages.items():
    #    print(nom, stats)
    #    print(" ")
        
        
# pour obtenir un dictionnaire de tous les personnages avec la même structure que ce que j'avais à la base: 
# liste_personnages_db = de_liste_a_dictionnaire(convertir_db_liste(get_personnages()))
# liste_ennemis = de_liste_a_dictionnaire(convertir_db_liste(get_ennemis()))


def créer_personnage(personnages_disponibles,nom):
    # on crée des variables temporaires pour les valeurs
    # on trouve le bon personnage selon le nom dans la base de données
    # récupérer les caractéristiques du personnage pour les mettre dans les variables
    name = personnages_disponibles[nom][0]
    pv = personnages_disponibles[nom][1]["PV"]
    atk = personnages_disponibles[nom][1]["ATK"]
    # créer un objet de la classe Character
    chara = Character(name,pv,atk)
    # retourner ce nouvel objet Character


def afficher_options_numérotées(options):
    # pour chaque option dans enumerate(options, start=1)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")


def récupérer_choix_utilisateur(options):
    """Affiche les choix possibles et récupère le choix de l'utilisateur jusqu'à obtenir un résultat valide"""
    # tant que le choix n'est pas valide
    est_valide = False
    while not est_valide:
        # afficher options numérotées 
        afficher_options_numérotées(options)
        # récupérer le choix de l'utilisateur en demandant d'entrer un nombre entier entre le maximum et le minimum 
        choix = input(f"Veuillez entrer un nombre entier entre 0 et {len(options)}: ")
        est_valide = est_choix_valide(choix,options)
    return choix
        

def est_choix_valide(choix,options):
    # vérifier si le choix est un nombre
    if not choix.isdigit():
        return False
    # vérifier si c'est un int
    if not int(choix).is_integer():
        return False
    # vérifier si le choix est entre le minimum et le maximum:
    if int(choix) <= 0 and int(choix) > len(options):
        return False
    return True


def est_équipe_complète(equipe):
    # si longueur de équipe égale à 3
    if len(equipe) == 3:
        return True
    return False


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


# On convertie l'équipe vers la structure souhaitée
def conversion_équipe():
    ...

# construire la liste des options à afficher disponibles
def construire_options_affichables(personnages_disponibles):
    # créer une liste options
    options = []
    # pour chaque personnage dans personnages_disponibles:
    for personnage in personnages_disponibles:
        # ajouter à la liste : f"{personnage["nom"]} - ATK : {personnage["ATK"]}- DEF : {personnage["DEF"]}"
        options.append(f"{personnage["NOM"]} - ATK : {personnage["ATK"]}- DEF : {personnage["DEF"]}")
    # retourner la liste d'options
    return options


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