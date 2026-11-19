def afficher_options_numérotées(options):
    # pour chaque option dans enumerate(options, start=1)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    return


def construire_options_affichables(personnages_disponibles):
    # construire la liste des options à afficher disponibles
    # créer une liste options
    options = []
    # pour chaque personnage dans personnages_disponibles:
    for personnage in personnages_disponibles:
        # ajouter à la liste : f"{personnage["nom"]} - ATK : {personnage["ATK"]}- DEF : {personnage["DEF"]}"
        options.append(f"{personnage["NOM"]} - PV : {personnage["PV"]} - ATK : {personnage["ATK"]} - DEF : {personnage["DEF"]}")
    # retourner la liste d'options
    return options


def récupérer_choix_utilisateur(options):
    """Affiche les choix possibles et récupère le choix de l'utilisateur jusqu'à obtenir un résultat valide"""
    # tant que le choix n'est pas valide
    est_valide = False
    while not est_valide:
        # afficher options numérotées 
        afficher_options_numérotées(options)
        # récupérer le choix de l'utilisateur en demandant d'entrer un nombre entier entre le maximum et le minimum 
        choix = input(f"Veuillez entrer un nombre entier entre 0 et {len(options)}: ")
        est_valide = est_choix_valide(choix,options)
    return int(choix)
        

def est_choix_valide(choix,options):
    # vérifier si le choix est un nombre
    if not choix.isdigit():
        return False
    # vérifier si c'est un int
    if not int(choix).is_integer():
        return False
    # vérifier si le choix est entre le minimum et le maximum:
    if int(choix) <= 0 or int(choix) > len(options):
        return False
    return True


def top_3_des_scores(liste):
    scores=[]
    # On récupère les éléments souhaités de la base de donnée et on les trie
    for score in liste:
        scores.append([score['score'],score['nom']])
    # On met la liste dans l'ordre décroissant
    scores.sort(reverse = True)
    # On renvoie les 3 premiers éléments de la liste
    return scores[:3]

def afficher_scores(liste):
    # On affiche un par un les meilleurs scores
    print(f"Voici la liste des 3 meilleurs scores: ")
    # On ajoute un nombre à incrémenter pour afficher le classement
    i = 1
    for score,nom in liste: 
        # On affiche le score avec le nom du joueur de la partie concernée
        print(f"{i}. {nom} : {score}")
        # On incrémente i
        i+=1