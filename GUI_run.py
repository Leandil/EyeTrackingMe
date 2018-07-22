# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 12:34:56 2018

@author: A.P
"""

import sys, os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout,QGroupBox, QApplication, QDialog, QGridLayout, QLayout, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

import basic_EL
import random, re , csv
import numpy as np


class Ui_Dialog(QDialog):
        def __init__(self, parent=None):
            super(Ui_Dialog, self).__init__(parent)
            self.setupUi(self)
            self.setupPlot()

        def setupUi(self, Dialog):
            Dialog.setObjectName("Dialog")
            Dialog.resize(1600, 1200)
            Dialog.setWindowTitle("CobEye")
            
            
            self.createGridLayout()
            windowLayout = QVBoxLayout()
            windowLayout.addWidget(self.horizontalGroupBox)
            self.setLayout(windowLayout)
            
            
            QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        def loadrawData(self):
                global dpath1,y1,x1
                options = QFileDialog.Options()
#                options |= QFileDialog.DontUseNativeDialog
                fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","edf file (*.edf);;All Files (*);;Python Files (*.py)", options=options)
                if fileName:
                    dpath1 = os.path.dirname(os.path.realpath(fileName))
                    y1 =int(dpath1.split("\\")[-2][-1]) ; x1=int(dpath1.split("\\")[-1][-1])
                    self.makedat(y1,x1)
#                for i in range (0,len(nam)):
#                        self.gamelist.addItem(nam[i])
                    
                    
        
        def setupPlot(self):
            self.setLayout(QHBoxLayout())
            self.layout().setContentsMargins(0, 0, 0, 0)
            self.figure = plt.figure(figsize = (250,225)) ## gère la taille de la figure dans le Layout (pas compris vraiment en quelle unité)
            self.figure.set_facecolor("none")
            self.canvas = FigureCanvas(self.figure)
        
            self.toolbar = NavigationToolbar(self.canvas, self)
        
            self.widget = QtWidgets.QWidget()
            layout = QVBoxLayout()
            self.widget.setLayout(layout)
            self.layout().setContentsMargins(0, 0, 0, 0)
            layout.addWidget(self.toolbar)
            layout.addWidget(self.canvas)
            self.layout().addWidget(self.widget)
#        
#             self.plot()
#            self.plot_pxl()
#            self.plot_deg()
#            self.plot_vel()
#            self.plot_acc()

        def plot_save(self):
                name, _ = QFileDialog.getSaveFileName(self, 'QFileDialog.getSaveFileName()',""," tiff (*.tif);; pdf (*.pdf);; png (*.png);; svg (*.svg);; eps (*.eps)")
#                file = open(name,'w')
                plt.savefig("%s"%(name), dpi=100, facecolor='w', edgecolor='w',orientation='landscape')
#                text = self.textEdit.toPlainText()
#                file.write(text)
#                file.close()
                
        def plot_clear(self):
                self.figure.clear()
                self.canvas.draw()
# =============================================================================
# ## fonction plots        
# ============================================================================
            
#        def plot(self):
#                
##            if type(filename) == str:
#            data = [random.random() for i in range(10)]
#            self.figure.clear()
#            ax = self.figure.add_subplot(111)
#            ax.plot(data["Sacc1"]["X1"], '*-')
#            self.canvas.draw()
## FONCTIoN QUI PERMET EN fonction du bouton cliqué : raw pixel.... acceleration de charger les données adéquates.
        def fill_combo_pxl(self):
            self.gamelist.clear()
            for i in range (0,len(nam)):
                self.gamelist.addItem(nam[i],G["%s"%(nam[i])]["X1"])
#                self.checkBox8.
        def fill_combo_deg(self):
            self.gamelist.clear()
            for i in range (0,len(nam)):
                self.gamelist.addItem(nam[i],DG["%s"%(nam[i])]["X1"])
        def fill_combo_vel(self):
            self.gamelist.clear()
            for i in range (0,len(nam)):
                self.gamelist.addItem(nam[i],VG["%s"%(nam[i])]["X1"])
        def fill_combo_acc(self):
            self.gamelist.clear()
            for i in range (0,len(nam)):
                self.gamelist.addItem(nam[i],AG["%s"%(nam[i])]["X1"])
            
        def plot_pxl(self):
#            global currentItem
                
#            if G != {}:
            currentItem = str(self.gamelist.currentText())
#                    data = G
#            data = [random.random() for i in range(10)]
            self.figure.clear()
            
            ax = self.figure.add_subplot(111)
            
            ## EX1
            if self.checkBox8.isChecked() == True:
                ax.plot(G["%s"%(currentItem)]["TS"],G["%s"%(currentItem)]["X1"], '*-')
                ax.set_ylabel("Left Eye Position on X axis (pxl)")
#                plt.show()
            ##EX2    
            if self.checkBox9.isChecked() == True:
                ax.plot(G["%s"%(currentItem)]["TS"],G["%s"%(currentItem)]["Y1"], '*-')
                ax.set_ylabel("Left Eye Position on Y axis (pxl)")
#                plt.show()
            ## PUP1
            if self.checkBox10.isChecked() == True:
                ax.plot(G["%s"%(currentItem)]["TS"],G["%s"%(currentItem)]["PUP1"], '*-')
                ax.set_ylabel("Pupil Dyn of Left Eye")
#                plt.show()
                
            ## EX2
            if self.checkBox11.isChecked() == True:
                ax.plot(G["%s"%(currentItem)]["TS"],G["%s"%(currentItem)]["X2"], '*-')
                ax.set_ylabel("Right Eye Position on X axis (pxl)")
#                plt.show()
            ## EY2
            if self.checkBox12.isChecked() == True:
                ax.plot(G["%s"%(currentItem)]["TS"],G["%s"%(currentItem)]["Y2"], '*-')
                ax.set_ylabel("Right Eye Position on Y axis (pxl)")
#                plt.show()
            ## PUP2
            if self.checkBox13.isChecked() == True:
                ax.plot(G["%s"%(currentItem)]["TS"],G["%s"%(currentItem)]["PUP2"], '*-')
                ax.set_ylabel("Pupil Dyn of Right Eye")
#                plt.show()
                
            ax.set_xlabel("Time (sec)")
#                    ax.set_ylabel("Eye Position (pxl)")
            plt.subplots_adjust(top=0.92,bottom=0.08,left=0.04,right=0.985,hspace=0.2,wspace=0.2)
            self.canvas.draw()
#            self.canvas.show()
                    
        def plot_deg(self):
            currentItem = str(self.gamelist.currentText())
            #                    data = G
            #            data = [random.random() for i in range(10)]
            self.figure.clear()
            
            ax = self.figure.add_subplot(111)
            
            ## EX1
            if self.checkBox8.isChecked() == True:
                ax.plot(DG["%s"%(currentItem)]["TS"],DG["%s"%(currentItem)]["X1"], '*-')
                ax.set_ylabel("Left Eye Position on X axis (°)")
#                plt.show()
            ##EX2    
            if self.checkBox9.isChecked() == True:
                ax.plot(DG["%s"%(currentItem)]["TS"],DG["%s"%(currentItem)]["Y1"], '*-')
                ax.set_ylabel("Left Eye Position on Y axis (°)")
#                plt.show()
            ## PUP1
            if self.checkBox10.isChecked() == True:
                ax.plot(DG["%s"%(currentItem)]["TS"],DG["%s"%(currentItem)]["PUP1"], '*-')
                ax.set_ylabel("Pupil Dynamic of Left Eye")
                
            ## EX2
            if self.checkBox11.isChecked() == True:
                ax.plot(DG["%s"%(currentItem)]["TS"],DG["%s"%(currentItem)]["X2"], '*-')
                ax.set_ylabel("Right Eye Position on X axis (°)")
            ## EY2
            if self.checkBox12.isChecked() == True:
                ax.plot(DG["%s"%(currentItem)]["TS"],DG["%s"%(currentItem)]["Y2"], '*-')
                ax.set_ylabel("Right Eye Position on Y axis (°)")
            ## PUP2
            if self.checkBox13.isChecked() == True:
                ax.plot(DG["%s"%(currentItem)]["TS"],DG["%s"%(currentItem)]["PUP2"], '*-')
                ax.set_ylabel("Pupil Dynamic of Righ Eye")
                
            ax.set_xlabel("Time (sec)")
#                    ax.set_ylabel("Eye Position (pxl)")
            plt.subplots_adjust(top=0.92,bottom=0.08,left=0.04,right=0.985,hspace=0.2,wspace=0.2)
            self.canvas.draw()
#            self.canvas.show()
            
        def plot_vel(self):
            currentItem = str(self.gamelist.currentText())
            #                    data = G
            #            data = [random.random() for i in range(10)]
            self.figure.clear()
            
            ax = self.figure.add_subplot(111)
            
            ## EX1
            if self.checkBox8.isChecked() == True:
                ax.plot(VG["%s"%(currentItem)]["X1"], '*-')
                ax.set_ylabel("Left Eye Velocity on X axis (°/s)")
                plt.show()
            ##EX2    
            if self.checkBox9.isChecked() == True:
                ax.plot(G["%s"%(currentItem)]["Y1"], '*-')
                ax.set_ylabel("Eye Velocity on Y axis (°/s)")
                plt.show()
            ## PUP1
            if self.checkBox10.isChecked() == True:
                ax.plot(G["%s"%(currentItem)]["PUP1"], '*-')
                ax.set_ylabel("Pupil Dyn")
                
            ## EX2
            if self.checkBox11.isChecked() == True:
                ax.plot(G["%s"%(currentItem)]["X2"], '*-')
                ax.set_ylabel("Eye Position (pxl)")
            ## EY2
            if self.checkBox12.isChecked() == True:
                ax.plot(G["%s"%(currentItem)]["Y2"], '*-')
                ax.set_ylabel("Eye Position (pxl)")
            ## PUP2
            if self.checkBox13.isChecked() == True:
                ax.plot(G["%s"%(currentItem)]["PUP2"], '*-')
                ax.set_ylabel("Pupil Dyn")
                
            ax.set_xlabel("Time (ms)")
            #                    ax.set_ylabel("Eye Position (pxl)")
            plt.subplots_adjust(top=0.92,bottom=0.08,left=0.04,right=0.985,hspace=0.2,wspace=0.2)
            self.canvas.draw()

        def plot_acc(self):
            if AG != {}:
#                    data = AG
                    self.figure.clear()
                    ax = self.figure.add_subplot(111)
                    ax.plot(AG["%s"%(nam[i])]["X1"], '*-')
                    ax.set_xlabel("Time (ms)")
                    ax.set_ylabel("Eye acceleration (deg/s²)")
                    plt.subplots_adjust(top=0.92,bottom=0.08,left=0.04,right=0.985,hspace=0.2,wspace=0.2)
                    self.canvas.draw()    
        
## Lié la liste de jeux dans le menu déroulant avec des données ou un boutton
#        def loadgame():
#                if self.gamelist() == 
#                
                        
                        
#        def dynplot(ns,name,name1,name2):
#                import pyqtgraph as pg
#                import pyqtgraph.exporters
#                import numpy as np
#                
#                # define the data
#                theTitle = "pyqtgraph plot"
#                y = game["S%s"%(x1)]["%s"%(name)]["%s"%(name1)]
#                y2 = game["S%s"%(x1)]["%s"%(name)]["%s"%(name2)]
#                x = range(0,len(y))
#                
#                # create plot
#                plt = pg.plot()
#                plt.showGrid(x=True,y=True)
#                plt.addLegend()
#                
#                # set properties
#                if (name1 == "X1"):
#                        plt.setLabel('left', 'EyePosition', units='pxl')
#                elif (name1 == "PUP1"):
#                        plt.setLabel('left', 'PupDynamic', units='-')
#                plt.setLabel('bottom', 'Time', units='sec')
#                plt.setXRange(0,len(y))
#                plt.setYRange(0,max(y))
#                plt.setWindowTitle('pyqtgraph plot')
#                
#                # plot
#                c1 = plt.plot(x, y, pen='b', symbol='x', symbolPen='b', symbolBrush=0.2, name='blue')
#                c2 = plt.plot(x, y2, pen='m', symbol='o', symbolPen='r', symbolBrush=0.2, name='magenta')

        def makedat(self,y1,x1):
                global GAME,DGAME,VGAME,AGAME,MINFOS,G,DG,VG,AG
                GAME,DGAME,VGAME,AGAME,MINFOS = {},{},{},{},{}
                ilab = []
                
                clabo = ["Institut de la Vision","ICM","GIBSA","IMPACT","Inférence et Comportements Visuels","Perception et Sensori-Motricité","Perception et Attention","Vision Action Cognition","Psychologie de la Perception","SCAlab","Neuroergonomie"]
                llabo = ["Paris_75012","Paris_75013","Grenoble_38185","Lyon_69123","Marseille_13055","Grenoble_38185", "Marseille_13055", "Boulogne Billancourt_92012", "Paris_75006", "Lille_59350", "Toulouse_31555"]
                rlabo = ["Jean Lorenceau", "Pierre Pouget", "Nathalie Guyader", "Denis Pelisson", "Anna Montagnini", "Carole Peyrin", "Françoise Vitu", "Céline Paeye", "Thérèse Collins", "Laurent Madelain", "Vsevolod Peysakhovich"]
                
                ilab = [clabo[y1],llabo[y1],rlabo[y1]] 
                
                
                
                self.checkasc(y1,x1);self.sub_cut(y1,x1) ; self.get_etdata(y1,x1);self.gnames();self.convpxltodeg(57,2,29,0,0); self.degtovel(500) ; self.veltoacc(500) ;self.rectime(500)
                
                #print (time.clock()) ## check le temps
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
                
                GAME["S%s"%(x1)] = G ; 
                DGAME["S%s"%(x1)] = DG
                VGAME["S%s"%(x1)] = VG
                AGAME["S%s"%(x1)] = AG
                MINFOS["S%s"%(x1)] = INFOS
                
        def atoi(self,text):
            return int(text) if text.isdigit() else text

        def natural_keys(self,text):
            '''
            alist.sort(key=natural_keys) sorts in human order
            http://nedbatchelder.com/blog/200712/human_sorting.html
            (See Toothy's implementation in the comments)
            '''
            return [ self.atoi(c) for c in re.split('(\d+)', text) ]        


        def is_number(self,s):
            try: 
                float(s)
                return True
            except ValueError:
                pass
         
            try:
                import unicodedata
                unicodedata.numeric(s)
                return True
            except (TypeError, ValueError):
                pass
         
            return False
        ## CHECK AND CONVERT EDF TO ASC
        def checkasc(self,m,n):     
                cmd = 'C:\\Users\\A.P\\Desktop\\Arthur\\Tools_EYELINK\\edf2asc.exe'
                os.chdir(dpath1[:-5] + "L%s\\S%s\\"%(m,n))
                dir1 = os.path.dirname(dpath1[:-5] + "L%s\\S%s\\"%(m,n))
                for root,dirs,files in os.walk(dir1):
                   for file in sorted(files):
                       if file.endswith(".edf"):
                               ascfile = file[:-3]+"asc"
                               if not os.path.isfile(ascfile) : #and not file.endswith(".asc"):
                                   subprocess.run([cmd, file]) #shell = True, check = True)
        #                           subprocess.Popen([cmd,file])

        def sub_cut(self,m,n):
                """ This function allows us to get all the namefiles ending with the extension .eos and .asc.
                In order to get the time onset and the offset timestamps in each eos files and use it to slice the ascii files. These timestamps are stored in 
                "index" dictionnary : column 3 : beginning of the game // column 4 : end of the game """
                global ajfile,allaj, eosall,ajall,index,elfile
                
                #        m = 7 ; n = 2 ;
                ajfile= list() ; allaj = {}
                os.chdir(dpath1[:-5] + "L%s\\S%s\\"%(m,n))
                dir1 = os.path.dirname(dpath1[:-5] + "L%s\\S%s\\"%(m,n))
                for root,dirs,files in os.walk(dir1):
                    for file in sorted(files):
                        if file.endswith(".eos"):
                            print(os.path.join(root,file))
                            ajfile.append(file)
                            ajfile.sort(key=self.natural_keys)
                        if file.endswith(".asc"):
                            print(os.path.join(root,file))
                            elfile = os.path.join(root,file)  
                        
        #                else:
        #                    print("Miss Asc FILE")
        
                eosall = {}
                for i in range (0,len(ajfile)):    
                    with open(ajfile[i],"rt") as csvfile:
                #            csvReader = csv.reader(codecs.open("Sujet%s\A_S%s_%s_%s.aju" %(n,m,s,b), 'rU', 'utf-16'))
                            data= csv.reader(csvfile,delimiter=',') ##pour symboliser des colonnes delimiter = ";"
                            l = list()
                            for row in data:
                                #print type(row)
                                #print row ## affiche la colonne 2
                                l.append(row) ## recupère la colonne où sont affichés les numéros d'essais
                            eosall["%s"%(ajfile[i])]=l
                            
                
                    aj = list();ajall={}              
                    for i in range (0,len(eosall)):    
                        for j in range (0,len(eosall["%s"%(ajfile[i])])):
                            aj.append(eosall["%s"%(ajfile[i])][j][0].split())
                        ajall["%s"%(ajfile[i])] = aj
                        aj = list()
                            
                    
                    index = {}
                    for i in range (0,len(ajall)):
                        for j in range(0,len(ajall[ajfile[i]])-1):
                            if len(ajall[ajfile[i]][j]) == 5:    
                                index[ajfile[i]]= [ajall[ajfile[i]][j][1],ajall[ajfile[i]][j+1][1],int(ajall[ajfile[i]][j+1][2]),int(ajall[ajfile[i]][j+3][16]),int(ajall[ajfile[i]][-2][16])]
                    





        def get_etdata(self,m,n):
                """ From the timestamps get in the first function, this function allos us to get the eye positions in x and y, then pupil dynamic for each eye in binocular or one eye in monocular recording"""
                global taboo,tabo3,O3,O1,O2,tmt,indo1,indo2,EX1,EY1,PUP1,EX2,EY2,PUP2,TMT,MM1,MM2, namenu, nmenu, menus_ind
                global hdet,pr,date,sampler,duration_sec,ilab, clabo, llabo,rlabo
                
        #        clabo = ["Institut de la Vision","ICM","GIBSA","IMPACT","Inférence et Comportements Visuels","Perception et Sensori-Motricité","Perception et Attention","Vision Action Cognition","Psychologie de la Perception","SCAlab","Neuroergonomie"]
        #        llabo = ["Paris - 75012","Paris - 75013","Grenoble - 38185","Lyon - 69123","Marseille - 13055","Grenoble - 38185", "Marseille - 13055", "Boulogne Billancourt - 92012", "Paris - 75006", "Lille - 59350", "Toulouse - 31555"]
        #        rlabo = ["Jean Lorenceau", "Pierre Pouget", "Nathalie Guyader", "Denis Pelisson", "Anna Montagnini", "Carole Peyrin", "Françoise Vitu", "Céline Paeye", "Thérèse Collins", "Laurent Madelain", "Vsevolod Peysakhovich"]

                ## information fichier EOS / get timestamp début / fin // Slice in ASCII file 
                menus_ind = {}
                for i in range (0,len(ajfile)):
                    menus_ind[ajfile[i]] = [index[ajfile[i]][3],index[ajfile[i]][4]]## index de la timeline ASCII de début et de fin pour chaque menu 
                                                  
        
                
                with open(elfile,"rt") as elf:
                    data= csv.reader(elf,delimiter='\t') ##pour symboliser des colonnes delimiter = ";"
                    tabo3=list(data)       
                
                ## decoupage fichier .asc
                taboo = tabo3[28:] ## data
                hdet2 = tabo3[0:28] ## header du fichier .acs
                
                
                #• Infos relative au header hdet
                hdet = list() 
                for i in range (0,len(hdet2)):
                        for j in range(0,len(hdet2[i])):
                                try :
                                        hdet.append(hdet2[i][j].split(" "))
                                except IndexError:
                                        break
        #                        hdet3.append(hdet1)
        #                        hdet1 = []
                
        #        hdet = hdet1 + hdet2[i:] ## reformation du header splitter de la même manière
                ## trouver le sample rate
                pr = [(i, hdet.index("RECORD")) for i, hdet in enumerate(hdet) if "RECORD" in hdet] ## renvoie [(ligne,position dans la ligne)]
                sampler = float(hdet[pr[0][0]][pr[0][1]+2]) ## récupère sample rate
                ## trouver la date
                rd = [(i, hdet.index("DATE:")) for i, hdet in enumerate(hdet) if "DATE:" in hdet] ## renvoie [(ligne,position dans la ligne)]
                date = hdet[rd[0][0]][rd[0][1]+1] + str("_") + hdet[rd[0][0]][rd[0][1]+2] + str("_") + hdet[rd[0][0]][rd[0][1]+3] + str("_") + hdet[rd[0][0]][rd[0][1]+5] ## récupére date d'enregistrement
                ## calculer la durée de l'enregistrement
                ost =[(i, hdet.index("INPUT")) for i, hdet in enumerate(hdet) if "INPUT" in hdet]
                duration_sec = (int(taboo[-1][1])-int(hdet[ost[0][0]+1][0]))/float(1000) ## donne le temps en secondes de l'enregistrement
                ## infos du labo de l'enregistrement
                
        #        
                
                
                ## Infos relatives au données eyes taboo
                for i in range (2,len(taboo)):
                    while '' in taboo[i]:
                        taboo[i].remove('')
                
                    
                O3 = list()
                for i in range(0,len(taboo)-2): ## recupere les colonnes de data
                    O3.append(taboo[i])
                    
                O1 = list() ; O2 = list() ; tmt = list()
                for i in range (0,len(O3)): ## Reduire aux coordonnées x,y et pupille (colonnes 1,2,3 respectivement)
                    O1.append(O3[i][1:4]) ## oeil 1
                    O2.append(O3[i][4:7]) ## oeil 2
                    tmt.append(O3[i][0]) ## timestamp
                    
                ind1 = list()
                for i in range (0,len(O1)):
                    for j in range (0,len(O1[i])):
                        if O1[i][j]=='   .':
                            ind1.append([i,int(tmt[i])])
                
                ind2 = list()            
                for i in range (0,len(O2)):
                    for j in range (0,len(O2[i])):
                        if O2[i][j]=='   .':
                            ind2.append([i,int(tmt[i])])
                
                ## ordonne les indexs            
                import itertools
                ind1.sort()
                ind2.sort()
                
                indo1 = list(ind1 for ind1, _ in itertools.groupby(ind1))
                indo2 = list(ind2 for ind2, _ in itertools.groupby(ind2))
                    
                
                ## on remplace les points par des 'NAN'
                for i in range (0,len(indo1)):
                    O1[indo1[i][0]] = [np.NaN,np.NaN,np.NaN]
                for i in range (0,len(indo2)):
                    O2[indo2[i][0]] = [np.NaN,np.NaN,np.NaN]
                    
                ## List to get information from OEIL1 et OEIL2
                EX1 = list() ## coordonnée en x
                EY1= list() ## coordonnée en y
                PUP1 = list() ## pupille
                EX2 = list()
                EY2 = list()
                PUP2 = list()
                
                
                ## get OEIL 1    
                for i in range(0,len(O1)):
                    if len(O1[i]) == 3:
                        EX1.append(float(O1[i][0]))
                        EY1.append(float(O1[i][1]))
                        PUP1.append(float(O1[i][2]))
                
                ## transform in array
                EX1 = np.array(EX1)
                EY1 = np.array(EY1)
                PUP1 = np.array(PUP1)
                
                
                # get OEIL 2
                for i in range(0,len(O2)):
                    if len(O2[i]) == 3:
                        EX2.append(float(O2[i][0]))
                        EY2.append(float(O2[i][1]))
                        PUP2.append(float(O2[i][2]))
                
                ## transform in array
                EX2 = np.array(EX2)
                EY2 = np.array(EY2)
                PUP2 = np.array(PUP2)
                ###################
                ## timestamp
                tmt1 = list()
                for i in range(0,len(tmt)):
                    if self.is_number(tmt[i]) == True :
                        tmt1.append(int(tmt[i]))
                    
                tmt1 = np.array(tmt1)
                TMT = np.transpose(tmt1)
                ## Transpose
                EX1 = np.transpose(EX1)
                EY1 = np.transpose(EY1)
                PUP1 = np.transpose(PUP1)
                EX2 = np.transpose(EX2)
                EXY2 = np.transpose(EY2)
                PUP2 = np.transpose(PUP2)
                
        ## get dataEL par menu
                MM1, MM2 = {},{}
                for i in range (0,len(ajfile)):
                    MM1[ajfile[i]] = [EX1[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],EY1[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],PUP1[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],TMT[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]]] ## EYE1
                    MM2[ajfile[i]] = [EX2[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],EY2[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],PUP2[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],TMT[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]]] ## EYE1
        
        
                namenu = ["L%s_Sujet %s \n"%(m,n)]
                for i in range (0,len(ajfile)):
                    namenu.append("Game %s: "%(i+1) + ajfile[i]+ ' \n')   
                nmenu = ''.join(namenu)

        def convpxltodeg(self,dis,c,win,order,deriv):
                """
                Function pixel to angular degree (pour une distance oeil écran de 1000 mm ):
                dis = distance Oeil/Ecran en cm ; 
                hs = taille horizontale de l'écran en cm ; vs = taille verticale de l'écran en cm 
                Facdis = ref distance O/Screen = 57 cm --> 1 cm == 1°
                Taille H pixel sur dispositif LiveTrack avec écran BenQ XL2411 pour une résolution 1024*768 = 0.0521 cm 
                Taille V pixel sur dispositif LiveTrack avec écran BenQ XL2411 pour une résolution 1024*768 = 0.0390 cm 
                24 pouces = 531.36 x 298.89‎
                28 pouces = 620.928 x 341.28
                c peut prendre la valeur 1 qui correspond à un écran de 24 pouces
                la valeur 2 qui correspond à un écran de 28 pouces
                """
                global MDEG1,MDEG2,tpx,tpy
                MDEG1 = {} ; MDEG2 =  {}
                ## variables setup :
                if c == 1 : ## SETUP IDV
                        ## 24 inches parameters
                        hs = 53.136
                        vs = 29.889
                if c == 2 :  ## SETUP
                        ## 28 inches parameters
                        hs = 62.0928
                        vs = 34.128
                        
        
                        
                factdis = (dis / 57.0) ## facteur de correspondance distance oeil/ecran pour 1° = x cm sur l'écran
                tpx = hs/1024.0 ; tpy = vs/768.0
                for i in range (0,len(ajfile)):
                        MDEG1[ajfile[i]] = [(self.s_g(MM1[ajfile[i]][0],win,order,deriv)*tpx)/factdis,(self.s_g(MM1[ajfile[i]][1],win,order,deriv)*tpy)/factdis,MM1[ajfile[i]][2],MM1[ajfile[i]][3]]
                        MDEG2[ajfile[i]] = [(self.s_g(MM2[ajfile[i]][0],win,order,deriv)*tpx)/factdis,(self.s_g(MM2[ajfile[i]][1],win,order,deriv)*tpy)/factdis,MM2[ajfile[i]][2],MM2[ajfile[i]][3]]
                        
        #                MDEG1[ajfile[i]] = [(MM1[ajfile[i]][0]*tpx)/factdis,(MM1[ajfile[i]][1]*tpy)/factdis,MM1[ajfile[i]][2],MM1[ajfile[i]][3]]
        #                MDEG2[ajfile[i]] = [(MM2[ajfile[i]][0]*tpx)/factdis,(MM2[ajfile[i]][1]*tpy)/factdis,MM2[ajfile[i]][2],MM2[ajfile[i]][3]]

        def degtovel(self,sr):
                """
                Transformation des signaux de positions en degré en vitesse angulaire (smoothée)
                taux d'échantillonnage (samplerate) du live track = 500 Hz soit une durée de 2ms entre 2 points.
                sr = samplerate du recording
                """
                global MVEL1,MVEL2
                MVEL1 = {} ; MVEL2 = {} ; ufs = 1.0/float(sr)
                mvela,mvelb, mvelaa, mvelbb = [],[],[],[]
                for i in range (0,len(ajfile)):
                        if MDEG1[ajfile[i]][0] != []:        
                                a = MDEG1[ajfile[i]][0] 
                                b = MDEG1[ajfile[i]][1]
                                for k in range (0,len(a)-1):
                                        mvela.append((a[k+1]-a[k])/ufs)
                                        mvelb.append((b[k+1]-b[k])/ufs)
                        if MDEG2[ajfile[i]][0] != []:
                                aa = MDEG2[ajfile[i]][0]
                                bb = MDEG2[ajfile[i]][1]
                                for k in range (0,len(a)-1):
                                        mvelaa.append((aa[k+1]-aa[k])/ufs)
                                        mvelbb.append((bb[k+1]-bb[k])/ufs)
                        MVEL1[ajfile[i]] = [np.array(mvela),np.array(mvelb), MDEG1[ajfile[i]][2],MDEG1[ajfile[i]][3]]
                        MVEL2[ajfile[i]] = [np.array(mvelaa),np.array(mvelbb),MDEG2[ajfile[i]][2],MDEG2[ajfile[i]][3]]
                        ## Utilisation Sazvitzky Golay
        #                MVEL1[ajfile[i]] = [s_g(mvela,win,order,deriv),s_g(mvelb,win,order,deriv), MDEG1[ajfile[i]][2],MDEG1[ajfile[i]][3]]
        #                MVEL2[ajfile[i]] = [s_g(mvelaa,win,order,deriv),s_g(mvelbb,win,order,deriv),MDEG2[ajfile[i]][2],MDEG2[ajfile[i]][3]]
                        mvela,mvelb, mvelaa, mvelbb = [],[],[],[]
                        
        def veltoacc(self,sr):
                """
                Transformation des signaux de vitesse angulaire en accélération (smoothée)
                taux d'échantillonnage (samplerate) du live track = 500 Hz soit une durée de 2ms entre 2 points.
                sr = samplerate du recording
                """
                global MACC1,MACC2
                MACC1 = {} ; MACC2 = {} ; ufs = 1.0/float(sr)
                macca,maccb,maccaa,maccbb = [],[],[],[]
                for i in range (0,len(ajfile)):
                        a = MVEL1[ajfile[i]][0] ; b = MVEL1[ajfile[i]][1]
                        aa = MVEL2[ajfile[i]][0] ; bb=MVEL2[ajfile[i]][1]
                        for k in range (0,len(a)-1):
                                macca.append((a[k+1]-a[k])/ufs)
                                maccb.append((b[k+1]-b[k])/ufs)
                                maccaa.append((aa[k+1]-aa[k])/ufs)
                                maccbb.append((bb[k+1]-bb[k])/ufs)
                        MACC1[ajfile[i]] = [np.array(macca),np.array(maccb), MDEG1[ajfile[i]][2],MDEG1[ajfile[i]][3]]
                        MACC2[ajfile[i]] = [np.array(maccaa),np.array(maccbb),MDEG2[ajfile[i]][2],MDEG2[ajfile[i]][3]]
                        macca,maccb, maccaa, maccbb = [],[],[],[]
                        
                        
        def gnames(self):
                """ 
                renomme name file 
                """
                global names, spl,spl1, nam
                names=[] ; nam = []
                for i in range (0,len(ajfile)):
                        spl = ajfile[i].split('_') ## split le nom original
                        try:
                                int(spl[-1][0])
                                names.append(spl[0]+str("_")+spl[-2])
        #                if str(spl[-1][0]) == True:
                        except ValueError:
                                spl1 = spl[-1].split(".eos")
                                names.append(spl[0]+str("_")+spl1[0]) ## rebuild un nom cohérent
        #                        names.append(spl1[0]) ## rebuild un nom cohérent
                names.sort(key=self.natural_keys)
        
                for i in range (0,len(names)):
                        nam.append(names[i].split("_")[1])
                        
        def rectime(self,sr):
                """
                Pour chaque jeu remet ONSET à 0 Secondes """
                global CHUNK1, CHUNK2, CHUNK3
                CHUNK1 = {} ; CHUNK2 = {} ; CHUNK3 = {} ; ufs = 1.0/float(sr)
                for i in range(0,len(ajfile)):
                        a = np.arange(0,len(MDEG1[ajfile[i]][3]),1)
                        CHUNK1[ajfile[i]] = a*ufs
                
                
                for i in range(0,len(ajfile)):
                        aa = np.arange(0,len(MVEL1[ajfile[i]][3])-1,1)
                        CHUNK2[ajfile[i]] = aa*ufs
                        
                for i in range(0,len(ajfile)):
                        aa = np.arange(0,len(MACC1[ajfile[i]][3])-1,1)
                        CHUNK3[ajfile[i]] = aa*ufs
                
        
        
        
        def s_g(self,y, window_size, order, deriv=0, rate=1):
            r"""Smooth (and optionally differentiate) data with a Savitzky-Golay filter.
            The Savitzky-Golay filter removes high frequency noise from data.
            It has the advantage of preserving the original shape and
            features of the signal better than other types of filtering
            approaches, such as moving averages techniques.
            Parameters
            ----------
            y : array_like, shape (N,)
                the values of the time history of the signal.
            window_size : int
                the length of the window. Must be an odd integer number.
            order : int
                the order of the polynomial used in the filtering.
                Must be less then `window_size` - 1.
            deriv: int
                the order of the derivative to compute (default = 0 means only smoothing)
            Returns
            -------
            ys : ndarray, shape (N)
                the smoothed signal (or it's n-th derivative).
            Notes
            -----
            The Savitzky-Golay is a type of low-pass filter, particularly
            suited for smoothing noisy data. The main idea behind this
            approach is to make for each point a least-square fit with a
            polynomial of high order over a odd-sized window centered at
            the point.
            Examples
            --------
            t = np.linspace(-4, 4, 500)
            y = np.exp( -t**2 ) + np.random.normal(0, 0.05, t.shape)
            ysg = savitzky_golay(y, window_size=31, order=4)
            import matplotlib.pyplot as plt
            plt.plot(t, y, label='Noisy signal')
            plt.plot(t, np.exp(-t**2), 'k', lw=1.5, label='Original signal')
            plt.plot(t, ysg, 'r', label='Filtered signal')
            plt.legend()
            plt.show()
            References
            ----------
            .. [1] A. Savitzky, M. J. E. Golay, Smoothing and Differentiation of
               Data by Simplified Least Squares Procedures. Analytical
               Chemistry, 1964, 36 (8), pp 1627-1639.
            .. [2] Numerical Recipes 3rd Edition: The Art of Scientific Computing
               W.H. Press, S.A. Teukolsky, W.T. Vetterling, B.P. Flannery
               Cambridge University Press ISBN-13: 9780521880688
            """
            import numpy as np
            from math import factorial
        
            try:
                window_size = np.abs(np.int(window_size))
                order = np.abs(np.int(order))
            except ValueError:
                raise ValueError("window_size and order have to be of type int")
            if window_size % 2 != 1 or window_size < 1:
                raise TypeError("window_size size must be a positive odd number")
            if window_size < order + 2:
                raise TypeError("window_size is too small for the polynomials order")
            order_range = range(order+1)
            half_window = (window_size -1) // 2
            # precompute coefficients
            b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
            m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
            # pad the signal at the extremes with
            # values taken from the signal itself
            firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
            lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
            y = np.concatenate((firstvals, y, lastvals))
            return np.convolve( m[::-1], y, mode='valid')
    

        
