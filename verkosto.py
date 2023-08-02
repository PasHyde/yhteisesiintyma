
import matplotlib.pyplot as plt
import networkx as nx

G_weighted = nx.Graph()

G_weighted.add_nodes_from(['Room.', '1.Kor.', '2.Kor.', 'Gal.', 'Ef.', 'Fil.', '2.Tess.', '1.Tim.', '2.Tim.', 'Tit.',
                           'Haer.',	'1 Apol.', 'Dial.',	'Pol.Fil.',	'1.Clem.',	'2.Clem.',	'Ign.',	'Ap.t.',	'Tek.t.',	'Protr.',	'Paed.'])


G_weighted.add_edge('Room.', '1.Kor.', weight=((0.20 + 1.8) / 2))
G_weighted.add_edge('Room.', '2.Kor.', weight=((0.3 + 2.0) / 2))
G_weighted.add_edge('Room.', 'Gal.', weight=((1.54 + 3.40) / 2))
G_weighted.add_edge('Room.', 'Ef.', weight=((0.10 + 1.25) / 2))
G_weighted.add_edge('Room.', 'Fil.', weight=((0.30 + 2.14) / 2))
G_weighted.add_edge('Room.', '1.Tim.', weight=((0.30 + 2.3) / 2))
G_weighted.add_edge('Room.', '2.Tim.', weight=((0.10 + 1.0) / 2))
G_weighted.add_edge('Room.', 'Tit.', weight=((0.20 + 1.81) / 2))
G_weighted.add_edge('Room.', 'Haer.', weight=((0.20 + 0.8) / 2))
G_weighted.add_edge('Room.', '1 Apol.', weight=((0.41 + 0.88) / 2))
G_weighted.add_edge('Room.', 'Dial.', weight=((1.85 + 1.4) / 2))
G_weighted.add_edge('Room.', 'Pol.Fil.', weight=((0.41 + 1.75) / 2))
G_weighted.add_edge('Room.', '1.Clem.', weight=((1.23 + 1.53) / 2))
G_weighted.add_edge('Room.', '2.Clem.', weight=((0.30 + 1.20) / 2))
G_weighted.add_edge('Room.', 'Ign.', weight=((0.10 + 1.66) / 2))
G_weighted.add_edge('Room.', 'Ap.t.', weight=((0.41 + 1.17) / 2))
G_weighted.add_edge('Room.', 'Protr.', weight=((0.41 + 0.78) / 2))
G_weighted.add_edge('Room.', 'Paed.', weight=((1.54 + 1.28) / 2))

G_weighted.add_edge('1.Kor.', 'Gal.', weight=((0.90 + 0.22) / 2))
G_weighted.add_edge('1.Kor.', '1.Tim.', weight=((0.90 + 0.76) / 2))
G_weighted.add_edge('1.Kor.', 'Tit.', weight=((0.90 + 0.90) / 2))
G_weighted.add_edge('1.Kor.', 'Dial.', weight=((0.90 + 0.07) / 2))
G_weighted.add_edge('1.Kor.', 'Pol.Fil.', weight=((0.90 + 0.43) / 2))
G_weighted.add_edge('1.Kor.', '1.Clem.', weight=((1.8 + 0.25) / 2))
G_weighted.add_edge('1.Kor.', 'Paed.', weight=((1.8 + 0.17) / 2))

G_weighted.add_edge('2.Kor.', '1 Apol.', weight=((1.33 + 0.44) / 2))
G_weighted.add_edge('2.Kor.', 'Dial.', weight=((1.33 + 0.15) / 2))
G_weighted.add_edge('2.Kor.', 'Pol.Fil.', weight=((1.33 + 0.86) / 2))
G_weighted.add_edge('2.Kor.', '1.Clem.', weight=((0.66 + 0.12) / 2))
G_weighted.add_edge('2.Kor.', 'Ap.t.', weight=((0.66 + 0.29) / 2))
G_weighted.add_edge('2.Kor.', 'Protr.', weight=((1.33 + 0.39) / 2))
G_weighted.add_edge('2.Kor.', 'Paed.', weight=((1.33 + 0.17) / 2))

