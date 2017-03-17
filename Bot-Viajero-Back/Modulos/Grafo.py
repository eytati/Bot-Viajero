import networkx as nx

datos1 = {
    "Id": 0,
    "longitud": 0.0,
    "latitud": 0.0,
    "nombre": ''
}
grafo = nx.Graph()
grafo.add_node(datos1.get("Id"),attr_dict=datos1)
grafo.add_edge(1,2, weight=0.9)
grafo.add_edge(1,2, weight=0.9)
grafo.add_edge(1,2, weight=0.9)

nx.dijkstra_path(grafo,1,2)






