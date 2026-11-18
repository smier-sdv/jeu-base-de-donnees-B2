from personnages import *

# classe Jeu:

    # def __init__(self):
        # nombre de vagues self.vagues = 0
        # état du jeu pour créer une boucle pour garder le jeu ouvert self.game_state = True
        # self.equipe = {}


    # def gameplay_loop(self):
        # réinitialiser toutes les valeurs à leur état initial
        # réinitialiser le nombre de vagues vagues = 0
        # vider le dictionnaire de l'équipe
        # remettre game_state = True
        # tant que self.game_state:
            # lancer self.tour()
        # La partie est terminée, on envoie le score dans la base de données
        # On retourne le score 

    # def tour(self):
    # sélectionner un monstre aléatoirement depuis la bdd
    # afficher le monstre et ses stats
    # tant que les pv du monstre > 0
        # gameover_check()
        # pour hero dans équipe
            # si le life_state de hero est True:
                # hero attaque ennemi
        # si les pv de l'ennemi > 0:
            # ennemi attaque un hero au hasard
        # sinon 
            # déclarer la victoire
            # vagues +=1


    # def attack(self, attaquant, victime):
        # """fonction qui gère les attaques"""
        # utiliser la fonction quand attaquant attaque:
        # si victime.pv - attaquant.atk >= 0:
            # victime.pv -= attaquant.atk
            # si victime.pv == 0:
                # mettre les pv de la victime à 0 et le signaler
                # mettre life_state = False pour la victime
        # sinon
            # mettre les pv de la victime à 0 et le signaler
            # mettre life_state = False pour la victime
        # return

        
    # def gameover_check(self, characterlist):
        # vies = len(characterlist)
        # pour hero dans characterlist:
            # si life_state est false:
                # vies -= 1
        # si vies == 0
            # afficher message de game over
            # mettre self.game_state en False
            # renvoyer le nombre de vagues