Ce fichier explique comment lancer correctement le programme MesuresTrajetOptimal.py qui permet de générer un fichier de mesures des différentes méthodes. Ce programme ne concerne pas le problème du voyageur de commerce, mais la recherche d'un chemin optimal entre deux points.

Le programme MesuresTrajetOptimal.py fonctionne avec Dijkstra.py et ACO.py présents dans la même fork du projet github (Gustule/tm-aco)

===Mesurer l'efficacité des méthodes===

Afin de lancer correctement le programme, télécharger les trois programmes de cette fork puis ouvrir MesuresTrajetOptimal.py et modifier au besoin les variables suivantes :
- iterations (ligne 8) : définit le nombre de chemins qui vont être recherchés avec ACO, DIjkstra et la méthode aléatoire
- filename : le nom du fichier .csv dans lequel les données vont être stockées
- adresse : le nom du fichier .csv contenant le graphe à copier. Si vous ne possédez pas encore de graphe, vous pouvez en générer un en suivant les instructions dans 'Explications Dijkstra.txt' dans la fork principale du projet github.
- nombre_points : le nombre de points présents dans le graphe copié
- fonctions_methode_aleatoire : divers paramètres modifiables liés à la méthode aléatoire. Vous pouvez trouver plus d'informations dans 'Explications Dijkstra.txt'.

Si le fichier spécifié dans filename est ouvert lorsque le programme doit y écrire les données, il vous demandera de le fermer avant de sauvegarder les données.

===Obtenir les données===

Une fois le fichier de résultats ouvert il est possible de créer des graphes mettant en valeur les données obtenues. Il arrive que Excel ne considère pas ces valeurs comme numériques parce que certaines expériences windows utilisent ',' ou '.' pour les virgules. Utiliser Ctrl+F et 'remplacer tout' pour régler le problème.

===Ouvrir ACO et Dijkstra indépendamment===

Il est possible de faire tourner ACO directement depuis le programme ACO.py pour l'utiliser sans les mesures et afficher le résultat.
Pour Dijkstra et la méthode aléatoire, il faut mettre en commentaire les 'yield' à l'intérieur de la fonction execute() dans le programme Dijkstra.py pour que ça s'exécute correctement.
