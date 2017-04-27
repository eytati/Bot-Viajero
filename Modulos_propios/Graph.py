import networkx as nx

class create_graph:
    grafo = nx.Graph()
    instance = None

    def __init__(self):
        if not self.grafo.instance:
            self.grafo.instance = self

    def create_node(self, name, data_json):
        self.grafo.add_node(name, data_json)

    def create_edge(self, origin, destination, weight):
        self.grafo.add_edge(origin, destination, weight = weight)

    def show_cities(self):
        cities = []
        for couter in self.grafo.node:
            graph_data = self.grafo.node[couter]
            if not graph_data == {}:
                id = graph_data['id']
                city = graph_data['ciudad']
                latitude = graph_data['latitude']
                longitude = graph_data['longitude']
                json_data = {"Id": id, "Ciudad": city, "Latitud": latitude, "Longitud": longitude}
                cities.append(json_data)
        print(cities)
        return cities

    def show_short_path(self, source, target):
            large_path= []
            path = nx.shortest_path(self.grafo, source, target)
            for node in range(len(path)):
                data = self.grafo.node[path[node]]
                if not data == {}:
                    id = data['id']
                    city = data['ciudad']
                    latitude =data['latitude']
                    longitude = data['longitude']
                    json_data = {"Id": id, "Ciudad": city, "Latitud": latitude, "Longitud": longitude}
                    large_path.append(json_data)
            print(large_path)
            return large_path

    def show_routes(self, source, target):
        exists = nx.has_path(self.grafo,  source, target)
        if exists is True:
            path = []
            for value in nx.all_shortest_paths(self.grafo, source, target, weight='weight'):
                for a in range(len(value)):
                    data = value[a]
                    new_data = self.grafo.node[data]
                    id = new_data['id']
                    city = new_data['ciudad']
                    latitude = new_data['latitude']
                    longitude = new_data['longitude']
                    json_data = {"Id": id, "Ciudad": city, "Latitud": latitude, "Longitud": longitude}
                    path.append(json_data)
            length = nx.shortest_path_length(self.grafo, source, target, weight='weight')
            return {"Camino": path, "Total de Km": length}
        return False

    def show_all_routes(self, source, target):
        exists = nx.has_path(self.grafo, source, target)
        if exists is True:
            path = []
            ruta = 0
            for value in nx.all_simple_paths(self.grafo, source, target):
                distance = 0
                for a in range(len(value)):
                    data_point1 = value[a]
                    if a < len(value)-1:
                        data_point2 = value[a+1]
                        new_data = self.grafo[data_point1][data_point2]['weight']
                        distance += new_data
                json_route = {"Numero de ruta": ruta, "Distancia": distance}
                ruta += 1
                path.append(json_route)
            return path
        return False

    def number_routes(self, source, target):
        exists = nx.has_path(self.grafo, source, target)
        counter = 0
        if exists is True:
            for value in nx.all_simple_paths(self.grafo, source, target):
                counter += 1
        return counter


