import networkx as nx
import json


class creacion_de_grafo:


    def carga_de_nodos(self,grafo):
        nodos = []
        with open('data.json') as datos_json:
            nodos = json.load(datos_json)
           # print(nodos)

            for contador in range(len (nodos["locations"])):
                grafo.add_node(nodos["locations"][contador].get('id'), nodos["locations"][contador])
        print(grafo)

    def carga_de_aristas(self,grafo):
        aristas = []
        with open('edges.json') as datos_json:
            aristas = json.load(datos_json)
        for contador in range(len(aristas["routes"])):
            grafo.add_edge(aristas['routes'][contador].get('a'),aristas['routes'][contador].get('b'), weight= aristas['routes'][contador].get('weight'))
           # grafo.add_node(aristas["routes"][contador].get('a'),aristas["routes"][contador].get('b'), weight= aristas["routes"][contador].get('weight') )

grafo = nx.Graph()
a = creacion_de_grafo()
a.carga_de_nodos(grafo)
a.carga_de_aristas(grafo)
print(grafo)
#a.carga_de_aristas()


'''
grafo.add_node(datos1.get("Id"),attr_dict=datos1)
grafo.add_edge(1,2, weight=0.9)
grafo.add_edge(1,2, weight=0.9)
grafo.add_edge(1,2, weight=0.9)

nx.dijkstra_path(grafo,1,2)


'''



