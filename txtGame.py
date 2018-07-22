# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 14:14:45 2018

@author: A.P
"""
import os ; import csv ; import pandas as pd
runfile(u'C:\\Users\\A.P\\Desktop\\Arthur\\Manip_Run\\cobeye\\basic_EL.py')

dir1 = "C:\\Users\\A.P\\Desktop\\Arthur\\Manip_Run\\cobeye\\SecureData\\TXT_RTF\\" 
itemfile = []
os.chdir(dir1)
for root,dirs,files in os.walk(dir1):
            for file in sorted(files):
                if file.endswith(".rtf"):
                    print(os.path.join(root,file))
                    itemfile.append(file)
                    itemfile.sort(key=natural_keys)
                        
        cstGame = {}
        for i in range (0,len(itemfile)):    
            with open(itemfile[i],"rt") as csvfile:
        #            csvReader = csv.reader(codecs.open("Sujet%s\A_S%s_%s_%s.aju" %(n,m,s,b), 'rU', 'utf-16'))
                    data= csv.reader(csvfile,delimiter=',') ##pour symboliser des colonnes delimiter = ";"
                    l = list()
                    for row in data:
                        #print type(row)
                        #print row ## affiche la colonne 2
                        l.append(row) ## recupère la colonne où sont affichés les numéros d'essais
                    cstGame["%s"%(itemfile[i])]=l
                    
        
            aj = list();cstAll={}              
            for i in range (0,len(cstGame)):    
                for j in range (0,len(cstGame["%s"%(itemfile[i])])):
                    aj.append(cstGame["%s"%(itemfile[i])][j][0].split())
                cstAll["%s"%(itemfile[i])] = aj
                aj = list()

Constante = pd.DataFrame(cstAll["Anti1TXT.rtf"][1:])
Constante.columns = Constante.iloc[0]
