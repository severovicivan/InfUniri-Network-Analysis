# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 19:44:19 2019

@author: ivan.severovic
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

#Konstrukcija bipartitnog grafa
BG = nx.read_graphml('bipartitni_gfri.graphml')
    
def dohvati_cvorove_iz_particije(graf,particija):
    # Inicijaliziramo praznu listu u koju ćemo spremiti čvorove
    nodes = []
    # Iteriramo kroz sve čvorove grafa
    for n in graf.nodes():
        # Provjeravamo pripada li čvor traženoj particiji
        if graf.node[n]['bipartite'] == particija:
            # Ako pripada, dodajemo ga na listu čvorova
            nodes.append(n)
    return nodes
#Broj čvorova u particiji radovi
print('\nBroj znanstvenih radova: ' + str(len(dohvati_cvorove_iz_particije(BG, 'rad'))) + '\n')

#Broj znanstvenih radova na kojima je sudjelovao profesor Pavlić
#print('Broj znanstvenih radova na kojima je sudjelovao profesor Pavlić: '
#      + str(len(list(BG.neighbors('Pavlic Mile')))) + '\n')

#  5 autora s najviše suradnji na znanstvenim radovima
#Dohvaćamo particiju koja sadrži autore znanstvenih radova
autori = dohvati_cvorove_iz_particije(BG, 'autor')

print(len(autori))
print(sorted(autori))

stupnjevi_autora = []
for autor in autori:
    stupnjevi_autora.append(BG.degree(autor))
#print(list(reversed(sorted(stupnjevi_autora)))[:5])
for autor in autori:
    if BG.degree(autor) in list(reversed(sorted(stupnjevi_autora)))[:10]:
        print(autor + ' je sudjelovao na ' + str(BG.degree(autor)) + ' radova.')
        
#print(sorted(list(BG.neighbors('Karleusa Barbara'))))
        
#for n,naziv in enumerate(list(BG.neighbors('Arbanas Zeljko'))):
#    print('\n' + str(n) + ' - ' + naziv)
    
#      Računamo unipartitnu projekciju suradnika  
# Autori će biti povezani ako imaju zajedničku suranju
PG = nx.bipartite.projected_graph(BG,autori)
print('\nBroj čvorova projekcije autor: ' + str(len(PG.nodes())))
print('Broj bridova projekcije autor: ' + str(len(PG.edges())))
# Konstrukcija težinskog grafa
G2 = nx.read_graphml('gfri.graphml')
print('\nBroj čvorova težinskog grafa: ' + str(len(G2.nodes())))
print('Broj bridova težinskog grafa: ' + str(len(G2.edges())))
## Prosječan broj veza
#veze_cvorova = 0
#for cvor in G2.degree():
#    veze_cvorova += cvor[1]
#prosjek_veza = veze_cvorova/len(G2.nodes())
#print('\nProsječni stupanj grafa G2 je: ' + str(prosjek_veza))
#
#bridovi = pd.read_csv('gfri.csv')
#del bridovi['Unnamed: 0']
#G=nx.from_pandas_edgelist(bridovi, 'autor1', 'autor2', edge_attr=True, create_using=nx.MultiGraph())
##high_degree_people = [node for node in G.nodes() if node in bridovi.autor1.unique() and G.degree(node) > 30]
##people = [node for node in G.nodes() if node in bridovi.autor2.unique()]
##print(sorted(G.nodes()))
##with open("odjel.graphml", "wb") as ofile:
##    nx.write_graphml(G, ofile)
#godine = list(bridovi.godina.unique())
#godine.sort()
##Filtar kojim ćemo pratiti rast broja suradnji od 2007. godine
#filtar = godine[godine.index(2006):]
#Gs = []
#for godina in filtar:
#    # Instantiate a new undirected Multigraph: MG
#    MG = nx.MultiGraph()    
#    # Add in all nodes that have ever shown up to the graph
#    MG.add_nodes_from(bridovi['autor1'])
#    MG.add_nodes_from(bridovi['autor2'])    
#    # Filter the DataFrame so that there's only the given year
#    df_filtered = bridovi[bridovi['godina'] == godina]    
#    # Add edges from filtered DataFrame
#    MG.add_edges_from(zip(df_filtered['autor1'],df_filtered['autor2']))    
#    # Append G to the list of graphs
#    Gs.append(MG)    
#print(len(Gs))
#
## Instanciranje liste multigrafova koja će sadržavati veze nastale od 2007.
#novi_bridovi = []
#window = 1  
#i = 0      
#for i in range(len(Gs) - window):
#    g1 = Gs[i]
#    g2 = Gs[i + window]
#        
#    # Dodavanje bridova koje g2 ima, a g1 nema u listu novi_bridovi
#    novi_bridovi.append(nx.difference(g2, g1))
#print(len(novi_bridovi))
## Plot the number of edges added over time
#edges_added = [len(g.edges()) for g in novi_bridovi]
#print('Broj bridova nastalih od 2007. do danas: ' + str(sum(edges_added)))
#print('Graf ima: ' + str(len(G.edges())) + ' bridova.')
##podaci = zip(godine[1:],edges_added)
##print(list(podaci))
#fig = plt.figure(figsize=(13, 5))
#plt.bar(filtar[1:],edges_added)
#plt.xlabel('Godine', fontsize=18)
#plt.ylabel('Broj nastalih suradnji', fontsize=18)
#plt.show()
##print(sorted(Gs[-1].edges()))
#print('U ' + str(filtar[1]) + '. je nastalo: ' + str(edges_added[0]) + ' suradnji.')
#print('U ' + str(filtar[-1]) + '. je nastalo: ' + str(edges_added[-1]) + ' suradnji.\n')
#
## Dohvaćanje 10 najvećih jedinstvenih vrijednosti centralnosti stupnja čvora: top_dcs
#top_dcs = sorted(set(nx.degree_centrality(G).values()), reverse=True)[0:10]
## Kreiranje liste čvorova koji imaju 10 najvećih vrijednosti za centralnost stupnja čvora(degree centrality)
#top_connected = []
#for n, dc in nx.degree_centrality(G).items():
#    if dc in top_dcs:
#        top_connected.append(n)     
## Čvorovi s najvećim centralnostima stupnja čvora
#print(top_connected)
#
## Kreiramo defaultdict u kojem su čvorovi ključevi, a vrijednosti liste suradnji kroz godine
## Lista suradnji sadrži broj pojedinaca s kojima je čvor ostvario suradnju tokom godine
#connectivity = defaultdict(list)
#for n in top_connected:
#    for g in Gs:
#        connectivity[n].append(len(list(g.neighbors(n))))
##print(connectivity)
## Plot the connectivity for each node
#fig = plt.figure(figsize=(13, 5)) 
#for n, conn in connectivity.items(): 
#    plt.plot(conn, label=n)
##Dodajemo godine iz filtra umjesto brojeva (1-14)
#plt.xticks(np.arange(15), range(2006,2020))
#plt.legend()  
#plt.show()