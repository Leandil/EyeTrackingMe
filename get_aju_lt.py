# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:56:37 2017

@author: A.P
"""

##################################
##################################
from __future__ import division, print_function
runfile(u'C:\\Users\\A.P\\Desktop\\Arthur\\Manip_Run\\cobeye\\basic_LT.py')
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
datpath = "C:\\Users\\A.P\\Desktop\\Arthur\\Manip_Run\\cobeye\\SecureData\\LiveTrack\\"    
GAME =dict() ; DGAME =dict() ; VGAME =dict() ; AGAME =dict() ; MINFOS = dict()
m = 0 ; n = [9] ; col = 16
for k in range(0,len(n)):
        names = []
        sub_cut(m,n[k],col) ; get_etdata(n[k]) ; convpxltodeg(78,1,29,0,0) ; degtovel(500) ; veltoacc(500) ; gnames()
        rectime(500)
        
        ## Stockage des données en PXLS
        #for i in range (0,len(ajfile)):
        #        GAME["%s"%(ajfile[i])] = {'L%s_S%s'%(m,n): {'X1': MM1[ajfile[i]][0], 'Y1': MM1[ajfile[i]][1], 'PUP1': MM1[ajfile[i]][2],'X2': MM2[ajfile[i]][0], 'Y2': MM2[ajfile[i]][1], 'PUP2': MM2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK1[ajfile[i]]}}        
        ### Stockage des données en DEGREE
        #for i in range (0,len(ajfile)):
        #        DGAME["%s"%(ajfile[i])] = {'L%s_S%s'%(m,n): {'X1': MDEG1[ajfile[i]][0], 'Y1': MDEG1[ajfile[i]][1], 'PUP1': MDEG1[ajfile[i]][2],'X2': MDEG2[ajfile[i]][0], 'Y2': MDEG2[ajfile[i]][1], 'PUP2': MDEG2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK1[ajfile[i]]}}
        ### Stockage des données en VITESSE (°/s)
        #for i in range (0,len(ajfile)):
        #        VGAME["%s"%(ajfile[i])] = {'L%s_S%s'%(m,n): {'X1': MVEL1[ajfile[i]][0], 'Y1': MVEL1[ajfile[i]][1], 'PUP1': MVEL1[ajfile[i]][2],'X2': MVEL2[ajfile[i]][0], 'Y2': MVEL2[ajfile[i]][1], 'PUP2': MVEL2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK2[ajfile[i]]}}
        ### Stockage des données en ACCELERATION
        #for i in range (0,len(ajfile)):
        #        AGAME["%s"%(ajfile[i])] = {'L%s_S%s'%(m,n): {'X1': MACC1[ajfile[i]][0],'Y1': MACC1[ajfile[i]][1],'PUP1': MACC1[ajfile[i]][2],'X2': MACC2[ajfile[i]][0], 'Y2': MACC2[ajfile[i]][1], 'PUP2': MACC2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK2[ajfile[i]]}}
        #
        
        # Stockage des données en PXLS
        G,DG,VG,AG = {},{},{},{}
        for i in range (0,len(names)):
                G["%s"%(names[i])] =  {'X1': MM1[ajfile[i]][0], 'Y1': MM1[ajfile[i]][1], 'PUP1': MM1[ajfile[i]][2],'X2': MM2[ajfile[i]][0], 'Y2': MM2[ajfile[i]][1], 'PUP2': MM2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK1[ajfile[i]]}
        ## Stockage des données en DEGREE
        for i in range (0,len(names)):
                DG["%s"%(names[i])] = {'X1': MDEG1[ajfile[i]][0], 'Y1': MDEG1[ajfile[i]][1], 'PUP1': MDEG1[ajfile[i]][2],'X2': MDEG2[ajfile[i]][0], 'Y2': MDEG2[ajfile[i]][1], 'PUP2': MDEG2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK1[ajfile[i]]}
        ## Stockage des données en VITESSE (°/s)
        for i in range (0,len(names)):
                VG["%s"%(names[i])] =  {'X1': MVEL1[ajfile[i]][0], 'Y1': MVEL1[ajfile[i]][1], 'PUP1': MVEL1[ajfile[i]][2],'X2': MVEL2[ajfile[i]][0], 'Y2': MVEL2[ajfile[i]][1], 'PUP2': MVEL2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK2[ajfile[i]]}
        ## Stockage des données en ACCELERATION
        for i in range (0,len(names)):
                AG["%s"%(names[i])] = {'X1': MACC1[ajfile[i]][0],'Y1': MACC1[ajfile[i]][1],'PUP1': MACC1[ajfile[i]][2],'X2': MACC2[ajfile[i]][0], 'Y2': MACC2[ajfile[i]][1], 'PUP2': MACC2[ajfile[i]][2],'FR': MM1[ajfile[i]][3],'TS':CHUNK2[ajfile[i]]}
##        ## Stockage information sujet
#                INFOS = {"NAME_ORIGINAL" : ajfile, "NAME_MODIF" : names, "DATE" : date, "SAMPLE" : sampler,"DURATION" : duration_sec, "INFLAB" : ilab}
##        
        GAME["L%s_S%s"%(m,n[k])] = G ; 
        DGAME["L%s_S%s"%(m,n[k])] = DG
        VGAME["L%s_S%s"%(m,n[k])] = VG
        AGAME["L%s_S%s"%(m,n[k])] = AG
#        MINFOS["L%s_S%s"%(m,n[k])] = INFOS



# =============================================================================
# Poblème signal data pup: ecart de 0.03125
# =============================================================================

#GAME = {'L%s_S%s'%(m,n): {'X1': MM1[ajfile[i]][0], 'Y1': MM1[ajfile[i]][1], 'PUP1': MM1[ajfile[i]][2],'X2': MM2[ajfile[i]][0], 'Y2': MM2[ajfile[i]][1], 'PUP2': MM2[ajfile[i]][2],'TS': MM1[ajfile[i]][3]}}

        
        
## Exemple : 
#                g1 = game(6)
#                g1.name
                
                
## First Variables

##############################
#LIVETRACK
#############################
# fonction qui permet de recupérer à la fois le fichier aju et le fichier LiveTrack
#def exctajlt(n):
#def sub_cut(m,n):
#        """ This function allows us to get all the namefiles ending with the extension .eos and .asc.
#        In order to get the time onset and the offset timestamps in each eos files and use it to slice the ascii files. These timestamps are stored in 
#        "index" dictionnary : column 3 : beginning of the game // column 4 : end of the game """
#        global ajfile,allaj, eosall,ajall,index,ltfile
##        m = 7 ; n = 2 ;
#        ajfile= list() ; allaj = {}
#        os.chdir(datpath + "L%s\\S%s_LT\\"%(m,n))
#        dir1 = os.path.dirname(datpath + "L%s\\S%s_LT\\"%(m,n))
#        for root,dirs,files in os.walk(dir1):
#            for file in files:
#                if file.endswith(".eos"):
#                    print(os.path.join(root,file))
#                    ajfile.append(file)
#                    ajfile.sort(key=natural_keys)
#        #        if file.endswith(".ltd"):
#                if file.endswith(".ltd"):
#                    print(os.path.join(root,file))
#                    ltfile = os.path.join(root,file)  
#            global tab1,o1,row,data,l,aj,index
#            import codecs
#
#
####################
#        eosall = {}
#        for i in range (0,len(ajfile)):    
#            with open(ajfile[i],"rt") as csvfile:
#        #            csvReader = csv.reader(codecs.open("Sujet%s\A_S%s_%s_%s.aju" %(n,m,s,b), 'rU', 'utf-16'))
#                    data= csv.reader(csvfile,delimiter=',') ##pour symboliser des colonnes delimiter = ";"
#                    l = list()
#                    for row in data:
#                        #print type(row)
#                        #print row ## affiche la colonne 2
#                        l.append(row) ## recupère la colonne où sont affichés les numéros d'essais
#                    eosall["%s"%(ajfile[i])]=l
#                    
#        
#            aj = list();ajall={}              
#            for i in range (0,len(eosall)):    
#                for j in range (0,len(eosall["%s"%(ajfile[i])])):
#                    aj.append(eosall["%s"%(ajfile[i])][j][0].split())
#                ajall["%s"%(ajfile[i])] = aj
#                aj = list()
#                    
##            
#            index = {}
#            for i in range (0,len(ajall)):
#                for j in range(0,len(ajall[ajfile[i]])-1):
#                    if len(ajall[ajfile[i]][j]) == 5:    
#                        index[ajfile[i]]= [ajall[ajfile[i]][j][1],ajall[ajfile[i]][j+1][1],int(ajall[ajfile[i]][j+1][2]),int(ajall[ajfile[i]][j+3][16]),int(ajall[ajfile[i]][-2][16])]
#    
###        
##            index = {}
##            for i in range (0,len(ajall)):
##                for j in range(0,len(ajall[ajfile[i]])-1):
##                    if len(ajall[ajfile[i]][j]) == 5:    
##                        index[ajfile[i]]= [ajall[ajfile[i]][j][1],ajall[ajfile[i]][j+1][1],int(ajall[ajfile[i]][j+1][2]),int(ajall[ajfile[i]][j+3][15]),int(ajall[ajfile[i]][-2][15])]
##    
#    
####################
## =============================================================================
## #GET DATA FICHIER EOS // TIMESTAMP MENU FIN
## =============================================================================
####################
## =============================================================================
## ## GET DATA LIVETRACK
## =============================================================================
#def get_etdata(n):
#        """ From the timestamps get in the first function, this function allos us to get the eye positions in x and y, then pupil dynamic for each eye in binocular or one eye in monocular recording"""
#        global taboo,O3,O1,O2,tmt,indo1,indo2,EX1,EY1,PUP1,EX2,EY2,PUP2,TMT,MM1,MM2, namenu, nmenu, menus_ind
#               
#        ## information fichier EOS / get timestamp début / fin // Slice in ASCII file 
#        menus_ind = {}
#        for i in range (0,len(ajfile)):
#            menus_ind[ajfile[i]] = [index[ajfile[i]][3],index[ajfile[i]][4]]## index de la timeline ASCII de début et de fin pour chaque menu 
#                                           
#        with open(ltfile,"rt") as ltf:
#            data= csv.reader(ltf,delimiter=' ') ##pour symboliser des colonnes delimiter = ";"
#            tabo3=list(data)       
#        
#        taboo = tabo3[2:]
#        for i in range (2,len(taboo)):
#            while '' in taboo[i]:
#                taboo[i].remove('')
#            
#        O3 = list()
#        for i in range(0,len(taboo)-2): ## recupere les colonnes de data
#            O3.append(taboo[i])
#            
#        O1 = list() ; O2 = list() ; tmt = list()
#        for i in range (0,len(O3)): ## Reduire aux coordonnées x,y et pupille (colonnes 1,2,3 respectivement)
#            O1.append(O3[i][3:6])
#            O2.append(O3[i][10:13])
#            tmt.append(O3[i][0][:-1])
#            
#        ## List to get information from OEIL1 et OEIL2
#        EX1 = list() ## coordonnée en x
#        EY1= list() ## coordonnée en y
#        PUP1 = list() ## pupille
#        EX2 = list()
#        EY2 = list()
#        PUP2 = list()
#        timeline = list()
#        recap=list()
#        
#        ## get OEIL 1    
#        for i in range(2,len(O1)):   
#            EX1.append(float(O1[i][0]))
#            EY1.append(float(O1[i][1]))
#            PUP1.append(float(O1[i][2]))
#        
#        ## transform in array
#        EX1 = np.array(EX1)
#        EY1 = np.array(EY1)
#        PUP1 = np.array(PUP1)
#        
#        
#        # get OEIL 2
#        for i in range(2,len(O2)):
#            EX2.append(float(O2[i][0]))
#            EY2.append(float(O2[i][1]))
#            PUP2.append(float(O2[i][2]))
#        
#        ## transform in array
#        EX2 = np.array(EX2)
#        EY2 = np.array(EY2)
#        PUP2 = np.array(PUP2)
#        ###################
#        ###################
#        ## timestamp
#        tmt1 = list()
#        for i in range(0,len(tmt)):
#            if is_number(tmt[i]) == True :
#                tmt1.append(int(tmt[i]))
#            
#        tmt1 = np.array(tmt1)
#        TMT = np.transpose(tmt1)
#        
#        ## Transpose
#        EX1 = np.transpose(EX1)
#        EY1 = np.transpose(EY1)
#        PUP1 = np.transpose(PUP1)
#        EX2 = np.transpose(EX2)
#        EXY2 = np.transpose(EY2)
#        PUP2 = np.transpose(PUP2)
#        
#        ## get dataEL par menu
#        MM1, MM2 = {},{}
#        for i in range (0,len(ajfile)):
#            MM1[ajfile[i]] = [EX1[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],EY1[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],PUP1[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],TMT[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]]] ## EYE1
#            MM2[ajfile[i]] = [EX2[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],EY2[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],PUP2[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],TMT[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]]] ## EYE1
#
#
#        #colors = cm.rainbow(np.linspace(0, 1, y[1]))
#        #listla = ["]
#        namenu = ["Sujet %s \n"%(n)]
#        for i in range (0,len(ajfile)):
#            namenu.append("Game %s: "%(i+1) + ajfile[i]+ ' \n')   
#        nmenu = ''.join(namenu)
#
#
## =============================================================================
## PLOT
## =============================================================================
#
##y = np.linspace(0,len(MM1[ajfile[i]][0])),len(MM1[ajfile[i]][0])
##colors = [str(item/255.) for item in y]
#def games_plot():
#        import time
#        k = 0 ; m=0.1
#        plt.figure(figsize = (24,10),dpi=100)
#        for i in range (0,len(ajfile)):
#            textstr = " Game %s"%(i+1)
#            plt.subplot(6,6,k+1)    
#            plt.scatter(MM1[ajfile[i]][0],MM1[ajfile[i]][1],s=1,color="b", marker='o',alpha =.2,lw=0)
#            plt.text(400,-50,textstr,fontweight ='bold')
#            plt.xlim(0,1024)
#            plt.ylim(768,0)
#            plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.060, right=0.75,wspace = 0.220, hspace=0.355)
#            k+=1;m+=5
#        #plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.125, right=0.75,wspace = 0.220, hspace=0.355)
#        plt.text(2750,-2500,nmenu, va="center",fontsize=14)
#        #plt.annotate(str(namenu), xy = (6500,-3000),xytext=(6500,-3000))
#        plt.subplot(6,6,k+1)
#        plt.xticks([])
#        plt.yticks([])
#        plt.xlabel("Eye on x in pixels",fontweight = "bold")
#        plt.ylabel("Eye on y in pixels",fontweight = "bold")
#        manager = plt.get_current_fig_manager()
#        manager.window.showMaximized()
#        time.sleep(2)
#        plt.savefig("game_LT_S%s"%(n), dpi=100, facecolor='w', edgecolor='w',orientation='landscape')
#        
#        

