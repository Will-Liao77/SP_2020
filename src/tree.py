import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_node("ROOT")

for i in range(1,3):
	
	G.add_node("Child_%i" %i)
	G.add_node("Grandchild_%i" %i)
	G.add_node("Greatgrandchild_%i" %i)

	G.add_edge("ROOT", "Child_%i" %i)
	G.add_edge("Child_%i" %i , "Grandchild_%i" %i)
	G.add_edge("Grandchild_%i" %i , "Greatgrandchild_%i" %i)


nx.nx_agraph.write_dot(G,'test.dot')

plt.title('draw_networkx')
pos = graphviz_layout(G, prog='dot')
nx.draw(G, pos, with_labels=True, arrows=False)

plt.savefig('nx_test.png')
