import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()


relations = [
    ("john", "mary", "parent"),
    ("john", "steve", "parent"),
    ("mary", "alice", "parent"),
    ("mary", "bob", "parent"),
    ("alice", "carol", "parent"),
    ("alice", "david", "parent"),
    ("bob", "emily", "parent"),
    ("bob", "frank", "parent"),
]


genders = [
    ("john", "male", "is-a"),
    ("steve", "male", "is-a"),
    ("bob", "male", "is-a"),
    ("carol", "male", "is-a"),
    ("david", "male", "is-a"),
    ("frank", "male", "is-a"),
    ("mary", "female", "is-a"),
    ("alice", "female", "is-a"),
    ("emily", "female", "is-a"),
]


for subj, obj, rel in relations + genders:
    G.add_edge(subj.capitalize(), obj.capitalize(), label=rel)


pos = nx.spring_layout(G, k=0.8, seed=42)


plt.figure(figsize=(10, 7))
nx.draw(
    G, pos,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=9,
    font_weight="bold",
    arrowsize=15
)


edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", font_size=9)

plt.title("Semantic Net from Prolog Knowledge Base", fontsize=12, fontweight="bold")
plt.show()