### Ensemble de fonction de base disponible :
        ## getpxlposition() ; convpxltofdeg

## PLOT PUPILLE GAME
#y = np.linspace(0,len(MM1[ajfile[i]][0])),len(MM1[ajfile[i]][0])
#colors = [str(item/255.) for item in y]
namenu1 = ["Sujet %s \n"%(n)]
for i in range (0,len(fixg)):
    namenu1.append("Game %s: "%(i+1) + ajfile[fixg[i]]+ ' \n')   
nmenu1 = ''.join(namenu1)

k = 0 ; m=0.1 ; 
fixg = [6,19,27]
plt.figure(dpi =100)
for i in range (0,len(fixg)):
    textstr1 = " Game %s"%(i+1)
    plt.subplot(3,2,k+1)    
#    plt.scatter(MM1[ajfile[i]][0],MM1[ajfile[i]][1],s=1,color="b", marker='o',alpha =.2,lw=0)
    plt.plot(MM1[ajfile[fixg[i]]][2],"orange")
    plt.plot(MM2[ajfile[fixg[i]]][2],"purple")
    plt.title(textstr1,fontweight ='bold')
#    plt.xlim(0,1024)
#    plt.ylim(768,0)
    plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.060, right=0.75,wspace = 0.220, hspace=0.355)
    k+=1;m+=5
#plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.125, right=0.75,wspace = 0.220, hspace=0.355)
plt.text(50050,-5,nmenu1, va="center",fontsize=14)
#plt.annotate(str(namenu), xy = (6500,-3000),xytext=(6500,-3000))
plt.subplot(3,2,k+1)
plt.xticks([])
plt.yticks([])
plt.xlabel("Time - (ms)",fontweight = "bold")
plt.ylabel("Pupil Variation - (mm)",fontweight = "bold")

#          
## =======================================================================
## ## Fonction PLot all menu
## =============================================================================
##colors = cm.rainbow(np.linspace(0, 1, y[1]))
##listla = ["]
#namenu = ["Sujet %s \n"%(n)]
#for i in range (0,len(ajfile)):
#    namenu.append("Game %s: "%(i+1) + ajfile[i]+ ' \n')   
#nmenu = ''.join(namenu)
#
##y = np.linspace(0,len(MM1[ajfile[i]][0])),len(MM1[ajfile[i]][0])
##colors = [str(item/255.) for item in y]
#k = 0 ; m=0.1
#plt.figure(dpi =100)
#for i in range (0,len(ajfile)):
#    textstr = " Game %s"%(i+1)
#    plt.subplot(6,6,k+1)    
#    plt.scatter(MDEG1[ajfile[i]][0],MDEG1[ajfile[i]][1],s=1,color="b", marker='o',alpha =.2,lw=0)
#    plt.text(400,-50,textstr,fontweight ='bold')
#    plt.xlim(5,25)
#    plt.ylim(16,0)
#    plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.060, right=0.75,wspace = 0.220, hspace=0.355)
#    k+=1;m+=5
##plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.125, right=0.75,wspace = 0.220, hspace=0.355)
#plt.text(125,-40,nmenu, va="center",fontsize=14)
##plt.annotate(str(namenu), xy = (6500,-3000),xytext=(6500,-3000))
#plt.subplot(6,6,k+1)
#plt.xticks([])
#plt.yticks([])
#plt.xlabel("Eye on x in angular °",fontweight = "bold")
#plt.ylabel("Eye on y in angular °",fontweight = "bold")
