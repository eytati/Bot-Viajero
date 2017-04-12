import networkx as nx
import json

class creacion_de_grafo:
    grafo = nx.Graph()
    instance = None

    def __init__(self):
        if not self.grafo.instance:
            self.grafo.instance = self


    def carga_de_nodos(self):
        nodos = []
        with open('data2.json') as datos_json:
            nodos = json.load(datos_json)

            for contador in range(len (nodos["locations"])):
                self.grafo.add_node(nodos["locations"][contador].get('id'), nodos["locations"][contador])

    def carga_de_aristas(self):
        aristas = []
        with open('edges2.json') as datos_json:
            aristas = json.load(datos_json)
        for contador in range(len(aristas["routes"])):
            peso = aristas['routes'][contador].get('weight')
            self.grafo.add_edge(aristas['routes'][contador].get('a'), aristas['routes'][contador].get('b'), weight= peso)

    def create_edge(self, origin, destination, data_json):
        self.grafo.add_edge(origin, destination, data_json)



class accede_al_grafo:
    a = creacion_de_grafo()
    a.carga_de_nodos()
    a.carga_de_aristas()

    def ruta_mas_corta(self, id1, id2):
        b =nx.dijkstra_path(self.a.grafo, id1, id2)
        print(b)



a = accede_al_grafo()
a.ruta_mas_corta(5,8)
a.ruta_mas_corta(18,16)
a.ruta_mas_corta(24,8)
a.ruta_mas_corta(2,5)





