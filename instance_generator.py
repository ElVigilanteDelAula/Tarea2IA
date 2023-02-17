#Generador de instancias de grafos ponderados
import random

instance = {}

#num_nodos = 
def create_instance(num_nodos):
    instance = {}
    for i in range(1, num_nodos+1):
        # Cuantos nodos adyacentes tiene el nodo i
        cuantos_adyacentes = random.randint(1, num_nodos-1)
        lista_nodos_adyacentes = random.sample (range(1, num_nodos), cuantos_adyacentes)
        while(i in lista_nodos_adyacentes):
            cuantos_adyacentes = random.randint(1, num_nodos-1)
            lista_nodos_adyacentes = random.sample(range(1, num_nodos), cuantos_adyacentes)

        lista_tuplas = []
        for j in range(0, len(lista_nodos_adyacentes)):
            lista_tuplas.append((lista_nodos_adyacentes[j], random.randint(1,1000)))
        instance[i] = lista_tuplas
    #print(instance)
    return(instance)