import networkx as nx
import json


class creacion_de_grafo:


    def carga_de_nodos(self):
        nodos = []
        with open('data.json') as datos_json:
            nodos = json.load(datos_json)
            print(nodos)
        '''
        for contador in range(len (nodos["locations"])):
                grafo.add_node(contador, nodos[contador])
        print(str(grafo))
        '''

    def carga_de_aristas(self):
        aristas = []
        with open('edges.json') as datos_json:
            aristas = json.load(datos_json)
            print(aristas)

grafo = nx.Graph()
a = creacion_de_grafo()
a.carga_de_nodos()
a.carga_de_aristas()


'''
grafo.add_node(datos1.get("Id"),attr_dict=datos1)
grafo.add_edge(1,2, weight=0.9)
grafo.add_edge(1,2, weight=0.9)
grafo.add_edge(1,2, weight=0.9)

nx.dijkstra_path(grafo,1,2)


'''



