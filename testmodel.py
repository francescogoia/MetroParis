from database.DAO import DAO
from model.model import Model

mymodel = Model()
mymodel.buildGraph()

myLinee = DAO.get_all_linee()

print(f"The grapg has {mymodel.getNumNodes()} nodes")
print(f"The graph has {mymodel.getNumEdges()} edges")
print(myLinee)