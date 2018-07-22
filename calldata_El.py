# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:46:01 2018

@author: A.P
"""

from __future__ import division, print_function
from collections import Counter
import copy ; import seaborn as sns
#runfile(u'C:\\Users\\A.P\\Desktop\\Arthur\\Manip_Run\\cobeye\\basic_EL.py')
runfile(u'C:\\Users\\Léo\\Desktop\\cobeye\\basic_EL.py')
%matplotlib auto
import pickle
#datpath = "C:\\Users\\A.P\\Desktop\\Arthur\\Manip_Run\\cobeye\\SecureData\\Eyelink\\"  
datpath = "C:\\Users\\Léo\\Desktop\\cobeye\\SecureData\\Eyelink\\"  
os.chdir(datpath)
game = pickle.load(open("GAME_.p","rb"))
dgame = pickle.load(open("DGAME_.p","rb"))
vgame = pickle.load(open("VGAME_.p","rb"))
agame = pickle.load(open("AGAME_.p","rb"))
minfos = pickle.load(open("MINFOS_.p","rb")) 

datg = pd.DataFrame(game)
datdg = pd.DataFrame(dgame)
datvg = pd.DataFrame(vgame)
datag = pd.DataFrame(agame)
datinf = pd.DataFrame(minfos)


#
## Call dataframe
data1 = pd.read_pickle("data1")


# sum(len(s) for s in sl1) ## SOMME de la longueur de toutes les listes contenus dans la liste sl1
## exempel : i = 6 ; j = 1

def nbloss(meth,wind,sep):
        """
        descriptif des variables à ajuster : dernier test sep = 50 points donc 100 ms / wind = 60 points dont 120 ms de chaque côté
        wind : taille du fenetrage autour du signal loss detecté (à 500 Hz, 60 pts représentes 120 millisecondes)
        sep : temps de séparation minmimum pour considérer deux pertes de signal différentes ou unique (relatif à la fréquence d'échantillonage : 50 == 100 ms à 500 Hz)
        """ 
        global LOS, blk, UNIQ, un1q
        n=list(minfos.keys()) ; LOS = {} ; UNIQ = {}
        for j in range (0,len(n)):  
                blk = {} ; un1q = {}
                listg = list(dgame["%s"%(n[j])].keys())
                for i in range (0,len(listg)):
                        sl = list() ; bltr= list()
#                        blksax,blksbx = [],[] ; bnksax, bnksbx = [],[]
                        ax = dgame["%s"%(n[j])]["%s"%(listg[i])]["Y1"]
                        bx = dgame["%s"%(n[j])]["%s"%(listg[i])]["Y2"]
                        ######################################################
                        if meth == 0 : ## get only common values into the two list need to choose between this and line 52 below
                            a_set = list(np.where(np.isnan(ax))[0]) 
                            b_set = list(np.where(np.isnan(bx))[0])
                            bldt = sorted(list(set(a_set) & set(b_set)))
                            unique = sorted(list(set(a_set) - set(b_set)))
                            
                        elif meth == 1 : ## merge two nan detection for ordinate EY1 et EY2 in one list without duplicate
                            bldt = list(set(list(np.where(np.isnan(ax))[0])+ list(np.where(np.isnan(bx))[0]))) 
                        ## Traitement du blink ## 
                        blink = [k for k in bldt if (k+1 - k) == 1]
                        blink = set(blink)
                        blink = sorted(list(blink))
                        ## Traitement des valeurs uniques (si meth == 0)
                        uni = [k for k in unique if (k+1 - k) == 1]
                        uni = set(uni)
                        uni = sorted(list(uni))
                        
                        
                        for ix in range(0,len(blink)-1):
                                if (blink[ix+1] - blink[ix] < sep): ## temps de separation minimum pour considérer deux pertes de signal différentes. 
                                        sl.append(blink[ix])
                                else:
                                        bltr.append(np.arange(sl[0]-wind,sl[-1]+wind))
                                        sl= list() ## permet de séparer les indexs dont la continuité n'est pas assurée, ex : i = 45 i+1 = 125, on slice ici en deux chunks.[....45][125....]
                        try: ## permet de s'affranchir de l'erreur lié au dépassement d'index si dernier point de l'array
                                bltr.append(np.arange(sl[0]-wind,sl[-1]+wind)) ## fenetrage +120 et -120 millisecondes autour de la perte de signal detectée (recommandation EyeLink et Nylstrom & Holmqvist, p176 5.7 paragraphe)
                        except IndexError:
                                pass
                        
                        un1q["%s"%(listg[i])] = uni 
#                        blk["%s"%(listg[i])] = bltr
#                        try :
#                                for ix in range(0,len(blink)-1):
#                                        if (blink[ix+1] - blink[ix] < sep): ## temps de separation minimum pour considérer deux pertes de signal différentes. 
#                                                sl.append(blink[ix])
#                                        else:
#                                                bltr.append(np.arange(sl[0]-wind,sl[-1]+wind))
#                                                sl= list() ## permet de séparer les indexs dont la continuité n'est pas assurée, ex : i = 45 i+1 = 125, on slice ici en deux chunks.[....45][125....]
#                                try: ## permet de s'affranchir de l'erreur lié au dépassement d'index si dernier point de l'array
#                                        bltr.append(np.arange(sl[0]-wind,sl[-1]+wind)) ## fenetrage +120 et -120 millisecondes autour de la perte de signal detectée (recommandation EyeLink et Nylstrom & Holmqvist, p176 5.7 paragraphe)
#                                except IndexError:
#                                        pass
#                        except IndexError:
#                                bltr.append([])
                        un1q["%s"%(listg[i])] = uni 
                        blk["%s"%(listg[i])] = bltr
                UNIQ["%s"%(n[j])] = un1q ##valeurs signal unique (pas sur les deux yeux), vide si meth == 1
                LOS["%s"%(n[j])] = blk  ##   
                

        
# =============================================================================
# UNBLINKED SIGNAL                        
# =============================================================================
## We need to replace the windowed detected blink by nan.
def blink_count(dmin):
        global nbls, BLK,nbls1,listg, data1,j,i
        # Check if signal loss matches on the two eyes :
        n=list(minfos.keys())
        BLK = {} ; intb = {} ; intb1 = []
        for i in range (0,len(n)):
                listg = list(LOS["%s"%(n[i])].keys()) ## parcours les sujets
                for j in range (0,len(listg)) : ## parcours les menus 
                        for k in range (0,len(LOS["%s"%(n[i])]["%s"%(listg[j])])): ## parcours le nombre de perte de signal detecter dans chaque menu
                                a = dgame["%s"%(n[i])]["%s"%(listg[j])]["PUP1"][LOS["%s"%(n[i])]["%s"%(listg[j])][k][0]:LOS["%s"%(n[i])]["%s"%(listg[j])][k][-1]]
                                b = dgame["%s"%(n[i])]["%s"%(listg[j])]["PUP2"][LOS["%s"%(n[i])]["%s"%(listg[j])][k][0]:LOS["%s"%(n[i])]["%s"%(listg[j])][k][-1]]
                                if len(a) and len(b) > dmin:  ## seuil basé sur des algorithmes encadrant cette durée, 100
                                        if len(np.where(np.isnan(a))[0]) and len(np.where(np.isnan(b))[0]) > 40.0 :## si le nombre de nan est supérieure à 50 points et est commun aux deux signaux alors "BLINK"
                                                 intb1.append(LOS["%s"%(n[i])]["%s"%(listg[j])][k])
                        intb["%s"%(listg[j])] = intb1
                        intb1 = []
                BLK["%s"%(n[i])] = intb
                intb =  {}
                
        ## CHECK NOMBRE DE BLINK pour chaque sujet
       
        nbls = pd.DataFrame() ; ## dataframe finale
        lbl = [] ;  nbls1 = [] ; durg = [] ; blkminute = [] ; sumblk = [] ## list intermédiaire qui permet de remplir la dataframe
        for i in range (0,len(n)):
            try:
                    listg = list(LOS["%s"%(n[i])].keys())
                    for j in range (0,len(listg)):
                            for k in range(0,len(BLK["%s"%(n[i])]["%s"%(listg[j])])):
                                    lbl.append(len(BLK["%s"%(n[i])]["%s"%(listg[j])][k])) ## durée d'un blink
                            nbls1.append(len(lbl)) ## nombre de blink pour le jeu
                            durg.append(len(dgame["%s"%(n[i])]["%s"%(listg[j])]["X1"])*0.002) # 0.002 --> 1/500 (Hz, samplerate de l'EL) ## durée du jeu
                            blkminute.append(float((len(lbl)*60)/(len(dgame["%s"%(n[i])]["%s"%(listg[j])]["X1"])*0.002))) ## normalisation du nombre blink par minute pour le jeu
                            sumblk.append(sum(lbl)*0.002)
                            lbl = []
                    nbls["N_Blinks_%s"%(n[i])] = nbls1
                    nbls["Games_%s"%(n[i])] = listg
                    nbls["Duration_%s"%(n[i])] = durg
                    nbls["blk_min_%s"%(n[i])] = blkminute
                    nbls["Sum_Duration_Blk_%s"%(n[i])] = sumblk
                    nbls["Ratio_DurBlk_DurGam_%s"%(n[i])] = np.array(sumblk)/np.array(durg) ## ration entre durée totale blink pour jeu / durée du jeu
                    nbls1 = [] ; durg = [] ; blkminute = [] ; sumblk = []
                    
            except ValueError:
                    af2 = np.full([1,1,len(nbls.columns)],np.nan)[0][0] ## ajoute NAN dans la colonne ou la ligne supplémentaire dans la dataFrame, option nécessaire lorsque le nombre de jeu n'est pas le même entre les sujets.
                    df2 = pd.DataFrame([list(af2)], columns=list(nbls.columns))
                    nbls = nbls.append(df2, ignore_index=True)
                    nbls["N_Blinks_%s"%(n[i])] = nbls1
                    nbls["Games_%s"%(n[i])] = listg
                    nbls["Duration_%s"%(n[i])] = durg
                    nbls["blk_min_%s"%(n[i])] = blkminute
                    nbls["Sum_Duration_Blk_%s"%(n[i])] = sumblk
                    nbls["Ratio_DurBlk_DurGam_%s"%(n[i])] =  np.array(sumblk)/np.array(durg) ## ration entre durée totale blink pour jeu / durée du jeu
                    nbls1 = [] ; durg = [] ; blkminute = [] ; sumblk = []
        ## procédure de normalisation des blinks --> blinks rate par (bl/minute)
                
#                        
#        #EXEMPLE :
#        for i in range (0,len(n)):  
#                plt.figure(figsize = (24,10),dpi=100)
#                ax = sns.barplot(x = nbls["Games_%s"%(n[i])],y = nbls["N_Blinks_%s"%(n[i])],data = nbls)
#                ax.set_ylim(0,100)
#                ax.set_xticklabels(ax.get_xticklabels(),rotation = 45)
#                plt.title("Blinks number by game - %s"%(n[i]))
#                plt.savefig("Graphs\\N_Blinks\\N_Blinks_%s"%(n[i]), dpi=100, facecolor='w', edgecolor='w',orientation='landscape')
#                plt.close()
#                text_file = open("Graphs\\N_Blinks\\N_Blinks_%s.txt"%(n[i]), "w")
#                for h in range(len(nbls["Games_%s"%(n[i])])):
#                        text_file.write("{} \t {} \t {} \t {}\n".format(nbls["Games_%s"%(n[i])][h],nbls["N_Blinks_%s"%(n[i])][h],nbls["blk_min_%s"%(n[i])][h],nbls["Duration_%s"%(n[i])][h]))
#                text_file.close()
#        plt.show()        
#        nbls.to_pickle("blink_count")
        ## pour call la data frame --> df = pd.read_pickle('blink_count')
        
        ## Try creation dataframe full of data with 4 columns : Nblinks, Duration , Games, Sujets
        data1 = pd.DataFrame(columns=["N_Blinks","blink_minute","Duration_Total_Blk - Seconde","Duration - Seconde","Ratio_DurBlk_DurJeu","Game","Sujet","Lab"])
        for i in range (0,len(n)):
                listg = list(LOS["%s"%(n[i])].keys())
                for j in range (0,len(listg)):
                        data1 = data1.append({'N_Blinks' : nbls["N_Blinks_%s"%(n[i])][j],'blink_minute':nbls["blk_min_%s"%(n[i])][j],'Duration_Total_Blk - Seconde':nbls["Sum_Duration_Blk_%s"%(n[i])][j],'Duration - Seconde': nbls["Duration_%s"%(n[i])][j], "Ratio_DurBlk_DurJeu":nbls["Ratio_DurBlk_DurGam_%s"%(n[i])][j],'Game': nbls["Games_%s"%(n[i])][j],'Sujet' : "%s"%(n[i]),'Lab' : "%s"%(minfos["%s"%(n[i])]["INFLAB"])},ignore_index=True)

        data1.to_pickle("data1")                

        


## remplace les chunks déterminer par la fonction nbloss() par des NaN dans les tables de données brutes et converties en degrés.                
def recode():
    global game1, dgame1
    game1 = copy.deepcopy(game) ; dgame1 = copy.deepcopy(dgame) ; vgame1 = copy.deepcopy(vgame) ; agame1 = copy.deepcopy(agame)
    n=list(minfos.keys()) ; 
    for j in range (0,len(n)):
        listg1 = list(LOS["%s"%(n[j])].keys())
        blknan = {};
        for i in range (0,len(listg1)):
            for k in range(0,len(LOS["%s"%(n[j])]["%s"%(listg1[i])])):
                try:
                    game1["%s"%(n[j])]["%s"%(listg1[i])]["X1"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]] = np.NaN 
                    game1["%s"%(n[j])]["%s"%(listg1[i])]["Y1"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    game1["%s"%(n[j])]["%s"%(listg1[i])]["X2"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    game1["%s"%(n[j])]["%s"%(listg1[i])]["Y2"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    game1["%s"%(n[j])]["%s"%(listg1[i])]["PUP1"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    game1["%s"%(n[j])]["%s"%(listg1[i])]["PUP2"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                
                    dgame1["%s"%(n[j])]["%s"%(listg1[i])]["X1"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]] = np.NaN 
                    dgame1["%s"%(n[j])]["%s"%(listg1[i])]["Y1"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    dgame1["%s"%(n[j])]["%s"%(listg1[i])]["X2"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    dgame1["%s"%(n[j])]["%s"%(listg1[i])]["Y2"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    dgame1["%s"%(n[j])]["%s"%(listg1[i])]["PUP1"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    dgame1["%s"%(n[j])]["%s"%(listg1[i])]["PUP2"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    
                    vgame1["%s"%(n[j])]["%s"%(listg1[i])]["X1"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]] = np.NaN 
                    vgame1["%s"%(n[j])]["%s"%(listg1[i])]["Y1"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    vgame1["%s"%(n[j])]["%s"%(listg1[i])]["X2"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    vgame1["%s"%(n[j])]["%s"%(listg1[i])]["Y2"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    vgame1["%s"%(n[j])]["%s"%(listg1[i])]["PUP1"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    vgame1["%s"%(n[j])]["%s"%(listg1[i])]["PUP2"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                
                    agame1["%s"%(n[j])]["%s"%(listg1[i])]["X1"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]] = np.NaN 
                    agame1["%s"%(n[j])]["%s"%(listg1[i])]["Y1"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    agame1["%s"%(n[j])]["%s"%(listg1[i])]["X2"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    agame1["%s"%(n[j])]["%s"%(listg1[i])]["Y2"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    agame1["%s"%(n[j])]["%s"%(listg1[i])]["PUP1"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                    agame1["%s"%(n[j])]["%s"%(listg1[i])]["PUP2"][LOS["%s"%(n[j])]["%s"%(listg1[i])][k]]= np.NaN 
                except IndexError:
                    continue

    pickle.dump(game1,open(datpath +"GAME1_.p","wb"))        
    pickle.dump(dgame1,open(datpath +"DGAME1_.p","wb"))
    pickle.dump(vgame1,open(datpath +"VGAME1_.p","wb"))        
    pickle.dump(agame1,open(datpath +"AGAME1_.p","wb"))*


## Procédure de conversion pour les table pickle to *.mat pour les ouvrir en matlab
import numpy, scipy.io
scipy.io.savemat(datpath + 'Raw_pxl.mat', mdict={'Position_pxl': game1})
scipy.io.savemat(datpath + 'Raw_deg.mat', mdict={'Position_deg': dgame1})
scipy.io.savemat(datpath + 'Raw_vel.mat', mdict={'Velocity': vgame1})
scipy.io.savemat(datpath + 'Raw_acc.mat', mdict={'Acceleration': agame1})
scipy.io.savemat(datpath + 'InfosSub.mat', mdict={'Infos_Sub': minfos})

game1 = pickle.load(open("GAME1_.p","rb")) ## data deblinké
dgame1 = pickle.load(open("DGAME1_.p","rb")) ## data deblinké
vgame1 = pickle.load(open("VGAME1_.p","rb")) ## data deblinké
agame1 = pickle.load(open("AGAME1_.p","rb")) ## data deblinké
               
### Analyse de saccade nécessite une adaptation selon les jeux,  pour les jeux poursuite les seuils de vitesse et d'accélération devront être adaptés.
### 3 Variables à determiner pour les saccades : Fréquences, Amplitude, Orientation.
def nsacc():
        global sc, sac,ss, lg
        """
        ["%s"%(list(vgame["L%s_S%s"%(m,n[j])].keys())[i]))] --> Cette expression me permet de récupérer le nom des jeux que l'on peut appeler 
        pour le sujet en question. list(vgame["L0_S5"].keys())[0] permet d'appeler le jeu "1_intro"
        ths : threshold saccade, fixé à 5 °/s
        """
#        ns = list(vgame1["%s"%(n)].keys())
        als = {} ; ths = 5
        sc = {} ; ss = list(minfos.keys())
        for j in range (0,len(ss)):
                lg = list(vgame1["%s"%(ss[j])].keys())
                for i in range (0,len(lg)):
#                        lg = list(vgame1["%s"%(ns[j])].keys())
                        sac = {}; slx1 = list() ; blsx1= list()
                        if lg[i] != 'PursG1' or lg[i] != 'PursD1' or lg[i] != 'PursH1' or lg[i] != 'PursB1': ## nécessité de traité les jeux "poursuite" différemments
                                sax = vgame1["%s"%(ss[j])]["%s"%(lg[i])]["X1"] ## voir explication fonction
                                say = vgame1["%s"%(ss[j])]["%s"%(lg[i])]["Y1"]
                                sbx = vgame1["%s"%(ss[j])]["%s"%(lg[i])]["X2"]
                                sby = vgame1["%s"%(ss[j])]["%s"%(lg[i])]["Y2"]
                        
                        
                                sac["X1"] = sorted(list(set(np.where(sax > ths)[0])))
                                sac["Y1"] = sorted(list(set(np.where(say > ths)[0])))
                                sac["X2"] = sorted(list(set(np.where(sbx > ths)[0])))
                                sac["Y2"] = sorted(list(set(np.where(sby > ths)[0])))
                                
                                sx1 = [k for k in sac["X1"] if (k+1 - k) == 1]
                                sx2 = [k for k in sac["X2"] if (k+1 - k) == 1]
                                sy1 = [k for k in sac["Y1"] if (k+1 - k) == 1]
                                sy2 = [k for k in sac["Y2"] if (k+1 - k) == 1]
                                
                                
                                
                                
                                for ix in range(0,len(sx1)-1):
                                        if (sx1[ix+1] - sx1[ix] < sep): ## temps de separation minimum pour considérer deux pertes de signal différentes. 
                                                slx1.append(sx1[ix])
                                        else:
                                                blsx1.append(np.arange(slx1[0]-wind,slx1[-1]+wind))
                                                sl= list() ## permet de séparer les indexs dont la continuité n'est pas assurée, ex : i = 45 i+1 = 125, on slice ici en deux chunks.[....45][125....]
                                try: ## permet de s'affranchir de l'erreur lié au dépassement d'index si dernier point de l'array
                                        blsx1.append(np.arange(slx1[0]-wind,slx1[-1]+wind)) ## fenetrage +120 et -120 millisecondes autour de la perte de signal detectée (recommandation EyeLink et Nylstrom & Holmqvist, p176 5.7 paragraphe)
                                except IndexError:
                                        pass                           
                                
                                
                        
                        
                        
                        sc["%s"%(lg[i])] = sac
                als["%s"%(ss[j])] = sc
                sc={}
                        
                                
                                
                                
                                
                                
        
      ######################################################

    a_set = list(np.where(np.isnan(ax))[0]) 
    b_set = list(np.where(np.isnan(bx))[0])
    bldt = sorted(list(set(a_set) & set(b_set)))
    unique = sorted(list(set(a_set) - set(b_set)))
    
elif meth == 1 : ## merge two nan detection for ordinate EY1 et EY2 in one list without duplicate
    bldt = list(set(list(np.where(np.isnan(ax))[0])+ list(np.where(np.isnan(bx))[0]))) 
## Traitement du blink ## 
blink = [k for k in bldt if (k+1 - k) == 1]
blink = set(blink)
blink = sorted(list(blink))
## Traitement des valeurs uniques (si meth == 0)
uni = [k for k in unique if (k+1 - k) == 1]
uni = set(uni)
uni = sorted(list(uni))


for ix in range(0,len(blink)-1):
        if (blink[ix+1] - blink[ix] < sep): ## temps de separation minimum pour considérer deux pertes de signal différentes. 
                sl.append(blink[ix])
        else:
                bltr.append(np.arange(sl[0]-wind,sl[-1]+wind))
                sl= list() ## permet de séparer les indexs dont la continuité n'est pas assurée, ex : i = 45 i+1 = 125, on slice ici en deux chunks.[....45][125....]
try: ## permet de s'affranchir de l'erreur lié au dépassement d'index si dernier point de l'array
        bltr.append(np.arange(sl[0]-wind,sl[-1]+wind)) ## fenetrage +120 et -120 millisecondes autour de la perte de signal detectée (recommandation EyeLink et Nylstrom & Holmqvist, p176 5.7 paragraphe)
except IndexError:
        pass                           
        
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                