# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:56:37 2017

@author: A.P
"""

from __future__ import division, print_function
import os; import sys 
import csv;from os import chdir;from pylab import *;from os import chdir;import pylab as p;from math import sqrt;from matplotlib.pyplot import *;import pandas as pd
from scipy.signal import butter, filtfilt;import sys;import scipy, pylab;from scipy import signal;from scipy.interpolate import interp1d
import numpy as np;from scipy import stats;from scipy.interpolate import UnivariateSpline;import copy; import time
from scipy.signal import medfilt

%matplotlib auto


## fonction qui permet de recupérer à la fois le fichier aju et le fichier LiveTrack
#def exctajlt(n):
    n = 3 ; ajfile= list() ; allaj = {}
#    filemenus =["intro","Sacc1","Sacc2","Sacc3","choice1","]
    os.chdir("C:\\Users\\A.P\\Desktop\\Arthur\\Manip_Run\\cobeye\\SecureData\\Sujet%s\\"%(n))
    dir1 = os.path.dirname("C:\\Users\\A.P\\Desktop\\Arthur\\Manip_Run\\cobeye\\SecureData\\Sujet%s\\"%(n))
    for root,dirs,files in os.walk(dir1):
        for file in files:
            if file.endswith(".eos"):
                print(os.path.join(root,file))
                ajfile.append(os.path.join(root,file))
            if file.endswith(".ltd"):
                print(os.path.join(root,file))
                ltfile = os.path.join(root,file)  
        global tab1,o1,row,data,l,aj,index
        import codecs
    ###################
    #
    ###################
    for i in range (0,len(ajfile)):
        
        with open(ajfile[i],"rt") as csvfile:
    #            csvReader = csv.reader(codecs.open("Sujet%s\A_S%s_%s_%s.aju" %(n,m,s,b), 'rU', 'utf-16'))
                data= csv.reader(csvfile,delimiter=',') ##pour symboliser des colonnes delimiter = ";"
                l = list()
                for row in data:
                    #print type(row)
                    #print row ## affiche la colonne 2
                    l.append(row) ## recupère la colonne où sont affichés les numéros d'essais
    
    
        aj = list()                
        for i in range (0,len(l)):
                aj.append(l[i][0].split())
        #j.remove(aj[0])
        #aj.remove(aj[1])
        print (len(aj))
        
## GET DATA LTD
with open(ltfile,"rt") as ltf:
    data= csv.reader(ltf,delimiter=' ') ##pour symboliser des colonnes delimiter = ";"
    tabo3=list(data)       

taboo = tabo3[2:]
    
for i in range (2,len(taboo)):
    while '' in taboo[i]:
        taboo[i].remove('')
    
    O3 = list()
    for i in range(0,len(taboo)-2): ## recupere les colonnes de data
        O3.append(taboo[i])
    
O1 = list() ; O2 = list()
for i in range (0,len(O3)): ## Reduire aux coordonnées x,y et pupille (colonnes 1,2,3 respectivement)
    O1.append(O3[i][3:6])
    O2.append(O3[i][10:13])
    
#    ## on recupere les index des lignes contenant
#    ind = list()
#    for i in range (0,len(O)):
#        if O[i][1]=='   .':
#            ind.append([i,int(O[i][0])])
#    
#    ## on remplace les points par des '0.0'
#    for i in range (0,len(ind)):
#        O[ind[i][0]] = [ind[i][1],np.NaN,np.NaN,np.NaN]
    
    
    ## convertir en float, si point ds les listes, d'abord remplacer les points par des 0.0:
    
EX1 = list() ## coordonnée en x
EY1= list() ## coordonnée en y
PUP1 = list() ## pupille
EX2 = list()
EY2 = list()
PUP2 = list()
timeline = list()
recap=list()

## get oeil 1    
for i in range(0,len(O1)):
    EX1.append(float(O1[i][0]))
    EY1.append(float(O1[i][1]))
    PUP1.append(float(O1[i][2]))

EX1 = np.array(EX1)
EY1 = np.array(EY1)
PUP1 = np.array(PUP1)



for i in range(0,len(O2)):
    EX2.append(float(O2[i][0]))
    EY2.append(float(O2[i][1]))
    PUP2.append(float(O2[i][2]))

EX2 = np.array(EX2)
EY2 = np.array(EY2)
PUP2 = np.array(PUP2)
   
#    for i in range(0,len(O)):
#        timeline.append(int(O[i][0]))
    
#verif=[len(eyeX),len(eyeY),len(pup),len(timeline)]
#print (verif)
    

EX1 = np.transpose(EX1)
EY1 = np.transpose(EY1)
PUP1 = np.transpose(PUP1)
EX2 = np.transpose(EX2)
EXY2 = np.transpose(EY2)
PUP2 = np.transpose(PUP2)

