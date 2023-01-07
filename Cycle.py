# Ouvrir et lire le fichier
with open('kmers-data.txt', 'r') as f:
    reads_data = f.read().splitlines()

# Création de la liste de tuples
reads_data = [(reads_data[i], reads_data[i][:2], reads_data[i][-2:]) for i in range(len(reads_data))]

# Vérifie si le Dataset est vide ou si les éléments ont la bonne longueur
def check_dataset(dataset):

    if len(dataset) == 0:
        print('Error : Dataset is empty')
        
    for element in reads_data:
        if len(element[0]) != 3 or len(element[1]) != 2 or len(element[2]) != 2:
            print('Error : Wrong Dataset element length')

check_dataset(reads_data)

# Trouve un chemin Eulérien dans graph
def find_eulerian_path(visited, graph, longest_path):
    
    # Trouve les éléments voisins du dernier élément de la chaîne
    neighbors = [element for element in reads_data if element[1] == graph[-1][2] and element in visited]
    
    # Si il n'y a pas de correspondances, on vérifie si la chaîne est la plus longue possible
    if longest_path is None or len(longest_path) < len(graph):
        longest_path = graph[:]
    
    # Si il y a des voisins, alors on les ajoute au graph
    if len(neighbors) != 0:

        # Pour chaque élément voisin, on crée une copie du graph et de la liste des éléments déjà visités
        for i in neighbors:
            visited_copy = visited[:]
            graph_copy = graph[:]
            visited_copy.remove(i)
            graph_copy.append(i)


            # On appelle la fonction récursivement
            result = find_eulerian_path(visited_copy, graph_copy, longest_path)

            # Si la longueur du chemin est plus grande que la longueur du chemin le plus long, on le remplace           
            if len(longest_path) < len(result) and result  is not None:
                longest_path = result[:]

    # Si la longueur du chemin est égale à la longueur du graph, on retourne le graph
    if len(reads_data) == len(graph):
        return graph
    
    return longest_path

# Vérifie si le chemin Eulérien trouvé est le plus long
def check_graph(graph):
    
    lgt_graph = []
    # Pour chaque élément du graph, on appelle la fonction récursivement
    for element in graph:
        longest_path = None
        visited = reads_data[:]
        new_result = []

        # On ajoute l'élément au graph et on le supprime de la liste des éléments visités
        new_result.append(element)
        visited.remove(element)

        # Appel rcursif
        new_result = find_eulerian_path(visited, new_result, longest_path)
        
        # Si la longueur du chemin est plus grande que la longueur du chemin le plus long, on le remplace
        if len(lgt_graph) < len(new_result):
            lgt_graph = new_result[:]

    return lgt_graph


# Reconstruit le génome en utilisant la méthode d'overlapping
def overlap(result):  
    eulerian_path = result[0]
    # Pour tout les éléments du graph, on ajoute la dernière lettre de l'élément précédent
    for i in range(1, len(result)):
            eulerian_path += result[i][2]   
    return eulerian_path


result = [i[0] for i in check_graph(reads_data)]

# Appel des différents fonctions
eulerian_path = overlap(result)
print('Le chemin Eulérien le plus long est :',eulerian_path)



