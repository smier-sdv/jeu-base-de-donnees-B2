from personnages import *
from random import *

class Jeu:

    def __init__(self):
        # nombre de vagues 
        self.vagues = 0
        # état du jeu pour créer une boucle pour garder le jeu ouvert 
        self.game_state = True
        self.equipe = {}


    def gameplay_loop(self):
        # réinitialiser le nombre de vagues 
        self.vagues = 0
        # vider le dictionnaire de l'équipe
        self.equipe = {}
        # créer une équipe
        self.equipe = créer_équipe(get_personnages())
        afficher_equipe(self.equipe)
        # remettre self.game_state = True
        self.game_state = True
        # tant que self.game_state:
        while self.game_state:
            # lancer self.tour()
            self.tour()
        # La partie est terminée, on envoie le nombre de vagues dans la base de données
        # On retourne le nombre de vagues
        return self.vagues

    def tour(self):
        # sélectionner un monstre aléatoirement depuis la bdd
        ennemi = self.ennemi_aléatoire()
        # afficher le monstre et ses stats
        self.afficher_ennemi(ennemi)
        # tant que les pv du monstre > 0
        while ennemi["PV"] > 0 and self.game_state:
            # On vérifie si l'équipe est toujours vivante
            self.gameover_check()
            # pour héros dans équipe
            for héros in self.equipe:
                # si le héros est en vie:
                if héros["PV"] > 0:
                    # héros attaque ennemi
                    self.attack(héros,ennemi)
            # si l'ennemi est en vie
            if ennemi["PV"] > 0:
                print(f"{ennemi["NOM"]} a {ennemi["PV"]} PV")
                # obtenir un héros vivant aléatoire
                héros_choisi = self.héros_vivant_aléatoire()
                # ennemi attaque un hero au hasard
                self.attack(ennemi,héros_choisi)
            # sinon 
            else:
                # on augmente le compteur de vagues
                self.vagues +=1


    def attack(self, attaquant, victime):
        """fonction qui gère les attaques"""
        # on retire les pv de l'attaque à la victime
        victime["PV"] -= attaquant["ATK"]
        # si la victime est morte
        if victime["PV"] <= 0:
            # mettre les pv de la victime à 0 et le signaler
            victime["PV"] = 0
            print(f"{victime["NOM"]} a été vaincu !")
        return

        
    def gameover_check(self):
        # On crée un check pour voir si tous les héros sont en vie
        vies = len(self.equipe)
        # pour hero dans equipe:
        for hero in self.equipe:
            # si les pv du héros sont à 0, on retire une vie au total
            if hero["PV"] == 0:
                vies -= 1
        # Si toute l'équipe est morte
        if vies == 0:
            # afficher message de game over
            print("Ton équipe a été vaincue. Game Over")
            # mettre self.game_state en False
            self.game_state = False


    def héros_vivant_aléatoire(self):
        while True:
            héros_choisi = self.equipe[randint(0,len(self.equipe)-1)]
            if héros_choisi["PV"] > 0:
                return héros_choisi


    def ennemi_aléatoire(self):
        # Récupérer la liste des ennemis et en envoyer un au hasard
        liste_ennemis = get_ennemis()
        return liste_ennemis[randint(0,len(liste_ennemis)-1)]


    def afficher_ennemi(self, ennemi):
        # Afficher le nom de l'ennemi et ses stats
        print(f"{ennemi["NOM"]} - ATK : {ennemi["ATK"]} - DEF : {ennemi["DEF"]}")