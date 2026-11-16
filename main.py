class Character:

    def __init__(self, nom, pv, atk):
        self.nom = nom
        self.pv = pv
        self.atk = atk


def create_character(dico):
    characterlist = []
    for key in dico.items():
        name = key
        print(key[1]["ATK"])
        #atk = key.ATK.value()
        #pv = key.PV.value()
        #characterlist.append(Character(name,pv,atk))
    #return characterlist



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

create_character(personnages)