# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 17:58:17 2019

@author: ivan.severovic
"""

#IMPORTS
from matplotlib import pyplot as plt
from nxviz import plots
from utils import doubleprint 
from utils import check_folder as cf
from itertools import combinations 
from bs4 import BeautifulSoup
import pandas as pd
import networkx as nx
import requests
import os
import re


#CONSTANTS
if __name__=='__main__':
    TXT='data\\txt\\'
    cf(TXT)
    VERBOSE=True   
    VERSION=''
    LOG_NAME=os.path.basename(__file__)[:-3]
    LOG=TXT+'{}{}.log'.format(LOG_NAME,VERSION)
    HRVATSKA = 'hrvatska\\'
    cf(HRVATSKA)
    #SVIJET = 'svijet\\'
    #cf(SVIJET)
#INPUT='[name_of_file].xlsx'

#VERSION NOTES
"""
version:description
"""

#CLASSES


#INITIALIZATION
#fresh log for each run
if __name__=='__main__' and os.path.exists(LOG):
    os.remove(LOG)
#data=make_or_load_pickle(LOG,'tmp_{}_data'.format(INPUT),lambda : read_excel(LOG,INPUT))
   
#FUNCTIONS
def odjel_zadnja(LOG=''):
    url = "https://www.bib.irb.hr/pretraga?operators=and%7CSveu%C4%8Dili%C5%A1te%20u%20Rijeci%20-%20Odjel%20za%20informatiku%20%28318%29%7Ctext%7Cinstitution&group=journal_articles%7Cconference_proceedings&subgroup=ja-original_scientific_papers%7Ccpr-scientific_proceedings&order_by=year_asc&page=1"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    stranice = soup.find('div', class_="text-center")
    stranice1 = stranice.find_all('a')[-2]
    print(stranice1)
    global zadnja
    zadnja = stranice1.text
    print(zadnja)
    
def gfri_zadnja(LOG=''):
    url = "https://www.bib.irb.hr/pretraga?operators=and%7CGra%C4%91evinski%20fakultet%2C%20Rijeka%20%28114%29%7Ctext%7Cinstitution&group=journal_articles%7Cconference_proceedings&subgroup=ja-original_scientific_papers%7Ccpr-scientific_proceedings&order_by=year_asc&page=1"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    stranice = soup.find('div', class_="text-center")
    stranice1 = stranice.find_all('a')[-2]
    print(stranice1)
    global zadnja_gfri
    zadnja_gfri = stranice1.text
    print(zadnja_gfri)
    
def provjera(bridovi,LOG=''):
    for n, brid in enumerate(bridovi):
        if brid == 'Ivasic Marina':
            bridovi[n] = 'Ivasic-Kos Marina'
        if brid == 'Ivasic-Kos M.':
            bridovi[n] = 'Ivasic-Kos Marina'
        if brid == 'Ivasic Kos Marina':
            bridovi[n] = 'Ivasic-Kos Marina'
        if brid == 'Holenko Martina':
            bridovi[n] = 'Holenko Dlab Martina'
        if brid == 'Holenko Dlab M.':
            bridovi[n] = 'Holenko Dlab Martina'
        if brid == 'Martina Holenko Dlab':
            bridovi[n] = 'Holenko Dlab Martina'
        if brid == 'Asenbrener Martina':
            bridovi[n] = 'Asenbrener Katic Martina'
        if brid == 'Brkic Marija':
            bridovi[n] = 'Brkic Bakaric Marija'
        if brid == 'Brkic M.':
            bridovi[n] = 'Brkic Bakaric Marija'
        if brid == 'Matetic M.':
            bridovi[n] = 'Matetic Maja'
        if brid == 'Frankovic I.':
            bridovi[n] = 'Frankovic Ivona'
        if brid == 'Đurovic G.':
            bridovi[n] = 'Đurovic Gordan'
        if brid == 'Martincic-Ipsic sanda':
            bridovi[n] = 'Martincic-Ipsic Sanda'
        if brid == 'Martincic- Ipsic Sanda':
            bridovi[n] = 'Martincic-Ipsic Sanda'
        if brid == 'Martincic - Ipsic Sanda':
            bridovi[n] = 'Martincic-Ipsic Sanda'
        if brid == 'Martincic–Ipsic Sanda':
            bridovi[n] = 'Martincic-Ipsic Sanda'
        if brid == 'Hoic-Bozic N.':
            bridovi[n] = 'Hoic-Bozic Natasa'
        if brid == 'Hoic- Bozic Natasa':
            bridovi[n] = 'Hoic-Bozic Natasa'
        if brid == 'Hoic- Bozic Natasa.':
            bridovi[n] = 'Hoic-Bozic Natasa'
        if brid == 'mestrovic Ana':
            bridovi[n] = 'Mestrovic Ana'
        if brid == 'Miletic Vedran Svedruzic Zeljko M.':
            bridovi[n] = 'Miletic Vedran'
            bridovi.append('Svedruzic Zeljko')
        if brid == 'Jaksic Danijela Poscic Patrizia':
            bridovi[n] = 'Jaksic Danijela'
            bridovi.append('Poscic Patrizia')
            #bridovi[n+1] = 'Poscic Patrizia'
        if brid == 'Subotic Danijela':
            bridovi[n] = 'Jaksic Danijela'
        if brid == 'Jaksic  Danijela':
            bridovi[n] = 'Jaksic Danijela'
        if brid == 'Nacinovic Lucia':
            bridovi[n] = 'Nacinovic Prskalo Lucia'
        if brid == 'Orlic Mandi':
            bridovi[n] = 'Orlic Bachler Mandi'
        if brid == 'Jakupovic  Alen':
            bridovi[n] = 'Jakupovic Alen'
        if brid == 'Kovacic  Bozidar':
            bridovi[n] = 'Kovacic Bozidar'
        if brid == 'Looi Chee-Kit.':
            bridovi[n] = 'Looi Chee-Kit'
        if brid == 'Looi Chee Kit':
            bridovi[n] = 'Looi Chee-Kit'
        if brid == 'Looi Chee Kit':
            bridovi[n] = 'Looi Chee-Kit'
        if brid == 'Zhang Xiaoshuan':
            bridovi[n] = 'Xiaoshuan Zhang'
        if brid == 'Gligora Markovic  Maja':
            bridovi[n] = 'Gligora Markovic Maja'
        if brid == 'Lado Kranjcevic Boris Pirkic':
            bridovi[n] = 'Kranjcevic Lado'
            bridovi.append('Pirkic Boris')
        if brid == 'Kovcic Bozidar':
            bridovi[n] = 'Kovacic Bozidar'
        if brid == '':
            del bridovi[n]
    return bridovi
    
def ekstrakcija_odjel(LOG=''):
    MG = nx.MultiGraph()
    BG = nx.Graph()
    G = nx.Graph()
    for i in range(1,int(zadnja)+1): 
        url = "https://www.bib.irb.hr/pretraga?operators=and%7CSveu%C4%8Dili%C5%A1te%20u%20Rijeci%20-%20Odjel%20za%20informatiku%20%28318%29%7Ctext%7Cinstitution&group=journal_articles%7Cconference_proceedings&subgroup=ja-original_scientific_papers%7Ccpr-scientific_proceedings&order_by=year_asc&page="+str(i)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        radovi = soup.find('ul', class_="list-unstyled")
        #print(radovi)
        radovi1 = radovi.find_all('li')
        #print(radovi1)
        
        for rad in radovi1:
            naslov = rad.a.text
            print(naslov)
            godina = rad.find('span',class_="citation")
            s = godina.text
            try:                
                napisan = re.findall('[2][0][0-2][0-9]', s)[0]
                print(napisan)
                autori = rad.find('div',class_="authors")
                #print(autori)        
                cvorovi = re.sub("\(.*\)","", autori.text.replace(',', '').
                                 replace('š', 's').replace('Š', 'S').
                                 replace('č', 'c').replace('Č', 'C').
                                 replace('ć', 'c').replace('Ć', 'C').
                                 replace('ž', 'z').replace('Ž', 'Z'))
                #print(cvorovi)
                bridovi = cvorovi.split(";")
                bridovi = [cvor.strip() for cvor in bridovi]
                print(bridovi)
                provjera(bridovi)
                #Konstrukcija bipartitnog grafa
                if naslov in BG:
                    for cvor in bridovi:
                        BG.add_node(naslov + ' - ' + napisan,bipartite='rad',particija=2,godina=int(napisan))
                        BG.add_node(cvor,bipartite='autor',particija=1)
                        BG.add_edge(cvor,naslov + ' - ' + napisan)
                else:
                    for cvor in bridovi:
                        BG.add_node(naslov,bipartite='rad',particija=2,godina=int(napisan))
                        BG.add_node(cvor,bipartite='autor',particija=1)
                        BG.add_edge(cvor,naslov)
                #Konstrukcija multigrafa                      
                if len(bridovi)>1:
                    for cvor1,cvor2 in combinations(bridovi,2):
                        print((cvor1,cvor2))
                        MG.add_edge(cvor1,cvor2,godina=int(napisan),naziv=naslov)
                #Konstrukcija težinskog grafa                      
                if len(bridovi)>1:
                    for cvor1,cvor2 in combinations(bridovi,2):
                        print((cvor1,cvor2))
                        # Provjeravamo postoji li čvor
                        if G.has_edge(cvor1,cvor2):
                            G[cvor1][cvor2]['weight'] += 1
                        else:
                            G.add_edge(cvor1,cvor2,godina=int(napisan),weight=1)
                
            except:
                try:
                    napisan = re.findall('[1][9][8-9][0-9]', s)[0]
                    print(napisan)
                    autori = rad.find('div',class_="authors")
                    #print(autori)        
                    cvorovi = re.sub("\(.*\)","", autori.text.replace(',', '').
                                     replace('š', 's').replace('Š', 'S').
                                     replace('č', 'c').replace('Č', 'C').
                                     replace('ć', 'c').replace('Ć', 'C').
                                     replace('ž', 'z').replace('Ž', 'Z'))
                    #print(cvorovi)
                    bridovi = cvorovi.split(";")
                    bridovi = [cvor.strip() for cvor in bridovi]
                    print(bridovi)
                    provjera(bridovi)
                    #Konstrukcija bipartitnog grafa
                    if naslov in BG:
                        for cvor in bridovi:
                            BG.add_node(naslov + ' - ' + napisan,bipartite='rad',particija=2,godina=int(napisan))
                            BG.add_node(cvor,bipartite='autor',particija=1)
                            BG.add_edge(cvor,naslov + ' - ' + napisan)
                    else:
                        for cvor in bridovi:
                            BG.add_node(naslov,bipartite='rad',particija=2,godina=int(napisan))
                            BG.add_node(cvor,bipartite='autor',particija=1)
                            BG.add_edge(cvor,naslov)
                    #Konstrukcija multigrafa 
                    if len(bridovi)>1:
                        for cvor1,cvor2 in combinations(bridovi,2):
                            print((cvor1,cvor2))
                            MG.add_edge(cvor1,cvor2,godina=int(napisan),naziv=naslov)
                    #Konstrukcija grafa                      
                    if len(bridovi)>1:
                        for cvor1,cvor2 in combinations(bridovi,2):
                            print((cvor1,cvor2))
                            # Provjeravamo postoji li čvor
                            if G.has_edge(cvor1,cvor2):
                                G[cvor1][cvor2]['weight'] += 1
                            else:
                                G.add_edge(cvor1,cvor2,godina=int(napisan),weight=1)
                except: 
                    print('list index out of range')
    
    #print(G.edges(data=True))
    print('\nSuradništvo na Odjelu za informatiku')
    # Iterate over all the nodes in G, including the metadata
    for n, d in MG.nodes(data=True):
        # Calculate the degree of each node: G.node[n]['degree']
        MG.node[n]['degree'] = nx.degree(MG,n)
        
    #print(G.nodes(data=True))
       
    c = plots.CircosPlot(MG,node_labels=True,node_size='degree')
    c.draw()
    plt.show()
    print('Broj čvorova: ' + str(len(MG.nodes())))
    print('Broj suradnji: ' + str(len(MG.edges())) + "\n")
    with open("bipartitni_odjel.graphml", "wb") as ofile:
        nx.write_graphml(BG, ofile)
    with open("odjel.graphml", "wb") as ofile:
        nx.write_graphml(G, ofile)
    return BG

def spremi_podatke_bg(G,LOG=''):
    # Initialize a list to store each edge as a record: nodelist
    nodelist = []
    for n, d in G.nodes(data=True):
        # nodeinfo stores one "record" of data as a dict
        nodeinfo = {'autor/rad': n}         
        # Update the nodeinfo dictionary 
        nodeinfo.update(d)       
        # Append the nodeinfo to the node list
        nodelist.append(nodeinfo)    
    # Create a pandas DataFrame of the nodelist: node_df
    print(nodelist[:10])
    node_df = pd.DataFrame(nodelist)
    print(node_df.head())
    node_df.to_csv('odjeli_bg_cvorovi.csv')
    
    # Initialize a list to store each edge as a record: edgelist
    edgelist = []
    for n1, n2, d in G.edges(data=True):
        if G.node[n1]['bipartite'] == 'autor':
            # Initialize a dictionary that shows edge information: edgeinfo
            edgeinfo = {'autor':n1, 'rad':n2}
        else:
            edgeinfo = {'autor':n2, 'rad':n1}
        # Update the edgeinfo data with the edge metadata
        edgeinfo.update(d)     
        # Append the edgeinfo to the edgelist
        edgelist.append(edgeinfo)        
    # Create a pandas DataFrame of the edgelist: edge_df
    edge_df = pd.DataFrame(edgelist)
    print(edge_df.head())
    edge_df.to_csv('odjeli_bg.csv')
    return edge_df

def crtica(bridovi,LOG=''):
    for n, brid in enumerate(bridovi):
        if '-' in brid:
            lista = brid.split('-')
            lista = [i.strip() for i in lista]
            bridovi[n] = '-'.join(lista)
    return bridovi

def razdvoji(bridovi,LOG=''):
    for n, brid in enumerate(bridovi):
        if ':' in brid:
            bridovi[n] = brid.split(':')[0]
            bridovi.append(brid.split(':')[1])
    return bridovi

def ocisti(bridovi,LOG=''):
    for n, brid in enumerate(bridovi):
        bridovi[n] = brid.title()
        if re.match(r'\s', brid):
            bridovi[n] = brid.strip(' ')
        if '.' in brid:
            bridovi[n] = brid.replace('.','')
            #bridovi[n] = autor.strip('')
    return bridovi

def razmaci(bridovi,LOG=''):
    for n, brid in enumerate(bridovi):
        if len(brid.split(' ')) > 3:
            if len(brid.split(' ')[-1]) > 2:
                bridovi[n] = brid.split(' ')[0] + ' ' + brid.split(' ')[1]
                bridovi.append(brid.split(' ')[-2] + ' ' + brid.split(' ')[-1])
    return bridovi

def postoji_cvor(BG,bridovi,LOG=''):
    for n, brid in enumerate(bridovi):
        obrnuti = brid.split(' ')
        if obrnuti[1] + ' ' + obrnuti[0] in BG.nodes():
            bridovi[n] = obrnuti[1] + ' ' + obrnuti[0]
    return bridovi
    
def prvo_slovo(BG,bridovi,LOG=''):
    for n,brid in enumerate(bridovi):
        #print(brid)
        razdvojen = brid.split(' ')
        #print('^'+razdvojen[0] + ' ' + razdvojen[1][0]+'.*$')
        r = re.compile('^'+razdvojen[0] + ' ' + razdvojen[1][0]+'.*$')
        cvor = list(filter(r.match, BG.nodes())) # Read Note
        if len(cvor) > 0:
            #print(cvor[0])
            bridovi[n] = cvor[0]
    return bridovi

def provjera_gfri(bridovi,LOG=''):
    for n, brid in enumerate(bridovi):
        if brid == 'Zeljko Arbanas':
            bridovi[n] = 'Arbanas Zeljko'
        if brid == 'Arbanas Z Benac C Dugonjic S Kovacevic S M Juric-Kacunic D':
            bridovi[n] = 'Arbanas Zeljko'
            bridovi.append('Benac Cedomir')
            bridovi.append('Dugonjic Jovancevic Sanja')
            bridovi.append('Kovacevic Meho-Sasa')
            bridovi.append('Juric-Kacunic Danijela')
        if brid == 'Dugonjic Sanja':
            bridovi[n] = 'Dugonjic Jovancevic Sanja'
        if brid == 'Josko Ozbolt':
            bridovi[n] = 'Ozbolt Josko'
        if brid == ' Ozbolt Josko':
            bridovi[n] = 'Ozbolt Josko'
        if brid == 'Smolcic Z i Ozbolt J':
            bridovi[n] = 'Ozbolt Josko'
            bridovi.append('Smolcic Zeljko')
        if brid == 'Ozbolt J':
            bridovi[n] = 'Ozbolt Josko'
        if brid == ' Jakominic':
            bridovi[n] = 'Jakominic Marot Natasa'
        if brid == 'Marot Natasa':
            bridovi[n] = 'Jakominic Marot Natasa'
        if brid == ' Li M-X':
            bridovi[n] = 'Li Ming-Xia'
        if brid == 'Zhou Wei-Xing Stanley H Eugene':
            bridovi[n] = 'Stanley Eugene H'
            bridovi.append('Zhou Wei-Xing')
        if brid == 'Wei-Xing Zhou Stanley H Eugene':
            bridovi[n] = 'Stanley Eugene H'
            bridovi.append('Zhou Wei-Xing')
        if brid == ' Stanley H E':
            bridovi[n] = 'Stanley Eugene H'
        if brid == 'Xie W-J: Li M-X':
            bridovi[n] = 'Li Ming-Xia'
            bridovi.append('Xie Wen-Jie')
        if re.search('^Stanley.*$',brid):
            bridovi[n] = 'Stanley Eugene H'
        if brid == 'H Eugene Stanley':
            bridovi[n] = 'Stanley Eugene H'
        if brid == 'Rubinic J':
            bridovi[n] = 'Rubinic Josip'
        if brid == 'Kukuljan Lovel Glavas Ivan Rubinic Josip':
            bridovi[n] = 'Rubinic Josip'
            bridovi.append('Kukuljan Lovel')
            bridovi.append('Glavas Ivan')
        if brid == 'Car-Pusic D':
            bridovi[n] = 'Car-Pusic Diana'
        if brid == 'Candrlic V':
            bridovi[n] = 'Candrlic Vinko'
        if brid == ' Giuffre Tullio':
            bridovi[n] = 'Giuffre Tullio'
        if brid == 'Vahida Zujo Diana Car-Pusic Valentina Zileska-Pancovska':
            bridovi[n] = 'Car-Pusic Diana'
            bridovi.append('Zujo Vahida')
            bridovi.append('Zileska-Pancovska Valentina')
        if brid == 'Li M-X':
            bridovi[n] = 'Li Ming-Xia'
        if brid == 'Podobnik Boris Balen Vanco':
            bridovi[n] = 'Podobnik Boris'
            bridovi.append('Balen Vanco')
        if brid == 'Boris Podobnik Boris':
            bridovi[n] = 'Podobnik Boris'
        if brid == 'Balen Vanco Kolanovic Marko':
            bridovi[n] = 'Balen Vanco'
            bridovi.append('Kolanovic Marko')
        if brid == 'Karleusa Barbara Crnko Tamara':
            bridovi[n] = 'Karleusa Barbara'
            bridovi.append('Crnko Tamara')
        if brid == 'Kozar I':
            bridovi[n] = 'Kozar Ivica'
        if brid == 'Ivica Kozar':
            bridovi[n] = 'Kozar Ivica'
        if brid == 'Zwicker':
            bridovi[n] = 'Zwicker Gordana'
        if brid == 'Zhou W-X':
            bridovi[n] = 'Zhou Wei-Xing'
        if brid == 'Zhou Wei-X':
            bridovi[n] = 'Zhou Wei-Xing'
        if brid == '':
            del bridovi[n]
    return bridovi
    
def ekstrakcija_gfri(LOG=''):
    G = nx.Graph()
    BG = nx.Graph()
    MG = nx.MultiGraph()
    for i in range(1,int(zadnja_gfri)+1):
        url = "https://www.bib.irb.hr/pretraga?operators=and%7CGra%C4%91evinski%20fakultet%2C%20Rijeka%20%28114%29%7Ctext%7Cinstitution&group=journal_articles%7Cconference_proceedings&subgroup=ja-original_scientific_papers%7Ccpr-scientific_proceedings&order_by=year_asc&page="+str(i)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        radovi = soup.find('ul', class_="list-unstyled")
        #print(radovi)
        radovi1 = radovi.find_all('li')
        #print(radovi1)
        
        for rad in radovi1:
            naslov = rad.a.text
            print(naslov)
            godina = rad.find('span',class_="citation")
            s = godina.text
            try:                
                napisan = re.findall('[2][0][0-2][0-9]', s)[0]
                print(napisan)
                autori = rad.find('div',class_="authors")
                #print(autori)        
                cvorovi = re.sub("\(.*\)","", autori.text.replace(',', '').
                                 replace('š', 's').replace('Š', 'S').
                                 replace('č', 'c').replace('Č', 'C').
                                 replace('ć', 'c').replace('Ć', 'C').
                                 replace('ž', 'z').replace('Ž', 'Z'))
                #print(cvorovi)                   
                bridovi = cvorovi.split(";")
                bridovi = [cvor.strip() for cvor in bridovi]
                print(bridovi)
                ocisti(bridovi)
                razdvoji(bridovi)
                crtica(bridovi)
                prvo_slovo(BG,bridovi)
                postoji_cvor(BG,bridovi)
                razmaci(bridovi)
                provjera_gfri(bridovi)
                #Konstrukcija bipartitnog grafa
                if naslov in BG:
                    for cvor in bridovi:
                        BG.add_node(naslov + ' - ' + napisan,bipartite='rad',particija=2,godina=int(napisan))
                        BG.add_node(cvor,bipartite='autor',particija=1)
                        BG.add_edge(cvor,naslov + ' - ' + napisan)
                else:
                    for cvor in bridovi:
                        BG.add_node(naslov,bipartite='rad',particija=2,godina=int(napisan))
                        BG.add_node(cvor,bipartite='autor',particija=1)
                        BG.add_edge(cvor,naslov)
                #Konstrukcija multigrafa                      
                if len(bridovi)>1:
                    for cvor1,cvor2 in combinations(bridovi,2):
                        #print((cvor1,cvor2))
                        MG.add_edge(cvor1,cvor2,godina=int(napisan),naziv=naslov)
                #Konstrukcija grafa                      
                if len(bridovi)>1:
                    for cvor1,cvor2 in combinations(bridovi,2):
                        print((cvor1,cvor2))
                        # Provjeravamo postoji li čvor
                        if G.has_edge(cvor1,cvor2):
                            G[cvor1][cvor2]['weight'] += 1
                        else:
                            G.add_edge(cvor1,cvor2,godina=int(napisan),weight=1)
                
            except:
                try:
                    napisan = re.findall('[1][9][8-9][0-9]', s)[0]
                    print(napisan)
                    autori = rad.find('div',class_="authors")
                    #print(autori)        
                    cvorovi = re.sub("\(.*\)","", autori.text.replace(',', '').
                                     replace('š', 's').replace('Š', 'S').
                                     replace('č', 'c').replace('Č', 'C').
                                     replace('ć', 'c').replace('Ć', 'C').
                                     replace('ž', 'z').replace('Ž', 'Z'))
                    #print(cvorovi)
                    bridovi = cvorovi.split(";")
                    bridovi = [cvor.strip() for cvor in bridovi]
                    print(bridovi)
                    ocisti(bridovi)
                    razdvoji(bridovi)
                    crtica(bridovi)
                    prvo_slovo(BG,bridovi)
                    postoji_cvor(BG,bridovi)
                    razmaci(bridovi)
                    provjera_gfri(bridovi)
                    #Konstrukcija bipartitnog grafa
                    if naslov in BG:
                        for cvor in bridovi:
                            BG.add_node(naslov + ' - ' + napisan,bipartite='rad',particija=2,godina=int(napisan))
                            BG.add_node(cvor,bipartite='autor',particija=1)
                            BG.add_edge(cvor,naslov + ' - ' + napisan)
                    else:
                        for cvor in bridovi:
                            BG.add_node(naslov,bipartite='rad',particija=2,godina=int(napisan))
                            BG.add_node(cvor,bipartite='autor',particija=1)
                            BG.add_edge(cvor,naslov)
                    #Konstrukcija multigrafa 
                    if len(bridovi)>1:
                        for cvor1,cvor2 in combinations(bridovi,2):
                            #print((cvor1,cvor2))
                            MG.add_edge(cvor1,cvor2,godina=int(napisan),naziv=naslov)
                    #Konstrukcija grafa                      
                    if len(bridovi)>1:
                        for cvor1,cvor2 in combinations(bridovi,2):
                            print((cvor1,cvor2))
                            # Provjeravamo postoji li čvor
                            if G.has_edge(cvor1,cvor2):
                                G[cvor1][cvor2]['weight'] += 1
                            else:
                                G.add_edge(cvor1,cvor2,godina=int(napisan),weight=1)
                except: 
                    print('list index out of range')
    
    #print(G.edges(data=True))
    print('\nSuradništvo na Građevinskom fakultetu')
    # Iterate over all the nodes in G, including the metadata
    for n, d in MG.nodes(data=True):
        # Calculate the degree of each node: G.node[n]['degree']
        MG.node[n]['degree'] = nx.degree(G,n)
        
    #print(G.nodes(data=True))
       
    c = plots.CircosPlot(MG,node_labels=True,node_size='degree')
    c.draw()
    plt.show()
    print('Broj čvorova: ' + str(len(MG.nodes())))
    print('Broj suradnji: ' + str(len(MG.edges())) + "\n")
    with open("bipartitni_gfri.graphml", "wb") as ofile:
        nx.write_graphml(BG, ofile)
    with open("gfri.graphml", "wb") as ofile:
        nx.write_graphml(G, ofile)
    return MG

def spremi_mg(G,LOG=''):
    # Initialize a list to store each edge as a record: nodelist
    nodelist = []
    for n, d in G.nodes(data=True):
        # nodeinfo stores one "record" of data as a dict
        nodeinfo = {'autor': n}         
        # Update the nodeinfo dictionary 
        nodeinfo.update(d)       
        # Append the nodeinfo to the node list
        nodelist.append(nodeinfo)    
    # Create a pandas DataFrame of the nodelist: node_df
    print(nodelist)
    node_df = pd.DataFrame(nodelist)
    print(node_df.head())
    
    # Inicijalizacija liste za pohranu svake veze: edgelist
    edgelist = []
    for n1, n2, d in G.edges(data=True):
        # Inicijalizacija riječnika koji prikazuje informacije o vezi:edgeinfo
        edgeinfo = {'autor1':n1, 'autor2':n2}        
        # Ažuriranje podatka o vezi s ostalim atributima
        edgeinfo.update(d)        
        # Proširujemo listu bridova novim bridom
        edgelist.append(edgeinfo)        
    # Kreiramo DataFrame liste bridova pomoću pandas biblioteke: edge_df
    edge_df = pd.DataFrame(edgelist)
    print(edge_df.head())
    edge_df.to_csv('gfri_mg.csv')
    return edge_df,node_df 
                

    #MAIN
if __name__=='__main__':
    print('main...')    
    import time
    tic=time.time()
    #odjel_zadnja(LOG)
    gfri_zadnja(LOG)
    #G = ekstrakcija_odjel(LOG)
    G2 = ekstrakcija_gfri(LOG)
    #podaci = spremi_podatke_bg(G,LOG)
    podaci2 = spremi_mg(G2,LOG)
    toc=time.time()
    doubleprint('\n\nExecution time: {} seconds'.format(toc-tic),LOG)