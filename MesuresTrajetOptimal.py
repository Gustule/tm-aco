from Dijkstra import execute as execute_dijkstra
from ACO import execute as execute_aco
import time, random, csv
from functools import wraps # permet de créer un décorateur qui appelle une fonction sans ses prints internes


#--------------
iterations = 10
filename = 'Résultats.csv'
adresse = 'GrapheFile.csv'
#--------------
nombre_points = 100
fonctions_methode_aleatoire = {
    'iterations': 5,
    'mode': 2,
    'precision longueur': 20   # La différence de longueur max (en %) entre la longueur minimale et la longueur min aléatoire quand le mode aléatoire vaut 2
}
#--------------

def decorateur_sans_print(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_print = print
        print = lambda *args, **kwargs: None
        result = func(*args, **kwargs)
        print = original_print
        return result
    return wrapper





def execute_for_1_path(path, resultslist:list):
    dijkstra_measure = list(execute_dijkstra(adresse, path, 'copie', nombre_points, fonctions_methode_aleatoire, 0))
    new_line = dijkstra_measure
    try : aco_measure = execute_aco(adresse, path)
    except : return 0
    print('\n\n', aco_measure)
    new_line.append(aco_measure)
    print('--->', new_line)
    resultslist.append(new_line)
    return 1


def swap_points(adresse):
    pass



def execute(iterations, filename):
    t0_overall = time.time()

    results = []
    iteration_time = 0
    for i in range(iterations):
        t0 = time.time()
        p0 = random.randint(0,nombre_points-1)
        p1 = p0
        while p1 == p0:
            p1 = random.randint(0,nombre_points-1)
        trajet = (p0, p1)
        print('/ / / / / / / / / / / / / /\nItération {}, trajet: {}\n'.format(i, trajet))
        check_ok = execute_for_1_path(trajet, results)
        iteration_time = time.time() - t0 
        print('Durée de l\'itération :', iteration_time, '\ \ \ \ \ \ \ \ \ \ \ \ \ \n\n')
        # if not check_ok: break

    # for line in results: print(line)

    loop = True
    while loop:
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                # writer.writerow('SEP=,')    # Permet d'ouvrir le fichier csv dans excel en séparant les données en colonnes
                for row in [
                    ['SEP=,'],
                    ['Dijkstra',     '',         'Méthode aléatoire',    '',         'ACO',       ''         ],
                    ['Temps [s]',    'Longueur', 'Temps [s]',            'Longueur', 'Temps [s]', 'Longueur' ]
                    ]:
                    writer.writerow(row)

                print('Hey')

                for line in results:
                    row = []
                    for i in line:
                        for j in i:
                            row.append(j)
                    writer.writerow(row)
                    loop = False
        except: 
            if input(f"{filename} est ouvert. Fermer le fichier puis appuyer sur une touche pour réessayer.\nAppuyer sur S pour arrêter le programme.") in ['S', 's']:
                break

    overall_time = time.time() - t0_overall
    print("---> Temps d'exécution total :", overall_time)

execute(iterations, filename)