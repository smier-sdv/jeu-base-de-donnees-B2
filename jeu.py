from personnages import *

# def tour():
# sélectionner un monstre aléatoirement depuis la bdd
# afficher le monstre et ses stats
# tant que les pv du monstre > 0
    # gameover_check()
    # pour hero dans équipe
        # hero attaque ennemi
    # si les pv de l'ennemi > 0:
        # ennemi attaque un hero au hasard
    # sinon 
        # déclarer la victoire
        # vagues +=1


# def attack(attaquant, victime):
    # """fonction qui gère les attaques"""
    # utiliser la fonction quand attaquant attaque:
    # si victime.pv - attaquant.atk >= 0:
        # victime.pv -= attaquant.atk
        # si victime.pv == 0:
            # signaler que les pv de la victime sont à 0
            # mettre life_state = False pour la victime
    # sinon
        # signaler que les pv de la victime sont à 0
        # mettre life_state = False pour la victime
    # return

    
# def gameover_check(characterlist):
    # vies = len(characterlist)
    # pour hero dans characterlist
        # si state_life est false:
            # vies -= 1
    # si vies == 0
        # afficher message de gameover
        # mettre en False un booléen pour run le jeu qui s'appellerait genre game_state mais faudrait le passer en classe pour y avoir accès donc ce serait self.game_state
        # renvoyer le nombre de vagues