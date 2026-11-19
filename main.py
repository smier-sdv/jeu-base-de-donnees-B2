from game import *

# Fonction d'affichage du menu
def menu_principal():
    # Header du menu principal
    afficher_header("Menu Principal")
    # créer une liste d'options
    options = ["Lancer le jeu", "Voir le classement", "Quitter"]
    # afficher menu principal et récupérer un choix valide de l'utilisateur
    choix = récupérer_choix_utilisateur(options)
    # si choix == 1:
    if choix == 1:
        # Header du jeu
        afficher_header("GAME START")
        # Lancer option 1, le jeu avec gameplay_loop()
        jeu = Jeu()
        score = jeu.gameplay_loop()
        # On affiche le score de la partie
        print(f"Score de la partie : {score}")
        # On affiche le classement
        classement()
        return True
    # si choix == 2: 
    if choix == 2:
        # Lancer option 2, le classement
        classement()
        return True
    # si choix == 3:
    if choix == 3:
        # Lancer l'option 3 arrêter le jeu
        return False


def afficher_header(titre:str):
    print("-" * 23)
    print(titre.center(23))
    print("-"*23)


# On affiche le classement
def classement():
    # On affiche le header
    afficher_header("Classement")
    # On récupère les scores de la bdd
    liste_scores = get_scores()
    # On prend les 3 meilleurs scores de la bdd
    liste_classement = top_3_des_scores(liste_scores)
    # On affiche les 3 scores
    afficher_scores(liste_classement)


def main ():
    # Tant que running est True
    running = True
    while running:
        # On appelle le menu qui nous permet de choisir une option
        running = menu_principal()

main()