G_weighted.add_edge('Gal.', 'Fil.', weight=((0.68 + 2.14) / 2))
G_weighted.add_edge('Gal.', '1.Tim.', weight=((0.22 + 0.77) / 2))
G_weighted.add_edge('Gal.', 'Tit.', weight=((0.22 + 0.90) / 2))
G_weighted.add_edge('Gal.', 'Haer.', weight=((0.45 + 0.8) / 2))
G_weighted.add_edge('Gal.', 'Dial.', weight=((1.13 + 0.39) / 2))
G_weighted.add_edge('Gal.', 'Pol.Fil.', weight=((0.22 + 0.43) / 2))
G_weighted.add_edge('Gal.', '1.Clem.', weight=((1.36 + 0.77) / 2))
G_weighted.add_edge('Gal.', '2.Clem.', weight=((0.22 + 0.4) / 2))
G_weighted.add_edge('Gal.', 'Ap.t.', weight=((0.45 + 0.58) / 2))
G_weighted.add_edge('Gal.', 'Paed.', weight=((1.36 + 0.51) / 2))

G_weighted.add_edge('Ef.', 'Fil.', weight=((1.25 + 0.71) / 2))
G_weighted.add_edge('Ef.', 'Dial.', weight=((1.25 + 0.07) / 2))
G_weighted.add_edge('Ef.', '1.Clem.', weight=((1.25 + 0.12) / 2))
G_weighted.add_edge('Ef.', 'Tek.t.', weight=((1.25 + 2.0) / 2))
G_weighted.add_edge('Ef.', 'Protr.', weight=((2.5 + 0.39) / 2))
G_weighted.add_edge('Ef.', 'Paed.', weight=((1.25 + 0.08) / 2))

G_weighted.add_edge('Fil.', 'Haer.', weight=((0.71 + 0.4) / 2))
G_weighted.add_edge('Fil.', 'Dial.', weight=((0.71 + 0.07) / 2))
G_weighted.add_edge('Fil.', 'Pol.Fil.', weight=((0.71 + 0.43) / 2))
G_weighted.add_edge('Fil.', '1.Clem.', weight=((0.71 + 0.12) / 2))
G_weighted.add_edge('Fil.', 'Tek.t.', weight=((0.71 + 2.0) / 2))
G_weighted.add_edge('Fil.', 'Paed.', weight=((1.42 + 0.17) / 2))

G_weighted.add_edge('2.Tess.', '2.Tim.', weight=((0.83 + 1.0) / 2))
G_weighted.add_edge('2.Tess.', 'Haer.', weight=((0.83 + 0.4) / 2))
G_weighted.add_edge('2.Tess.', 'Dial.', weight=((2.5 + 0.23) / 2))
G_weighted.add_edge('2.Tess.', '1.Clem.', weight=((0.83 + 0.12) / 2))
G_weighted.add_edge('2.Tess.', 'Ap.t.', weight=((0.83 + 0.29) / 2))
G_weighted.add_edge('2.Tess.', 'Protr.', weight=((1.66 + 0.39) / 2))
G_weighted.add_edge('2.Tess.', 'Paed.', weight=((2.5 + 0.25) / 2))

G_weighted.add_edge('1.Tim.', '2.Tim.', weight=((0.76 + 1.0) / 2))
G_weighted.add_edge('1.Tim.', 'Tit.', weight=((0.76 + 0.9) / 2))
G_weighted.add_edge('1.Tim.', 'Dial.', weight=((1.5 + 0.15) / 2))
G_weighted.add_edge('1.Tim.', 'Pol.Fil.', weight=((0.76 + 0.43) / 2))
G_weighted.add_edge('1.Tim.', '1.Clem.', weight=((0.76 + 0.12) / 2))
G_weighted.add_edge('1.Tim.', '2.Clem.', weight=((0.76 + 0.4) / 2))
G_weighted.add_edge('1.Tim.', 'Paed.', weight=((0.76 + 0.08) / 2))