#        def state_changed(self):
#                if self.checkBox8.isChecked():

        def createGridLayout(self):
            self.horizontalGroupBox = QGroupBox("Dimensions of Eye Data")
            layout = QGridLayout()
            
#            layout.setColumnStretch(1, 4)
#            layout.setColumnStretch(2, 4)
            layout.setColumnStretch(0, 1)
            layout.setColumnStretch(1, 1)
            layout.setColumnStretch(2, 1)
            layout.setColumnStretch(3, 1)
            layout.setColumnStretch(4, 1)
            layout.setColumnStretch(5, 1)
            layout.setColumnStretch(6, 1)
            layout.setColumnStretch(7, 1)
            layout.setColumnStretch(8, 1)
            layout.setColumnStretch(9, 1)
            layout.setColumnStretch(10, 1)
            layout.setColumnStretch(11, 1)
            layout.setColumnStretch(12, 1)
            layout.setColumnStretch(13, 1)
            
#            layout.setRowStretch()

        ############################################
        ## Bouttons de visu, à connecter avec les différentes tables (raw, degree, velocity, acceleration)
        ############################################
# =============================================================================
            self.pushButton5 = QtWidgets.QPushButton(self)
            self.pushButton5.setGeometry(QtCore.QRect(200,0,0,0))
