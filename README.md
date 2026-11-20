# jeu base de données B2

Ceci est un jeu où on forme une équipe de héros à partir d'une base de données pour combattre tour à tour des monstres sélectionnés aléatoirement.

Bibliothèques utilisées:
- Pymongo
- Random


**Menu principal:**

Il y a 3 choix présents dans le menu principal : 
1. Lancer le jeu
2. Afficher le classement
3. Quitter

On entre le numéro correspondant pour choisir.


**Classement**

Le classement affiche les 3 meilleurs scores dans l'historique du jeu, stockés dans la base de données.


**Jeu**

Au lancement du jeu, on nous demande d'entrer un pseudo. Celui-ci sera sauvegardé dans la base de données avec notre score en fin de partie.

Ensuite, on nous demande de choisir 3 membres de notre équipe en entrant le nombre correspondant à celui qui est affiché.

Une fois l'équipe formée, le jeu commence et les combats se lancent automatiquement. Un ennemi est choisi aléatoirement dans la base de données et les membres de votre équipe l'attaquent chacun leur tour. Puis, l'ennemi en attaque un au hasard en réponse.
Une fois l'ennemi battu, on passe à la vague suivante et le jeu envoie un nouvel ennemi choisi aléatoirement et le cycle continue.

Une fois que toute votre équipe a été vaincue, on affiche le nombre de vagues que vous avez terminé et on l'envoie dans la base de donnée avec votre pseudo.

Enfin on affiche le classement actuel des 3 meilleurs scores.

On est renvoyé au menu principal et on peut relancer une partie sans fermer et rouvrir le jeu.