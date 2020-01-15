# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 19:44:19 2019

@author: ivan.severovic
"""
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

#Konstrukcija bipartitnog grafa
bridovi_bg = pd.read_csv('odjeli_bg.csv')
del bridovi_bg['Unnamed: 0']
BG = nx.Graph()
cvorovi_bg = pd.read_csv('odjeli_bg_cvorovi.csv')
del cvorovi_bg['Unnamed: 0']

# Dodajemo čvorove iz svake particije te ih povezujemo
for r, d in cvorovi_bg.iterrows():
    if d['bipartite'] == 'autor':
        BG.add_node(d['autor/rad'],bipartite=d['bipartite'])
    else:
        BG.add_node(d['autor/rad'],bipartite=d['bipartite'],godina=int(d['godina']))
for r, d in bridovi_bg.iterrows():
    BG.add_edge(d['autor'],d['rad'])
    
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
stupnjevi_autora = []
for autor in autori:
    stupnjevi_autora.append(BG.degree(autor))
#print(list(reversed(sorted(stupnjevi_autora)))[:5])
for autor in autori:
    if BG.degree(autor) in list(reversed(sorted(stupnjevi_autora)))[:10]:
        print(autor + ' je sudjelovao na ' + str(BG.degree(autor)) + ' radova.')
        
#      Računamo unipartitnu projekciju suradnika  
# Autori će biti povezani ako imaju zajedničku suranju
PG = nx.bipartite.projected_graph(BG,autori)
print('\nBroj čvorova projekcije: ' + str(len(PG.nodes())))
print('Broj bridova projekcije: ' + str(len(PG.edges())))

# 1. Broj čvorova N, broj veza K, prosječni broj veza <k>
# Konstrukcija težinskog grafa
G2 = nx.read_graphml('odjel.graphml')
print('\nBroj čvorova težinskog grafa: ' + str(len(G2.nodes())))
print('Broj bridova težinskog grafa: ' + str(len(G2.edges())))

# Prosječan broj veza
veze_cvorova = 0
for cvor in G2.degree():
    veze_cvorova += cvor[1]
prosjek_veza = veze_cvorova/len(G2.nodes())
print('\nProsječni stupanj grafa G2 je: ' + str(prosjek_veza))

# 3. Ukoliko je mreža težinska dodatno računati prosječnu snagu
snage_cvorova = []
for cvor in G2.degree(weight='weight'):
    snage_cvorova.append(cvor[1])
prosjek_snage = sum(snage_cvorova)/len(G2.nodes())
print('\nProsječna snaga grafa G2 je: ' + str(prosjek_snage) + '\n')

# 4. Odrediti broj komponenti i veličinu najveće komponente (broj čvovova i veza)
print('\nBroj povezanih komponenti: ' + str(nx.number_connected_components(G2)))
najveca = max(nx.connected_component_subgraphs(G2), key=len)
print('\nBroj čvorova najveće povezane komponente: ' + str(len(najveca.nodes())))
print('\nBroj bridova najveće povezane komponente: ' + str(len(najveca.edges())))

# 5. Odrediti mjere udaljenosti za cijelu mrežu (avg. shortest path length, diameter, eccentricity)
putevi = []
for komponenta in nx.connected_component_subgraphs(G2):
    putevi.append(nx.average_shortest_path_length(komponenta,weight='weight'))
print('\nProsječna duljina najkraćih puteva: ' + str(sum(putevi)/len(putevi)))
dijametri = []
for komponenta in nx.connected_component_subgraphs(G2):
    dijametri.append(nx.diameter(komponenta))
print('\nDijametar mreže: ' + str(sum(dijametri)/len(dijametri)))
ekscentricnosti = []
for komponenta in nx.connected_component_subgraphs(G2):
    ekscentricnost = nx.eccentricity(komponenta).values()
    ekscentricnosti.append(sum(ekscentricnost)/len(ekscentricnost))
print('\nEkscentričnost mreže: ' + str(sum(ekscentricnosti)/len(ekscentricnosti)))

#       6.zd. PITANJE: Treba li uzimati u obzir i težine?
#Tada je duljina puta zbroj recipročnih vrijednosti težina veza između čvorova.
print('\nGlobalna učinkovitost grafa: ' + str(nx.global_efficiency(G2)))
#       7.i 8.zd. PITANJE: Razlika globalni i prosječni ccoef
print('\nProsječni koeficjent grupiranja: ' + str(nx.average_clustering(G2,weight='weight')))

# 9. Izračunati asortativnost obzirom na stupanj čvora - hubovi se baš ne spajaju međusobno
print('\nAsortativnost: ' + str(nx.degree_assortativity_coefficient(G2,weight='weight')))

# 10. Nacrtati dijagram disturibucije stupnjeva - POLINOMNA
stupnjevi = [G2.degree(n) for n in G2.nodes()]
plt.figure(figsize=(11, 5))
plt.hist(stupnjevi)
plt.xticks(np.arange(min(stupnjevi), max(stupnjevi)+1, 1.0))
plt.xlabel('Stupanj čvora', fontsize=18)
plt.ylabel('Broj čvorova', fontsize=18)
plt.title('Dijagram distribucije stupnjeva',fontsize=18)
plt.show()
#print('Broj suradnika: ' + str(G2.degree('Pavlic Mile')))

# 10.5 Nacrtati dijagram disturibucije snage
plt.figure(figsize=(11, 5))
plt.hist(snage_cvorova)
plt.xticks(np.arange(min(snage_cvorova), max(snage_cvorova)+1, 5))
plt.xlabel('Snaga čvora', fontsize=18)
plt.ylabel('Broj čvorova', fontsize=18)
plt.title('Dijagram distribucije snage',fontsize=18)
plt.show()
print('Broj najviše suradnji: ' + str(G2.degree('Pavlic Mile',weight='weight')))

#               Analiza mreže na lokalnoj razini
# 11. Odrediti centralne čvorove prema različitim mjerama centralnosti
# 11.a) Centralnost stupnja čvora
# Dohvaćanje 10 najvećih jedinstvenih vrijednosti centralnosti stupnja čvora: top_dcs
top_dcs = sorted(set(nx.degree_centrality(G2).values()), reverse=True)[0:9]
# Kreiranje liste čvorova koji imaju 10 najvećih vrijednosti za centralnost stupnja čvora(degree centrality)
top_connected = []
for n, dc in nx.degree_centrality(G2).items():
    if dc in top_dcs:
        top_connected.append((n,dc))     
# Čvorovi s najvećim centralnostima stupnja čvora
print('\n10 osoba s najvećom centralnosti stupnja čvora: ')
print(top_connected)

# 11.b) Centralnost međupoloženosti
# Dohvaćanje 10 najvećih jedinstvenih vrijednosti centralnosti međupoloženosti: top_bcs
top_bcs = sorted(set(nx.betweenness_centrality(G2,weight='weight').values()), reverse=True)[0:9]
# Kreiranje liste čvorova koji imaju 10 najvećih vrijednosti za centralnost stupnja čvora(degree centrality)
najbitniji = []
for n, bc in nx.betweenness_centrality(G2,weight='weight').items():
    if bc in top_bcs:
        najbitniji.append((n,bc))     
# Čvorovi s najvećim centralnostima stupnja čvora
print('\n10 osoba s najvećom centralnosti međupoloženosti: ')
print(najbitniji)

# 11.c) Centralnost blizine
# Dohvaćanje 10 najvećih jedinstvenih vrijednosti centralnosti međupoloženosti: top_bcs
top_ccs = sorted(set(nx.closeness_centrality(G2).values()), reverse=True)[0:9]
# Kreiranje liste čvorova koji imaju 10 najvećih vrijednosti za centralnost stupnja čvora(degree centrality)
najpristupacniji = []
for n, cc in nx.closeness_centrality(G2).items():
    if cc in top_ccs:
        najpristupacniji.append((n,cc))     
# Čvorovi s najvećim centralnostima stupnja čvora
print('\n10 osoba s najvećom centralnosti blizine: ')
print(najpristupacniji)

# 12. Odrediti prosječnu centralnost blizine
blizine_cvorova = []
for n, cc in nx.closeness_centrality(G2).items():
    blizine_cvorova.append(cc)
prosjek_blizine = sum(blizine_cvorova)/len(G2.nodes())
print('\nProsječna centralnost blizine grafa G2 je: ' + str(prosjek_blizine) + '\n')

# 13. Odrediti prosječnu međupoloženost
medupolozenosti_cvorova = []
for n, bc in nx.betweenness_centrality(G2,weight='weight').items():
    medupolozenosti_cvorova.append(bc)
prosjek_medupolozenosti = sum(medupolozenosti_cvorova)/len(G2.nodes())
print('Prosječna centralnost međupoloženosti grafa G2 je: ' + str(prosjek_medupolozenosti) + '\n')

#                 Analiza mreže na središnjoj razini
# 14. Napraviti podjelu u zajednice te izračunati modularnost mreže za takvu podjelu u zajednice.
#     Ispisati broj čvorova i veza za prvih 10 najvećih zajednica u mreži.

print(nx.algorithms.community.greedy_modularity_communities(G2,weight='weight'))
#print(list(nx.find_cliques(G2)))


##ANALIZA BIPARTITNOG GRAFA
#print('\n5 najstarijih radova: ')
#print([(n,list(BG.neighbors(n)),BG.nodes[n]['godina']) for n in BG.neighbors('Pavlic Mile')][:5])
#suradnici = [n for n in BG.nodes() if BG.node[n]['bipartite'] == 'autor']
#
#print('\n')
##Centralnosti stupnja čvora - 5 s najvećim brojem radova
#dcs = nx.bipartite.degree_centrality(BG,suradnici)
#sortirani_dcs = {k: v for k, v in sorted(dcs.items(), key=lambda item: item[1])}
#for x in list(reversed(list(sortirani_dcs)))[0:5]:
#    print (x)
#print('\n')
#print(len(list(PG.neighbors('Pavlic Mile'))))
#
##print(len(list(G.neighbors('Pavlic Mile'))))
##Konstrukcija multigrafa
#bridovi = pd.read_csv('odjel_mg.csv')
#del bridovi['Unnamed: 0']
#G=nx.from_pandas_edgelist(bridovi, 'autor1', 'autor2', edge_attr=True, create_using=nx.MultiGraph())
##high_degree_people = [node for node in G.nodes() if node in bridovi.autor1.unique() and G.degree(node) > 30]
##people = [node for node in G.nodes() if node in bridovi.autor2.unique()]
##print(sorted(G.nodes()))
#godine = list(bridovi.godina.unique())
#godine.sort()
##Filtar kojim ćemo pratiti broj suradnji po godini od 2007.
#filtar = godine[godine.index(2009):]
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
#top_dcs = sorted(set(nx.degree_centrality(G).values()), reverse=True)[0:9]
## Kreiranje liste čvorova koji imaju 10 najvećih vrijednosti za centralnost stupnja čvora(degree centrality)
#top_connected = []
#for n, dc in nx.degree_centrality(G).items():
#    if dc in top_dcs:
#        top_connected.append(n)     
## Čvorovi s najvećim centralnostima stupnja čvora
#print('10 osoba s najvećom centralnosti stupnja čvora: ')
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
#plt.xticks(np.arange(12), filtar)
#plt.xlabel('Godine', fontsize=18)
#plt.ylabel('Broj suradnika', fontsize=18)
#plt.legend()  
#plt.show()
#print('\nBroj suradnji osobe: ' + str(G.degree('Pavlic Mile')))
#print('Broj jedinstvenih suradnika osobe: ' + str(len(list(G.neighbors('Pavlic Mile')))) + '\n')
#
##ANALIZA TEŽINSKOG GRAFA
#TG = nx.read_graphml()