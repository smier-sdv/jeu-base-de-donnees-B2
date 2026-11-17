from personnages import *


# def gameover_check():
    # si les pv de tt le monde dans l'équipe sont à 0
    # afficher message de gameover
    # mettre en False un booléen pour run le jeu qui s'appellerait genre game_on

# def tour():
# sélectionner un monstre aléatoirement depuis la bdd
# afficher le monstre et ses stats
# tant que les pv du monstre > 0
    # pour hero dans équipe
        # hero attaque ennemi
    # si les pv de l'ennemi > 0:
        # ennemi attaque un hero au hasard


def attack(attaquant, victime):
    """fonction qui gère les attaques"""
    # utiliser la fonction quand attaquant attaque:
    # si victime.pv - attaquant.atk >= 0:
        # victime.pv -= attaquant.atk
        # si victime.pv == 0:
            # signaler que les pv de la victime sont à 0 et lui mettre life_state = False
    # sinon
        # signaler que les pv de la victime sont à 0 et lui mettre life_state = False
    # return
    ...