G_weighted.add_edge('2.Tim.', 'Haer.', weight=((1.0 + 0.4) / 2))
G_weighted.add_edge('2.Tim.', 'Dial.', weight=((1.0 + 0.07) / 2))
G_weighted.add_edge('2.Tim.', 'Pol.Fil.', weight=((1.0 + 0.43) / 2))
G_weighted.add_edge('2.Tim.', '1.Clem.', weight=((1.0 + 0.12) / 2))
G_weighted.add_edge('2.Tim.', '2.Clem.', weight=((1.0 + 0.4) / 2))
G_weighted.add_edge('2.Tim.', 'Protr.', weight=((1.0 + 0.19) / 2))
G_weighted.add_edge('2.Tim.', 'Paed.', weight=((1.0 + 0.08) / 2))

G_weighted.add_edge('Tit.', 'Dial.', weight=((1.8 + 0.15) / 2))
G_weighted.add_edge('Tit.', '1.Clem.', weight=((1.8 + 0.25) / 2))
G_weighted.add_edge('Tit.', 'Protr.', weight=((0.9 + 0.19) / 2))
G_weighted.add_edge('Tit.', 'Paed.', weight=((0.9 + 0.08) / 2))

G_weighted.add_edge('Haer.', '1 Apol.', weight=((0.8 + 0.44) / 2))
G_weighted.add_edge('Haer.', 'Dial.', weight=((2.0 + 0.39) / 2))
G_weighted.add_edge('Haer.', 'Pol.Fil.', weight=((0.4 + 0.43) / 2))
G_weighted.add_edge('Haer.', '1.Clem.', weight=((2.0 + 0.64) / 2))
G_weighted.add_edge('Haer.', 'Ap.t.', weight=((0.4 + 0.29) / 2))
G_weighted.add_edge('Haer.', 'Tek.t.', weight=((0.4 + 2.0) / 2))
G_weighted.add_edge('Haer.', 'Paed.', weight=((1.2 + 0.25) / 2))

G_weighted.add_edge('1 Apol.', 'Dial.', weight=((1.7 + 0.6) / 2))
G_weighted.add_edge('1 Apol.', 'Pol.Fil.', weight=((0.22 + 0.43) / 2))
G_weighted.add_edge('1 Apol.', '1.Clem.', weight=((1.30 + 0.77) / 2))
G_weighted.add_edge('1 Apol.', '2.Clem.', weight=((1.11 + 2.0) / 2))
G_weighted.add_edge('1 Apol.', 'Ign.', weight=((0.22 + 1.6) / 2))
G_weighted.add_edge('1 Apol.', 'Ap.t.', weight=((0.9 + 1.17) / 2))
G_weighted.add_edge('1 Apol.', 'Tek.t.', weight=((0.22 + 2.0) / 2))
G_weighted.add_edge('1 Apol.', 'Protr.', weight=((0.66 + 0.6) / 2))
G_weighted.add_edge('1 Apol.', 'Paed.', weight=((1.77 + 0.68) / 2))

G_weighted.add_edge('Dial.', 'Pol.Fil.', weight=((0.23 + 1.3) / 2))
G_weighted.add_edge('Dial.', '1.Clem.', weight=((1.09 + 1.79) / 2))
G_weighted.add_edge('Dial.', '2.Clem.', weight=((0.23 + 1.2) / 2))
G_weighted.add_edge('Dial.', 'Ap.t.', weight=((0.39 + 1.47) / 2))
G_weighted.add_edge('Dial.', 'Protr.', weight=((1.09 + 2.74) / 2))
G_weighted.add_edge('Dial.', 'Paed.', weight=((3.1 + 3.4) / 2))

G_weighted.add_edge('Pol.Fil.', '1.Clem.', weight=((0.87 + 0.25) / 2))
G_weighted.add_edge('Pol.Fil.', '2.Clem.', weight=((0.43 + 0.4) / 2))
G_weighted.add_edge('Pol.Fil.', 'Ap.t.', weight=((0.43 + 0.29) / 2))
G_weighted.add_edge('Pol.Fil.', 'Protr.', weight=((0.43 + 0.19) / 2))
G_weighted.add_edge('Pol.Fil.', 'Paed.', weight=((0.86 + 0.17) / 2))

