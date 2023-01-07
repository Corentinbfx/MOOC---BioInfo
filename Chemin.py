import random

# Ouverture et lecture du Dataset
dataset = open('kmers-data.txt','r')
lines = dataset.readlines()

path = []
graph = []

# Création une liste de tuples contenant les kmers (edge, first_node, second_node)
def create_graph(graph, lines):

  for line in lines:

    first_node = line[0] + line[1]
    second_node = line[1] + line[2]
    edge = line[0:3]
    graph.append((edge, first_node, second_node))

  return graph

# Trouve un chemin Eulérien dans graph
def find_eulerian_list(graph):

  random_kmers = random.choice(graph)
  path.append(random_kmers[0])
  graph.remove(random_kmers)

  lenght_path = len(graph)

  while lenght_path < 15:

    if graph:
      matches = [t for t in graph if t[1] == random_kmers[2]]
      
      if not matches:
        break

      random_kmers = random.choice(matches)
      path.append(random_kmers[0])
      graph.remove(random_kmers)
      lenght_path -= 1

  return path

# Reconstruit le génome en utilisant la méthode d'overlapping
def construction_genome(path):

    overlap = 2
    merged = path[0]

    for i in range(1, len(path)):

        merged += path[i][overlap:]

    return merged


# Appel des différents fonctions
graph = create_graph(graph, lines)
path = find_eulerian_list(graph)
genome = construction_genome(path)

print('Un des chemins Eulérien est :', genome)