#            self.pushButton3.setGeometry(200,10,25,50)
            self.pushButton5.setObjectName("Raw-Pixel")
            self.pushButton5.setText("Raw-Pixel")
#            self.pushButton5.setCheckable(True)
#            self.pushButton5.clicked.connect(self.plot_pxl)
            self.pushButton5.clicked.connect(self.fill_combo_pxl)
#            self.pushButton5.clicked.connect(self.plot_pxl)
            
 
            self.pushButton6 = QtWidgets.QPushButton('Raw-Degree',self)
            self.pushButton6.setGeometry(QtCore.QRect(200,0,0,0))
#            self.pushButton4.setGeometry(200,30,25,50)
            self.pushButton6.setObjectName("Raw-Degree")
            self.pushButton6.setText("Raw-Degree")
#            self.pushButton6.setCheckable(True)
#            self.pushButton6.clicked.connect(self.plot_deg)
            self.pushButton6.clicked.connect(self.fill_combo_deg)
#            self.pushButton6.clicked.connect(self.plot_deg)
     
            self.pushButton7 = QtWidgets.QPushButton(self)
            self.pushButton7.setGeometry(QtCore.QRect(200,0,0,0))
#            self.pushButton5.setGeometry(200,50,25,50)
            self.pushButton7.setObjectName("Velocity")
            self.pushButton7.setText("Velocity")
