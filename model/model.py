from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._idMap = {}
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        for f in self._fermate:
            self._idMap[f._id_fermata] = f


    def getBFSNodes(self, source):
        edges = nx.bfs_edges(self._grafo, source)
        visited = []
        for u, v  in edges: # u, v = partenza e arrivo dell'arco
            visited.append(v)
            print(v)
        return visited

    def getDFSNodes(self, source):
        edges = nx.dfs_edges(self._grafo, source)
        visited = []
        for u, v in edges:
            visited.append(v)
            print(v)
        return visited



    def addEdgePesati(self):
        self._grafo.add_nodes_from(self._fermate)
        allConnessioni = DAO.get_all_connessioni()
        for c in allConnessioni:
            if self._grafo.has_edge(self._idMap[c.id_stazP],
                                    self._idMap[c.id_stazA]):
                # se l'arco c'è incremento il peso di 1
                self._grafo[self._idMap[c.id_stazP]][self._idMap[c.id_stazA]]["weight"] += 1
            else:
                self._grafo.add_edge(self._idMap[c.id_stazP], self._idMap[c.id_stazA], weight = 1)

    def getEdgeWeight(self, v1, v2):
        return self._grafo[v1][v2]["weight"]

    def buildGraph(self):
        self._grafo.clear()
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
            #print(f"Added edge between:{u_nodo} and {v_nodo}")
        print(f"Numero archi: {len(allConnessioni)}")

    def buildGraphPesato(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self.fermate)
        self.addEdgePesati()

    def getArchiPesoMaggiore(self):
        if (self._grafo.edges) == 0:
            print("Il grafo è vuoto")
            return
        else:
            edges = self._grafo.edges
            archiPesanti = []
            for u, v in edges:
                peso = self._grafo[u][v]["weight"]
                if peso > 1:
                    archiPesanti.append((u, v, peso))
                    print((u, v, peso))
            return archiPesanti


    @property
    def fermate(self):
        return self._fermate

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)
