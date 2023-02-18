import timeit #se importo una libreria para obtener el tiempo de procesado

import grafo_ponderado as GRP
import instance_generator as ig

start = timeit.default_timer() #inicia el conteo del tiempo

# Grafo ejemplo con listas de adyacencia y pesos asociados
#grafo = {'A': [('B', 1), ('C', 2), ('D', 3)],
#         'B': [('A', 1), ('C', 4)],
#         'C': [('A', 2), ('B', 4), ('D', 5)],
#         'D': [('A', 3), ('C', 5)]}


def testGrafo():
    grafo = ig.create_instance(1000)
    g = GRP.WeightedGraph(grafo)    # Crear el grafo con el diccionario de ejemplo
    while(len(g.isolatedNodes())>0):
        grafo = ig.create_instance(1000)
        g = GRP.WeightedGraph(grafo)

    print('Grafo')
    print(g)                    # Visualizar el grafo
    print('Iteración')
    for n in g:                 # Iterar sobre los nodos y arcos del grafo
        print(n)
        print(g.edges(n))
    print('Nodos:', g.nodes())  # Visualizar todos los nodos
    print('Arcos:', g.edges())  # Visualizar todos los arcos

    print('\nComprobaciones')
    print('Vacío:', g.isEmpty())                    # Comprobar si grafo vacío
   
if __name__ == '__main__':
    testGrafo()

    stop = timeit.default_timer() #detiene la cuenta del tiempo

    print('Time: ', stop - start)