#            self.pushButton7.setCheckable(True)
            self.pushButton7.clicked.connect(self.fill_combo_vel)
#            self.pushButton7.clicked.connect(self.plot_vel)
 
            self.pushButton8 = QtWidgets.QPushButton('Acceleration',self)
            self.pushButton8.setGeometry(QtCore.QRect(200,0,0,0))
#            self.pushButton6.setGeometry(200,70,25,50)
            self.pushButton8.setObjectName("Acceleration")
            self.pushButton8.setText("Acceleration")
#            self.pushButton8.setCheckable(True)
            self.pushButton8.clicked.connect(self.fill_combo_acc)
#            self.pushButton8.clicked.connect(self.plot_acc)
        #         
        # =============================================================================
        ############################################
        # Boite à cocher pour séléctionner la dimension que l'on veut afficher 
        # oeil 1 X, Y, la pupille (idem pour oeil 2)
        ############################################        
            self.checkBox8 = QtWidgets.QCheckBox(self)
            self.checkBox8.setGeometry(QtCore.QRect(200, 0, 0, 0))
            self.checkBox8.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.checkBox8.setText("Left Eye X")
            self.checkBox8.setCheckable(True)
            self.checkBox8.setObjectName("Left Eye X")
            self.checkBox8.stateChanged.connect(self.plot_pxl)
