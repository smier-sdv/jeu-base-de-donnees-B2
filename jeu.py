from personnages import *

# classe Jeu:

    # def __init__(self):
        # nombre de vagues self.vagues = 0
        # état du jeu pour créer une boucle pour garder le jeu ouvert self.game_state = True


    # def gameplay_loop(self):
        # tant que self.game_state:
            # lancer self.tour()

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
        # pour hero dans characterlist
            # si life_state est false:
                # vies -= 1
        # si vies == 0
            # afficher message de gameover
            # mettre en False un booléen pour run le jeu qui s'appellerait genre game_state mais faudrait le passer en classe pour y avoir accès donc ce serait self.game_state
            # renvoyer le nombre de vagues