from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._idMap = {}
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        for f in self._fermate:
            self._idMap[f._id_fermata] = f


    def buildGraph(self):
        self._grafo.add_nodes_from(self.fermate)
        # modo 1 doppio loop sui nodi e query per ogni arco
        """for u in self._fermate:
            for v in self._fermate:
                res = DAO.get_edges(u, v)
                if len(res) > 0:
                    self._grafo.add_edge(u, v)"""
        # modo 2 loop singolo sui nodi e query
        """for u in self._fermate:
            vicini = DAO.get_edges_vicini_v1(u)
            for v in vicini:
                v_nodo = self._idMap[v._id_stazA]
                self._grafo.add_edge(u, v_nodo)
                print(f"Added edge between:{u} and {v_nodo}")"""
        # modo 3 unica query che legge tutte le connessioni
        allConnessioni = DAO.get_all_connessioni()
        for c in allConnessioni:
            u_nodo = self._idMap[c.id_stazP]
            v_nodo = self._idMap[c.id_stazA]
            self._grafo.add_edge(u_nodo, v_nodo)
            print(f"Added edge between:{u_nodo} and {v_nodo}")
        print(len(allConnessioni))


    @property
    def fermate(self):
        return self._fermate

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)