#            self.checkBox8.stateChanged.connect(self.plot_deg)
            
            
            self.checkBox9 = QtWidgets.QCheckBox(self)
            self.checkBox9.setGeometry(QtCore.QRect(200, 0, 0, 0))
            self.checkBox9.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.checkBox9.setText("Left Eye Y")
            self.checkBox9.setCheckable(True)
            self.checkBox9.setObjectName("Left Eye Y")
            self.checkBox9.stateChanged.connect(self.plot_pxl)
#            self.checkBox9.stateChanged.connect(self.plot_deg)
            
            self.checkBox10 = QtWidgets.QCheckBox(self)
            self.checkBox10.setGeometry(QtCore.QRect(200, 0, 0, 0))
            self.checkBox10.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.checkBox10.setText("Left Eye Pupil")
            self.checkBox10.setCheckable(True)
            self.checkBox10.setObjectName("Left Eye Pupil")
            self.checkBox10.stateChanged.connect(self.plot_pxl)
#            self.checkBox10.stateChanged.connect(self.plot_deg)
            
            self.checkBox11 = QtWidgets.QCheckBox(self)
            self.checkBox11.setGeometry(QtCore.QRect(200, 0, 0, 0))
            self.checkBox11.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.checkBox11.setText("Right Eye X")
            self.checkBox11.setCheckable(True)
            self.checkBox11.setObjectName("Right Eye X")
            self.checkBox11.stateChanged.connect(self.plot_pxl)
