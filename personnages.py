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
    #
    #name = dico[nom][0]
    #pv = dico[nom][1]["PV"]
    #atk = dico[nom][1]["ATK"]
    #chara = Character(name,pv,atk)
    #return chara



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


# def gameover():
    # appelé quand les pv de quelqu'un dans l'équipe sont à 0


def attack(attaquant, victime):
    """fonction qui gère les attaques"""
    # utiliser la fonction quand attaquant attaque:
    # si victime.pv - attaquant.atk >= 0:
        # victime.pv -= attaquant.atk
        # si victime.pv == 0:
            # signaler que les pv de la victime sont à 0
    # sinon
        # signaler que les pv de la victime sont à 0
    return