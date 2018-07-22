# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:56:37 2017

@author: A.P
"""
from __future__ import division, print_function
#runfile(u'C:\\Users\\A.P\\Desktop\\Arthur\\Manip_Run\\cobeye\\basic_EL.py')
#runfile(u'C:\\Users\\A.P\\Desktop\\Arthur\\Manip_Run\\cobeye\\constantes.py')
runfile(u'C:\\Users\\Léo\\Desktop\\cobeye\\basic_EL.py')
runfile(u'C:\\Users\\Léo\\Desktop\\cobeye\\constantes.py')
%matplotlib auto

## Organisation des données : 
## Step 1 --> chaque nom de répertoire raw des données nommé "date_namesujet_repetition" doit être renommé Sx (x = numéro du sujet)
## Step 2 --> chaque repertoire Sx doit être placé dans un répertoire générale Ly (y = numéro du/ de votre laboratoire dans la nomenclature décidée - voir ci dessous)

#0 : Institut de la Vision (Jean)
#1 : ICM (Pierre)
#2 : GIBSA (Nathalie)
#3 : IMPACT (Denis)
#4 : Inférence et Comportements Visuels (Anna)
#5 : Perception et Sensori-Motricité (Carole) 
#6 : Perception et Attention (Francoise)
#7 : Vision Action Cognition (Céline)
#8 : Psychologie de la Perception (Thérèse)
#9 : SCALab (Laurent)
#10 : Neuroergonomie et Facteurs Humains (Seva)

## Path absolu dans lequel on peut récupérer les données : 
  
#datpath = "C:\\Users\\Léo\\Desktop\\cobeye\\SecureData\\Eyelink\\"  
GAME =dict() ; DGAME =dict() ; VGAME =dict() ; AGAME =dict() ; MINFOS = dict()
#m = 0 ; n=[5,6,7,8,9] #; k=0  

# =============================================================================
# EYELINK
# =============================================================================
datpath = "C:\\Users\\A.P\\Desktop\\Arthur\\Manip_Run\\cobeye\\SecureData\\Eyelink\\"  
for p in range (0,len(m)):
        if m[p] == 0:
                n = n0
#                c = 1
        elif m[p] == 1:
                n = n1
#                c = 2
        elif m[p] == 3:
                n = n3
        elif m[p] == 5:
                n = n5
        elif m[p] == 7:
                n = n7
        for k in range(0,len(n)):
                names = []  ; nam = [] ; ilab = []
                
                clabo = ["Institut de la Vision","ICM","GIBSA","IMPACT","Inférence et Comportements Visuels","Perception et Sensori-Motricité","Perception et Attention","Vision Action Cognition","Psychologie de la Perception","SCAlab","Neuroergonomie"]
                llabo = ["Paris_75012","Paris_75013","Grenoble_38185","Lyon_69123","Marseille_13055","Grenoble_38185", "Marseille_13055", "Boulogne Billancourt_92012", "Paris_75006", "Lille_59350", "Toulouse_31555"]
                rlabo = ["Jean Lorenceau", "Pierre Pouget", "Nathalie Guyader", "Denis Pelisson", "Anna Montagnini", "Carole Peyrin", "Françoise Vitu", "Céline Paeye", "Thérèse Collins", "Laurent Madelain", "Vsevolod Peysakhovich"]

                ilab = [clabo[m[p]],llabo[m[p]],rlabo[m[p]]] 
                
                
                
                checkasc(m[p],n[k]);sub_cut(m[p],n[k]) ; get_etdata(m[p],n[k]) ; convpxltodeg(dis,c,win,order,deriv); degtovel(sr) ; veltoacc(sr) ; gnames()
                rectime(sr)
                print (time.clock()) ## check le temps
                # Stockage des données en PXLS
                G,DG,VG,AG = {},{},{},{}
                for i in range (0,len(names)):
                        G["%s"%(nam[i])] =  {'X1': MM1[ajfile[i]][0], 'Y1': MM1[ajfile[i]][1], 'PUP1': MM1[ajfile[i]][2],'X2': MM2[ajfile[i]][0], 'Y2': MM2[ajfile[i]][1], 'PUP2': MM2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK1[ajfile[i]]}
                ## Stockage des données en DEGREE
        #        for i in range (0,len(names)):
                        DG["%s"%(nam[i])] = {'X1': MDEG1[ajfile[i]][0], 'Y1': MDEG1[ajfile[i]][1], 'PUP1': MDEG1[ajfile[i]][2],'X2': MDEG2[ajfile[i]][0], 'Y2': MDEG2[ajfile[i]][1], 'PUP2': MDEG2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK1[ajfile[i]]}
                ## Stockage des données en VITESSE (°/s)
        #        for i in range (0,len(names)):
                        VG["%s"%(nam[i])] =  {'X1': MVEL1[ajfile[i]][0], 'Y1': MVEL1[ajfile[i]][1], 'PUP1': MVEL1[ajfile[i]][2],'X2': MVEL2[ajfile[i]][0], 'Y2': MVEL2[ajfile[i]][1], 'PUP2': MVEL2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK2[ajfile[i]]}
                ## Stockage des données en ACCELERATION
        #        for i in range (0,len(names)):
                        AG["%s"%(nam[i])] = {'X1': MACC1[ajfile[i]][0],'Y1': MACC1[ajfile[i]][1],'PUP1': MACC1[ajfile[i]][2],'X2': MACC2[ajfile[i]][0], 'Y2': MACC2[ajfile[i]][1], 'PUP2': MACC2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK2[ajfile[i]]}
        #        ## Stockage information sujet
                        INFOS = {"NAME_ORIGINAL" : ajfile, "NAME_MODIF" : nam, "DATE" : date, "SAMPLE" : sampler,"DURATION" : duration_sec, "INFLAB" : ilab}
                s1000 += 1
                GAME["S%s"%(s1000)] = G ; 
                DGAME["S%s"%(s1000)] = DG
                VGAME["S%s"%(s1000)] = VG
                AGAME["S%s"%(s1000)] = AG
                MINFOS["S%s"%(s1000)] = INFOS
                
        # =============================================================================
        # #SAVE THE DICTIONNARY
# =============================================================================
pickle.dump(GAME,open(datpath +"GAME_.p","wb"))        
pickle.dump(DGAME,open(datpath +"DGAME_.p","wb"))
pickle.dump(VGAME,open(datpath +"VGAME_.p","wb"))
pickle.dump(AGAME,open(datpath +"AGAME_.p","wb"))
pickle.dump(MINFOS,open(datpath +"MINFOS_.p","wb"))
#


## =============================================================================
## LIVETRACK
## =============================================================================
#datpath = "C:\\Users\\A.P\\Desktop\\Arthur\\Manip_Run\\cobeye\\SecureData\\LiveTrack\\" 
#m = [0] ; 
#for p in range (0,len(m)):
#        if m[p] == 0:
#                n = [1,2,3,4,5,6,7]
#
#        for k in range(0,len(n)):
#                names = []  ; nam = [] ; ilab = []
#                
#                clabo = ["Institut de la Vision","ICM","GIBSA","IMPACT","Inférence et Comportements Visuels","Perception et Sensori-Motricité","Perception et Attention","Vision Action Cognition","Psychologie de la Perception","SCAlab","Neuroergonomie"]
#                llabo = ["Paris_75012","Paris_75013","Grenoble_38185","Lyon_69123","Marseille_13055","Grenoble_38185", "Marseille_13055", "Boulogne Billancourt_92012", "Paris_75006", "Lille_59350", "Toulouse_31555"]
#                rlabo = ["Jean Lorenceau", "Pierre Pouget", "Nathalie Guyader", "Denis Pelisson", "Anna Montagnini", "Carole Peyrin", "Françoise Vitu", "Céline Paeye", "Thérèse Collins", "Laurent Madelain", "Vsevolod Peysakhovich"]
#
#                ilab = [clabo[m[p]],llabo[m[p]],rlabo[m[p]]] 
#                
#                
#                
#                sub_cut_LT(m[p],n[k],16) ; get_etdata(m[p],n[k]) ; convpxltodeg(dis,c,win,order,deriv); degtovel(sr) ; veltoacc(sr) ; gnames()
#                rectime(sr)
#                print (time.clock()) ## check le temps
#                # Stockage des données en PXLS
#                G,DG,VG,AG = {},{},{},{}
#                for i in range (0,len(names)):
#                        G["%s"%(nam[i])] =  {'X1': MM1[ajfile[i]][0], 'Y1': MM1[ajfile[i]][1], 'PUP1': MM1[ajfile[i]][2],'X2': MM2[ajfile[i]][0], 'Y2': MM2[ajfile[i]][1], 'PUP2': MM2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK1[ajfile[i]]}
#                ## Stockage des données en DEGREE
#        #        for i in range (0,len(names)):
#                        DG["%s"%(nam[i])] = {'X1': MDEG1[ajfile[i]][0], 'Y1': MDEG1[ajfile[i]][1], 'PUP1': MDEG1[ajfile[i]][2],'X2': MDEG2[ajfile[i]][0], 'Y2': MDEG2[ajfile[i]][1], 'PUP2': MDEG2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK1[ajfile[i]]}
#                ## Stockage des données en VITESSE (°/s)
#        #        for i in range (0,len(names)):
#                        VG["%s"%(nam[i])] =  {'X1': MVEL1[ajfile[i]][0], 'Y1': MVEL1[ajfile[i]][1], 'PUP1': MVEL1[ajfile[i]][2],'X2': MVEL2[ajfile[i]][0], 'Y2': MVEL2[ajfile[i]][1], 'PUP2': MVEL2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK2[ajfile[i]]}
#                ## Stockage des données en ACCELERATION
#        #        for i in range (0,len(names)):
#                        AG["%s"%(nam[i])] = {'X1': MACC1[ajfile[i]][0],'Y1': MACC1[ajfile[i]][1],'PUP1': MACC1[ajfile[i]][2],'X2': MACC2[ajfile[i]][0], 'Y2': MACC2[ajfile[i]][1], 'PUP2': MACC2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK2[ajfile[i]]}
#        #        ## Stockage information sujet
#                        INFOS = {"NAME_ORIGINAL" : ajfile, "NAME_MODIF" : nam, "SAMPLE" : 500,"DURATION" : duration_sec, "INFLAB" : ilab}
#                s1000 += 1
#                GAME["S%s"%(s1000)] = G ; 
#                DGAME["S%s"%(s1000)] = DG
#                VGAME["S%s"%(s1000)] = VG
#                AGAME["S%s"%(s1000)] = AG
#                MINFOS["S%s"%(s1000)] = INFOS
#                
#        # =============================================================================
#        # #SAVE THE DICTIONNARY
## =============================================================================
#pickle.dump(GAME,open(datpath +"GAME_.p","wb"))        
#pickle.dump(DGAME,open(datpath +"DGAME_.p","wb"))
#pickle.dump(VGAME,open(datpath +"VGAME_.p","wb"))
#pickle.dump(AGAME,open(datpath +"AGAME_.p","wb"))
#pickle.dump(MINFOS,open(datpath +"MINFOS_.p","wb"))