#            self.checkBox11.stateChanged.connect(self.plot_deg)
            
            self.checkBox12 = QtWidgets.QCheckBox(self)
            self.checkBox12.setGeometry(QtCore.QRect(200, 0, 0, 0))
            self.checkBox12.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.checkBox12.setText("Right Eye Y")
            self.checkBox12.setCheckable(True)
            self.checkBox12.setObjectName("Right Eye Y")
            self.checkBox12.stateChanged.connect(self.plot_pxl)
#            self.checkBox12.stateChanged.connect(self.plot_deg)
            
            self.checkBox13 = QtWidgets.QCheckBox(self)
            self.checkBox13.setGeometry(QtCore.QRect(200, 0, 0, 0))
            self.checkBox13.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.checkBox13.setText("Right Eye Pupil")
            self.checkBox13.setCheckable(True)
            self.checkBox13.setObjectName("Right Eye Pupil")
            self.checkBox13.stateChanged.connect(self.plot_pxl)
#            self.checkBox13.stateChanged.connect(self.plot_deg)
# =============================================================================
#             Bouttons liés aux opérationx méta : Load, Save, Clear, Close
# =============================================================================
            self.pushButton1 = QtWidgets.QPushButton(self)
            self.pushButton1.setGeometry(QtCore.QRect(200,0,0,0))
            self.pushButton1.setObjectName("Load_Files")
            self.pushButton1.setText("Load_Files")
            self.pushButton1.clicked.connect(self.loadrawData)
                        
            self.pushButton2 = QtWidgets.QPushButton(self)
            self.pushButton2.setGeometry(QtCore.QRect(200,0,0,0))
            self.pushButton2.setObjectName("Save_Plot")
            self.pushButton2.setText("Save_Plot")
            self.pushButton2.clicked.connect(self.plot_save)
            
            self.pushButton3 = QtWidgets.QPushButton(self)
            self.pushButton3.setGeometry(QtCore.QRect(200,0,0,0))
            self.pushButton3.setObjectName("Clear_Plot")
            self.pushButton3.setText("Clear_Plot")
            self.pushButton3.clicked.connect(self.plot_clear)
            
            self.pushButton4 = QtWidgets.QPushButton('Close',self)
            self.pushButton4.setGeometry(QtCore.QRect(200,0,0,0))
            self.pushButton4.setObjectName("Close")
            self.pushButton4.setText("Close")
            self.pushButton4.clicked.connect(self.close)
            
            
            self.gamelist = QtWidgets.QComboBox(self)
            self.gamelist.setGeometry(QtCore.QRect(200,0,0,0))
            self.gamelist.setObjectName("games")
            
            
#            self.gamelist.activated.connect()
            
            
        
        
            layout.addWidget(self.pushButton5,0,8) ## button raw pixel data
            layout.addWidget(self.pushButton6,1,8) ## button raw degree data
            layout.addWidget(self.pushButton7,2,8) ## button velocity data
            layout.addWidget(self.pushButton8,3,8) ## button acceleration data
            layout.addWidget(self.gamelist,0,9)
            
            layout.addWidget(self.checkBox8,0,10)
            layout.addWidget(self.checkBox9,1,10)
            layout.addWidget(self.checkBox10,2,10) 
            layout.addWidget(self.checkBox11,0,11) 
            layout.addWidget(self.checkBox12,1,11) 
            layout.addWidget(self.checkBox13,2,11) 
            layout.addWidget(self.pushButton1,0,0)
            layout.addWidget(self.pushButton4,3,0)
            layout.addWidget(self.pushButton2,2,0)
            layout.addWidget(self.pushButton3,1,0)
             
            
            self.horizontalGroupBox.setLayout(layout)
 
#if __name__ == '__main__':
def run():
    app = QApplication(sys.argv)
    main = Ui_Dialog()
    main.show()
    sys.exit(app.exec_())