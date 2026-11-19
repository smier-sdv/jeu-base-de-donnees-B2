# Voici une classe que j'avais préparé pour les personnages et les ennemis.
# Ce sont les mêmes attributs que dans leurs formats actuels de listes de dictionnaires, 
# sauf pour life_state qui sert de booléen pour savoir si le personnage est vivant ou mort au lieu d'analyser les pv à chaque fois.
# Cette classe est inutilisée mais dans les consignes il fallait avoir un models.py pour les classes de personnages et ennemis donc je l'ai mise au cas où.

class Character:
    def __init__(self,nom,pv,atk,defe):
        self.nom = nom
        self.pv = pv
        self.atk = atk
        self.defe = defe
        self.life_state = True