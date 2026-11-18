class Character:

    def __init__(self, nom, pv, atk):
        self.nom = nom
        self.pv = pv
        self.atk = atk
        self.life_state = True

# def créer un personnage
    # on crée des variables temporaires pour les valeurs
    # on trouve le bon personnage selon le nom dans la base de données
    # récupérer les caractéristiques du personnage pour les mettre dans les variables
    # créer un objet de la classe Character
    # retourner ce nouvel objet Character

#def create_character(dico,nom):
    # là ça marche pour un dictionnaire mais pour la bdd ça sera surement différent
    #name = dico[nom][0]
    #pv = dico[nom][1]["PV"]
    #atk = dico[nom][1]["ATK"]
    #chara = Character(name,pv,atk)
    #return chara


def afficher_options_numérotées(options):
    # pour chaque option dans enumerate(options, start=1)
    for option,i in enumerate(options, start=1):
        print(f"{i}. {option}")


def récupérer_choix_utilisateur(options):
    """Affiche les choix possibles et récupère le choix de l'utilisateur jusqu'à obtenir un résultat valide"""
    # tant que infini
    while True:
        # afficher options numérotées 
        afficher_options_numérotées(options)
        # récupérer le choix de l'utilisateur en demandant d'entrer un nombre entier entre le maximum et le minimum 
        choix = input(f"Veuillez entrer un nombre entier entre 0 et {len(options)}")
        # vérifier si le choix est un nombre
        if choix.isdigit():
            # vérifier si c'est un int
            if int(choix).is_integer():
                # vérifier si le choix est entre le minimum et le maximum:
                if int(choix) > 0 and int(choix) <= len(options):
                    # retourner le choix
                    return choix


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


# construire la liste des options à afficher disponibles
def construire_options_affichables(personnages_disponibles):
    # créer une liste options
    options = []
    # pour chaque personnage dans personnages_disponibles:
    for personnage in personnages_disponibles:
        # ajouter à la liste : f"{personnage["nom"]} - ATK : {personnage["ATK"]}- DEF : {personnage["DEF"]}"
        options.append(f"{personnage["nom"]} - ATK : {personnage["ATK"]}- DEF : {personnage["DEF"]}")
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

#create_character(personnages)