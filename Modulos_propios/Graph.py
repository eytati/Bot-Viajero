import networkx as nx
import json

class create_graph:
    grafo = nx.Graph()
    instance = None

    def __init__(self):
        if not self.grafo.instance:
            self.grafo.instance = self

    def carga_de_nodos(self):
        nodos = []
        # collections_ciudades = string_connection.db.Ciudades
        with open('data2.json') as datos_json:
            nodos = json.load(datos_json)
            for contador in range(len(nodos["locations"])):
                city = nodos["locations"][contador].get('ciudad')
                json_data = nodos["locations"][contador]
                self.grafo.add_node(city, json_data)
            # collections_ciudades.insert(json_data)

    def carga_de_aristas(self):
        aristas = []
        with open('edges2.json') as datos_json:
            aristas = json.load(datos_json)
        for contador in range(len(aristas["routes"])):
            peso = aristas['routes'][contador].get('weight')
            self.grafo.add_edge(aristas['routes'][contador].get('a'), aristas['routes'][contador].get('b'), weight=peso)





    def create_node(self, name, data_json):
        self.grafo.add_node(name, data_json)


    def create_edge(self, origin, destination, data_json):
        self.grafo.add_edge(origin, destination, data_json)

    def show_cities(self):
        cities = []
        for couter in self.grafo.node:
            graph_data = self.grafo.node[couter]
            if not graph_data == {}:
                city = graph_data['ciudad']
                cities.append(city)
        print(cities)
        return cities

    def show_routes(self):
        counter = 0
        '''

        for ruta in  nx.all_simple_paths(self.grafo, "Liberia", "Puerto Jimenez"):
            for valor in range(len(ruta)):



            print(ruta)
            counter+=1
            '''
        print('=======ruta======')
        print(self.grafo.nodes())

a = create_graph()
a.carga_de_nodos()
a.carga_de_aristas()
a.show_cities()
a.show_routes()


# todas las rutas  for path in nx.all_simple_paths(G, source=0, target=3):
# Existe una ruta = nx.has_path(self.grafo, "Liberia", "Puerto Jimenez")
# todas las rutas cortas =  nx.all_shortest_paths(G,source=0,target=2)
#largo de la mas corta = nx.shortest_path_length(G,source=0,target=4
#nx.dijkstra_path(G,0,4)




'''
class accede_al_grafo:
    a = creacion_de_grafo()
    a.carga_de_nodos()
    a.carga_de_aristas()

    def ruta_mas_corta(self, id1, id2):
        b =nx.dijkstra_path(self.a.grafo, id1, id2)

        print(b)




a.ruta_mas_corta(18,16)
a.ruta_mas_corta(24,8)
a.ruta_mas_corta(2,5)
'''

'''


     def carga_de_aristas(self):
        aristas = []
        with open('edges2.json') as datos_json:
            aristas = json.load(datos_json)
        for contador in range(len(aristas["routes"])):
            peso = aristas['routes'][contador].get('weight')
            self.grafo.add_edge(aristas['routes'][contador].get('a'), aristas['routes'][contador].get('b'), weight= peso)


        def carga_de_nodos(self):
        nodos = []
        #collections_ciudades = string_connection.db.Ciudades
        with open('data2.json') as datos_json:
            nodos = json.load(datos_json)
            for contador in range(len(nodos["locations"])):
                city = nodos["locations"][contador].get('id')
                json_data = nodos["locations"][contador]
                self.grafo.add_node(city, json_data)
               # collections_ciudades.insert(json_data)

a = create_graph()
a.carga_de_nodos()
a.show_cities()
'''


