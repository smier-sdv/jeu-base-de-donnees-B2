from jeu import *

# variable running comme condition de boucle du jeu
running = True

# Fonction d'affichage du menu
def menu_principal():
    # créer une liste d'options
    options = ["Lancer le jeu", "Voir le classement", "Quitter"]
    # afficher menu principal et récupérer un choix valide de l'utilisateur
    choix = récupérer_choix_utilisateur(options)
    #print(f"choix récupéré : {choix}")
    # si choix == 1:
    if choix == 1:
        # Lancer option 1, le jeu avec gameplay_loop()
        jeu = Jeu()
        jeu.gameplay_loop()
    # si choix == 2: 
    if choix == 2:
        # Lancer option 2, le classement
        classement()
    # si choix == 3:
    if choix == 3:
        # Lancer l'option 3 arrêter le jeu
        return False


# On affiche le classement
def classement():
    # On prend les 3 meilleurs scores de la bdd
    # si on n'a pas au moins 3 scores, on affiche " " à la place
    # On affiche les 3 derniers scores de la bdd
    ...


def main ():
    # Tant que running est True
    running = True
    while running:
        # On appelle le menu qui nous permet de choisir une option
        running = menu_principal()
        # On affiche le dernier score et le classement
        classement()

main()