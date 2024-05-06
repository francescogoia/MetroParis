from model.model import Model

mymodel = Model()
mymodel.buildGraph()

print(f"The grapg has {mymodel.getNumNodes()} nodes")
print(f"The graph has {mymodel.getNumEdges()} edges")