G_weighted.add_edge('1.Clem.', '2.Clem.', weight=((0.51 + 1.6) / 2))
G_weighted.add_edge('1.Clem.', 'Ign.', weight=((0.12 + 1.6) / 2))
G_weighted.add_edge('1.Clem.', 'Ap.t.', weight=((0.77 + 1.76) / 2))
G_weighted.add_edge('1.Clem.', 'Protr.', weight=((0.25 + 0.4) / 2))
G_weighted.add_edge('1.Clem.', 'Paed.', weight=((1.15 + 0.77) / 2))

G_weighted.add_edge('2.Clem.', 'Ign.', weight=((0.4 + 1.66) / 2))
G_weighted.add_edge('2.Clem.', 'Ap.t.', weight=((0.8 + 0.58) / 2))
G_weighted.add_edge('2.Clem.', 'Protr.', weight=((0.4 + 0.19) / 2))
G_weighted.add_edge('2.Clem.', 'Paed.', weight=((0.8 + 0.17) / 2))

G_weighted.add_edge('Ign.', 'Ap.t.', weight=((1.66 + 0.29) / 2))
G_weighted.add_edge('Ign.', 'Protr.', weight=((1.66 + 0.19) / 2))

G_weighted.add_edge('Ap.t.', 'Tek.t.', weight=((0.29 + 2.0) / 2))
G_weighted.add_edge('Ap.t.', 'Protr.', weight=((0.58 + 0.39) / 2))
G_weighted.add_edge('Ap.t.', 'Paed.', weight=((0.88 + 0.25) / 2))

G_weighted.add_edge('Protr.', 'Paed.', weight=((2.9 + 1.28) / 2))

elarge4 = [(u, v) for (u, v, d) in G_weighted.edges(data=True) if d["weight"] > 3]
elarge3 = [(u, v) for (u, v, d) in G_weighted.edges(data=True) if d["weight"] >= 2.5 < 3]
elarge1 = [(u, v) for (u, v, d) in G_weighted.edges(data=True) if d["weight"] >= 2 < 2.5]
elarge2 = [(u, v) for (u, v, d) in G_weighted.edges(data=True) if d["weight"] >= 1.5 < 2]
esmall2 = [(u, v) for (u, v, d) in G_weighted.edges(data=True) if d["weight"] >= 1 < 1.5]
esmall1 = [(u, v) for (u, v, d) in G_weighted.edges(data=True) if d["weight"] <= 1]

pos = nx.spring_layout(G_weighted)  # positions for all nodes - seed for reproducibility

# nodes
Y = [((97/6100)*100),((11/6000)*100),((15/4000)*100),((44/2000)*100),((8/2000)*100),((14/1500)*100),((12/800)*100),((13/1500)*100),((10/1100)*100),((11/550)*100),((25/40000)*100),
     ((45/20000)*100),((128/65000)*100),((23/2000)*100),((78/9500)*100),((25/5000)*100),((6/10000)*100),((34/15000)*100),((5/6000)*100),((51/22000)*100),((117/65000)*100)]
nx.draw_networkx_nodes(G_weighted, pos, node_size=[v * 400 for v in Y], node_color='deepskyblue')
# edges
nx.draw_networkx_edges(G_weighted, pos, edgelist=elarge4, width=9, alpha=0.5, edge_color="dodgerblue")
nx.draw_networkx_edges(G_weighted, pos, edgelist=elarge3, width=7, alpha=0.5, edge_color="steelblue")
nx.draw_networkx_edges(G_weighted, pos, edgelist=elarge1, width=6, alpha=0.5, edge_color="deepskyblue")
nx.draw_networkx_edges(G_weighted, pos, edgelist=elarge2, width=4, alpha=0.5, edge_color="skyblue")
nx.draw_networkx_edges(G_weighted, pos, edgelist=esmall2, width=2, alpha=0.5, edge_color="lightblue")
nx.draw_networkx_edges(G_weighted, pos, edgelist=esmall1, width=1, alpha=0.5, edge_color="powderblue")

# node labels
nx.draw_networkx_labels(G_weighted, pos, font_size=16, font_family="times", verticalalignment='bottom')

ax = plt.gca()
ax.margins(0.08)
plt.tight_layout()
plt.show()
