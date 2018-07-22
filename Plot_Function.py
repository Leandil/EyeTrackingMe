# -*- coding: utf-8 -*-
"""
Created on Sun May 27 13:13:11 2018

@author: Léo
"""
## RAW pixel
def games_plot():
        import time
        n=list(minfos.keys())
#        plt.figure(figsize = (24,10),dpi=100)
        for j in range (0,len(n)):
                plt.figure(figsize = (24,10),dpi=100)
                k = 0 ; m=0.1 ;
                listg = list(game["%s"%(n[j])].keys())
                namenu = ["LASujet %s \n"%(n[j]) + "\n" + minfos["%s"%(n[j])]["DATE"] + "\n" + minfos["%s"%(n[j])]["INFLAB"][0] + "\n" + minfos["%s"%(n[j])]["NAME_ORIGINAL"][0]+"\n"]
                for i in range (0,len(listg)):
                        namenu.append("Game %s %s: "%(i+1,listg[i])+ ' \n')   
                nmenu = ''.join(namenu)
                for i in range (0,len(game["%s"%(n[j])])):
                    textstr = " Game %s"%(i+1)
                    plt.subplot(6,7,k+1)    
                    plt.scatter(game["%s"%(n[j])]["%s"%(listg[i])]["X1"],game["%s"%(n[j])]["%s"%(listg[i])]["Y1"],s=1,color="b", marker='o',alpha =.2,lw=0)
                    plt.scatter(game["%s"%(n[j])]["%s"%(listg[i])]["X2"],game["%s"%(n[j])]["%s"%(listg[i])]["Y2"],s=1,color="r", marker='o',alpha =.2,lw=0)
                    plt.text(400,-50,textstr,fontweight ='bold')
                    plt.xlim(0,1024)
                    plt.ylim(768,0)
                    plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.0450, right=0.945,wspace = 0.220, hspace=0.420)
                    k+=1;m+=5
                #plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.125, right=0.75,wspace = 0.220, hspace=0.355)
#                plt.text(2750,-1000,nmenu, ha = "right", va="center",fontsize=14)
                #plt.annotate(str(namenu), xy = (6500,-3000),xytext=(6500,-3000))
                plt.subplot(6,7,k+1)
                plt.xticks([])
                plt.yticks([])
                line1 = linspace(5,5,5)
                line2 = linspace(10,10,5)
                plt.plot(line1, color = "blue",alpha = .4,marker = "o", lw = 0)
                plt.plot(line2, color = "red", alpha = .4,marker = "o", lw = 0)
                plt.xlabel("Eye on x in pixels",fontweight = "bold")
                plt.ylabel("Eye on y in pixels",fontweight = "bold")
                plt.text(1.5,6,"Left Eye")
                plt.text(1.5,9,"Righ Eye")
                manager = plt.get_current_fig_manager()
                manager.window.showMaximized()
                time.sleep(2)
                plt.savefig("Graphs\\G_EL_%s_%s"%(n[j],minfos["%s"%(n[j])]["INFLAB"][1]), dpi=100, facecolor='w', edgecolor='w',orientation='landscape')
                text_file = open("Graphs\\Game_EL_%s.txt"%(n[j]), "w")
                text_file.write(nmenu)
                text_file.close()

## RAW deg                
def games_plot_deg():
        import time
        n=list(minfos.keys())
#        plt.figure(figsize = (24,10),dpi=100)
        for j in range (0,len(n)):
                plt.figure(figsize = (24,10),dpi=100)
                k = 0 ; m=0.1 ;
                listg = list(game["%s"%(n[j])].keys())
                namenu = ["LASujet %s \n"%(n[j]) + "\n" + minfos["%s"%(n[j])]["DATE"] + "\n" + minfos["%s"%(n[j])]["INFLAB"][0] + "\n" + minfos["%s"%(n[j])]["NAME_ORIGINAL"][0]+"\n"]
                for i in range (0,len(listg)):
                        namenu.append("Game %s: "%(i+1) + listg[i]+ ' \n')   
                nmenu = ''.join(namenu)
                for i in range (0,len(game["%s"%(n[j])])):
                    textstr = " Game %s"%(i+1)
                    plt.subplot(6,7,k+1)    
                    plt.scatter(dgame["%s"%(n[j])]["%s"%(listg[i])]["X1"],dgame["%s"%(n[j])]["%s"%(listg[i])]["Y1"],s=1,color="b", marker='o',alpha =.2,lw=0)
                    plt.scatter(dgame["%s"%(n[j])]["%s"%(listg[i])]["X2"],dgame["%s"%(n[j])]["%s"%(listg[i])]["Y2"],s=1,color="r", marker='o',alpha =.2,lw=0)
                    plt.text(30,65,textstr,fontweight ='bold')
                    plt.xlim(0,75.75) ## ecran ICM donne 82.92 degré horizontal
                    plt.ylim(41.63,0) ## ecran ICM donne 47.77 degrés en vertical à 80 cm
                    plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.0450, right=0.945,wspace = 0.220, hspace=0.420)
                    k+=1;m+=5
                #plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.125, right=0.75,wspace = 0.220, hspace=0.355)
#                plt.text(2750,-1000,nmenu, ha = "right", va="center",fontsize=14)
                #plt.annotate(str(namenu), xy = (6500,-3000),xytext=(6500,-3000))
                plt.subplot(6,7,k+1)
                plt.xticks([])
                plt.yticks([])
                line1 = linspace(5,5,5)
                line2 = linspace(10,10,5)
                plt.plot(line1, color = "blue",alpha = .4,marker = "o", lw = 0)
                plt.plot(line2, color = "red", alpha = .4,marker = "o", lw = 0)
                plt.xlabel("Eye on x in degres",fontweight = "bold")
                plt.ylabel("Eye on y in degres",fontweight = "bold")
                plt.text(1.5,6,"Left Eye")
                plt.text(1.5,9,"Righ Eye")
                manager = plt.get_current_fig_manager()
                manager.window.showMaximized()
                time.sleep(2)
                plt.savefig("Graphs\\DG_EL_%s_%s"%(n[j],minfos["%s"%(n[j])]["INFLAB"][1]), dpi=100, facecolor='w', edgecolor='w',orientation='landscape')
                text_file = open("Graphs\\dGame_EL_%s.txt"%(n[j]), "w")
                text_file.write(nmenu)
                text_file.close()
                
## PLOT TO CHECK REMOVE BLINK PROCEDURE
#On position
def check(i,j):
        k1 = i ; k2 = j
        n=list(minfos.keys())
        l=list(game["%s"%(n[k1])].keys())
        plt.figure(figsize = (24,10),dpi=100)
        plt.suptitle("Removal Blink Procedure - %s - Game %s"%(n[k1],l[k2]))
        ax1 = plt.subplot(321)
        ax1.plot(game["%s"%(n[k1])]["%s"%(l[k2])]["TS"],game["%s"%(n[k1])]["%s"%(l[k2])]["X1"],color = "black")
        ax1.plot(game1["%s"%(n[k1])]["%s"%(l[k2])]["TS"],game1["%s"%(n[k1])]["%s"%(l[k2])]["X1"],color = "red")
        ax1.set_ylabel("Position on X axis - pxl")
        ax1.set_title("EYE 1")
        
        ax2 = plt.subplot(323)
        ax2.plot(game["%s"%(n[k1])]["%s"%(l[k2])]["TS"],game["%s"%(n[k1])]["%s"%(l[k2])]["Y1"],color = "black")
        ax2.plot(game1["%s"%(n[k1])]["%s"%(l[k2])]["TS"],game1["%s"%(n[k1])]["%s"%(l[k2])]["Y1"],color = "red")
        ax2.set_ylabel("Position on Y axis - pxl")
        
        ax3 = plt.subplot(325)
        ax3.plot(game["%s"%(n[k1])]["%s"%(l[k2])]["TS"],game["%s"%(n[k1])]["%s"%(l[k2])]["PUP1"],color = "black")
        ax3.plot(game1["%s"%(n[k1])]["%s"%(l[k2])]["TS"],game1["%s"%(n[k1])]["%s"%(l[k2])]["PUP1"],color = "red")
        ax3.set_ylabel("Pupil")
        ax3.set_xlabel("Time - sec")
        ax3.legend(["W_Blink","Wo_Blink"])
        
        ax4 = plt.subplot(322)
        ax4.plot(game["%s"%(n[k1])]["%s"%(l[k2])]["TS"],game["%s"%(n[k1])]["%s"%(l[k2])]["X2"],color = "black")
        ax4.plot(game1["%s"%(n[k1])]["%s"%(l[k2])]["TS"],game1["%s"%(n[k1])]["%s"%(l[k2])]["X2"],color = "red")
        ax4.set_ylabel("Position on X axis  - pxl")
        ax4.set_title("EYE 2")
        
        ax5 = plt.subplot(324)
        ax5.plot(game["%s"%(n[k1])]["%s"%(l[k2])]["TS"],game["%s"%(n[k1])]["%s"%(l[k2])]["Y2"],color = "black")
        ax5.plot(game1["%s"%(n[k1])]["%s"%(l[k2])]["TS"],game1["%s"%(n[k1])]["%s"%(l[k2])]["Y2"],color = "red")
        ax5.set_ylabel("Position on Y axis - pxl")
        
        ax6 = plt.subplot(326)
        ax6.plot(game["%s"%(n[k1])]["%s"%(l[k2])]["TS"],game["%s"%(n[k1])]["%s"%(l[k2])]["PUP2"],color = "black")
        ax6.plot(game1["%s"%(n[k1])]["%s"%(l[k2])]["TS"],game1["%s"%(n[k1])]["%s"%(l[k2])]["PUP2"],color = "red")
        ax6.set_ylabel("Pupil")
        ax6.set_xlabel("Time - sec")
        ax6.legend("W_Blink","Wo_Blink")
        
        plt.savefig("Graphs\\Pos_BlinkCheck_%s_%s"%(n[k1],l[k2]), dpi=100, facecolor='w', edgecolor='w',orientation='landscape')

#On velocity
def check_vel(i,j):
        k1 = i ; k2 = j
        n=list(minfos.keys())
        l=list(vgame["%s"%(n[k1])].keys())
        plt.figure(figsize = (24,10),dpi=100)
        plt.suptitle("Removal Blink Procedure - %s - Game %s"%(n[k1],l[k2]))
        ax1 = plt.subplot(321)
        ax1.plot(vgame["%s"%(n[k1])]["%s"%(l[k2])]["TS"],vgame["%s"%(n[k1])]["%s"%(l[k2])]["X1"],color = "black")
        ax1.plot(vgame1["%s"%(n[k1])]["%s"%(l[k2])]["TS"],vgame1["%s"%(n[k1])]["%s"%(l[k2])]["X1"],color = "red")
        ax1.set_ylabel("Veolicty on X axis - pxl")
        ax1.set_title("EYE 1")
        
        ax2 = plt.subplot(323)
        ax2.plot(vgame["%s"%(n[k1])]["%s"%(l[k2])]["TS"],vgame["%s"%(n[k1])]["%s"%(l[k2])]["Y1"],color = "black")
        ax2.plot(vgame1["%s"%(n[k1])]["%s"%(l[k2])]["TS"],vgame1["%s"%(n[k1])]["%s"%(l[k2])]["Y1"],color = "red")
        ax2.set_ylabel("Velocity on Y axis - pxl")
        
        ax3 = plt.subplot(325)
        ax3.plot(vgame["%s"%(n[k1])]["%s"%(l[k2])]["TS"],vgame["%s"%(n[k1])]["%s"%(l[k2])]["PUP1"][0:-1],color = "black")
        ax3.plot(vgame1["%s"%(n[k1])]["%s"%(l[k2])]["TS"],vgame1["%s"%(n[k1])]["%s"%(l[k2])]["PUP1"][0:-1],color = "red")
        ax3.set_ylabel("Pupil")
        ax3.set_xlabel("Time - sec")
        ax3.legend(["W_Blink","Wo_Blink"])
        
        ax4 = plt.subplot(322)
        ax4.plot(vgame["%s"%(n[k1])]["%s"%(l[k2])]["TS"],vgame["%s"%(n[k1])]["%s"%(l[k2])]["X2"],color = "black")
        ax4.plot(vgame1["%s"%(n[k1])]["%s"%(l[k2])]["TS"],vgame1["%s"%(n[k1])]["%s"%(l[k2])]["X2"],color = "red")
        ax4.set_ylabel("Velocity on X axis  - pxl")
        ax4.set_title("EYE 2")
        
        ax5 = plt.subplot(324)
        ax5.plot(vgame["%s"%(n[k1])]["%s"%(l[k2])]["TS"],vgame["%s"%(n[k1])]["%s"%(l[k2])]["Y2"],color = "black")
        ax5.plot(vgame1["%s"%(n[k1])]["%s"%(l[k2])]["TS"],vgame1["%s"%(n[k1])]["%s"%(l[k2])]["Y2"],color = "red")
        ax5.set_ylabel("Velocity on Y axis - pxl")
        
        ax6 = plt.subplot(326)
        ax6.plot(vgame["%s"%(n[k1])]["%s"%(l[k2])]["TS"],vgame["%s"%(n[k1])]["%s"%(l[k2])]["PUP2"][0:-1],color = "black")
        ax6.plot(vgame1["%s"%(n[k1])]["%s"%(l[k2])]["TS"],vgame1["%s"%(n[k1])]["%s"%(l[k2])]["PUP2"][0:-1],color = "red")
        ax6.set_ylabel("Pupil")
        ax6.set_xlabel("Time - sec")
        ax6.legend("W_Blink","Wo_Blink")
        
        plt.savefig("Graphs\\Vel_BlinkCheck_%s_%s"%(n[k1],l[k2]), dpi=100, facecolor='w', edgecolor='w',orientation='landscape')

## Velocity deg
def games_plot_vel():
        import time
        n=list(minfos.keys())
#        plt.figure(figsize = (24,10),dpi=100)
        for j in range (0,len(n)):
                plt.figure(figsize = (24,10),dpi=100)
                k = 0 ; m=0.1 ;
                listg = list(game["%s"%(n[j])].keys())
                namenu = ["LASujet %s \n"%(n[j]) + "\n" + minfos["%s"%(n[j])]["DATE"] + "\n" + minfos["%s"%(n[j])]["INFLAB"][0] + "\n" + minfos["%s"%(n[j])]["NAME_ORIGINAL"][0]+"\n"]
                for i in range (0,len(listg)):
                        namenu.append("Game %s: "%(i+1) + listg[i]+ ' \n')   
                nmenu = ''.join(namenu)
                for i in range (0,len(game["%s"%(n[j])])):
                    textstr = " Game %s"%(i+1)
                    plt.subplot(6,7,k+1)    
                    plt.plot(vgame["%s"%(n[j])]["%s"%(listg[i])]["TS"],vgame["%s"%(n[j])]["%s"%(listg[i])]["X1"],color="purple", alpha =.5,lw=1)
                    plt.plot(vgame["%s"%(n[j])]["%s"%(listg[i])]["TS"],vgame["%s"%(n[j])]["%s"%(listg[i])]["Y1"],color ="green",alpha =.5,lw=1)
                    plt.text(mean(vgame["%s"%(n[j])]["%s"%(listg[i])]["TS"]),-820,textstr,fontweight ='bold')
#                    plt.xlim(0,75.75) ## ecran ICM donne 82.92 degré horizontal
                    plt.ylim(-500,500) ## ecran ICM donne 47.77 degrés en vertical à 80 cm
                    plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.0450, right=0.945,wspace = 0.220, hspace=0.420)
                    k+=1;m+=5
                #plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.125, right=0.75,wspace = 0.220, hspace=0.355)
#                plt.text(2750,-1000,nmenu, ha = "right", va="center",fontsize=14)
                #plt.annotate(str(namenu), xy = (6500,-3000),xytext=(6500,-3000))
                plt.subplot(6,7,k+1)
                plt.xticks([])
                plt.yticks([])
                line1 = linspace(5,5,5)
                line2 = linspace(10,10,5)
                plt.plot(line1, color = "purple",alpha = .4,marker = "o", lw = 0)
                plt.plot(line2, color = "green", alpha = .4,marker = "o", lw = 0)
                plt.xlabel("Time - Sec",fontweight = "bold")
                plt.ylabel("Velocity of the Left Eye \n °/s",fontweight = "bold",fontsize = 8)
                plt.text(1.5,6,"Eye on X")
                plt.text(1.5,9,"Eye on Y")
                manager = plt.get_current_fig_manager()
                manager.window.showMaximized()
                time.sleep(2)
                plt.savefig("Graphs\\vgame_EL_%s"%(n[j]), dpi=100, facecolor='w', edgecolor='w',orientation='landscape')
                text_file = open("Graphs\\vGame_EL_%s.txt"%(n[j]), "w")
                text_file.write(nmenu)
                text_file.close()
                
## Velocity deg
def games_plot_acc():
        import time
        n=list(minfos.keys())
#        plt.figure(figsize = (24,10),dpi=100)
        for j in range (0,len(n)):
                plt.figure(figsize = (24,10),dpi=100)
                k = 0 ; m=0.1 ;
                listg = list(game["%s"%(n[j])].keys())
                namenu = ["LASujet %s \n"%(n[j]) + "\n" + minfos["%s"%(n[j])]["DATE"] + "\n" + minfos["%s"%(n[j])]["INFLAB"][0] + "\n" + minfos["%s"%(n[j])]["NAME_ORIGINAL"][0]+"\n"]
                for i in range (0,len(listg)):
                        namenu.append("Game %s: "%(i+1) + listg[i]+ ' \n')   
                nmenu = ''.join(namenu)
                for i in range (0,len(game["%s"%(n[j])])):
                    textstr = " Game %s"%(i+1)
                    plt.subplot(6,7,k+1)    
                    plt.plot(agame["%s"%(n[j])]["%s"%(listg[i])]["TS"][0:-1],agame["%s"%(n[j])]["%s"%(listg[i])]["X1"],color="purple", alpha =.5,lw=1)
                    plt.plot(agame["%s"%(n[j])]["%s"%(listg[i])]["TS"][0:-1],agame["%s"%(n[j])]["%s"%(listg[i])]["Y1"],color ="green",alpha =.5,lw=1)
                    plt.text(mean(vgame["%s"%(n[j])]["%s"%(listg[i])]["TS"]),-13000,textstr,fontweight ='bold')
#                    plt.xlim(0,75.75) ## ecran ICM donne 82.92 degré horizontal
                    plt.ylim(-8000,8000) ## ecran ICM donne 47.77 degrés en vertical à 80 cm
                    plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.0450, right=0.945,wspace = 0.275, hspace=0.420)
                    k+=1;m+=5
                #plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.125, right=0.75,wspace = 0.220, hspace=0.355)
#                plt.text(2750,-1000,nmenu, ha = "right", va="center",fontsize=14)
                #plt.annotate(str(namenu), xy = (6500,-3000),xytext=(6500,-3000))
                plt.subplot(6,7,k+1)
                plt.xticks([])
                plt.yticks([])
                line1 = linspace(5,5,5)
                line2 = linspace(10,10,5)
                plt.plot(line1, color = "purple",alpha = .4,marker = "o", lw = 0)
                plt.plot(line2, color = "green", alpha = .4,marker = "o", lw = 0)
                plt.xlabel("Time - Sec",fontweight = "bold")
                plt.ylabel("Acceleration of the Left Eye \n °/s²",fontweight = "bold",fontsize = 8)
                plt.text(1.5,6,"Eye on X")
                plt.text(1.5,9,"Eye on Y")
                manager = plt.get_current_fig_manager()
                manager.window.showMaximized()
                time.sleep(2)
                plt.savefig("Graphs\\agame_EL_%s"%(n[j]), dpi=100, facecolor='w', edgecolor='w',orientation='landscape')
                text_file = open("Graphs\\aGame_EL_%s.txt"%(n[j]), "w")
                text_file.write(nmenu)
                text_file.close()




# =============================================================================
# ## DEBLINKE              
# =============================================================================
## Blink removed XY plot
def games_plot1():
        import time
        n=list(minfos.keys())
#        plt.figure(figsize = (24,10),dpi=100)
        for j in range (0,len(n)):
                plt.figure(figsize = (24,10),dpi=100)
                k = 0 ; m=0.1 ;
                listg = list(game["%s"%(n[j])].keys())
                namenu = ["LASujet %s \n"%(n[j]) + "\n" + minfos["%s"%(n[j])]["DATE"] + "\n" + minfos["%s"%(n[j])]["INFLAB"][0] + "\n" + minfos["%s"%(n[j])]["NAME_ORIGINAL"][0]+"\n"]
                for i in range (0,len(listg)):
                        namenu.append("Game %s: "%(i+1) + listg[i]+ ' \n')   
                nmenu = ''.join(namenu)
                for i in range (0,len(game["%s"%(n[j])])):
                    textstr = " Game %s"%(i+1)
                    plt.subplot(6,7,k+1)    
                    plt.scatter(game1["%s"%(n[j])]["%s"%(listg[i])]["X1"],game["%s"%(n[j])]["%s"%(listg[i])]["Y1"],s=1,color="b", marker='o',alpha =.2,lw=0)
                    plt.scatter(game1["%s"%(n[j])]["%s"%(listg[i])]["X2"],game["%s"%(n[j])]["%s"%(listg[i])]["Y2"],s=1,color="r", marker='o',alpha =.2,lw=0)
                    plt.text(400,-50,textstr,fontweight ='bold')
                    plt.xlim(0,1024)
                    plt.ylim(768,0)
                    plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.0450, right=0.945,wspace = 0.220, hspace=0.420)
                    k+=1;m+=5
                #plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.125, right=0.75,wspace = 0.220, hspace=0.355)
#                plt.text(2750,-1000,nmenu, ha = "right", va="center",fontsize=14)
                #plt.annotate(str(namenu), xy = (6500,-3000),xytext=(6500,-3000))
                plt.subplot(6,7,k+1)
                plt.xticks([])
                plt.yticks([])
                line1 = linspace(5,5,5)
                line2 = linspace(10,10,5)
                plt.plot(line1, color = "blue",alpha = .4,marker = "o", lw = 0)
                plt.plot(line2, color = "red", alpha = .4,marker = "o", lw = 0)
                plt.xlabel("Eye on x in pixels",fontweight = "bold")
                plt.ylabel("Eye on y in pixels",fontweight = "bold")
                plt.text(1.5,6,"Left Eye")
                plt.text(1.5,9,"Righ Eye")
                manager = plt.get_current_fig_manager()
                manager.window.showMaximized()
                time.sleep(2)
                plt.savefig("Graphs\\game1_EL_%s"%(n[j]), dpi=100, facecolor='w', edgecolor='w',orientation='landscape')
                text_file = open("Graphs\\Game1_EL_%s.txt"%(n[j]), "w")
                text_file.write(nmenu)
                text_file.close()
                
                
## Blink removed signal for pupil 
def eyesigblk():
        import time
        n=list(minfos.keys())
#        plt.figure(figsize = (24,10),dpi=100)
        for j in range (0,len(n)):
                listg=list(game1["%s"%(n[j])].keys())
                for i in range (0,len(listg)):
                        plt.figure(figsize = (24,10),dpi=100) ## X positions
                        plt.plot(game1["%s"%(n[j])]["%s"%(listg[i])]["X1"], lw = 2.0, color = "darkorange")
                        plt.plot(game1["%s"%(n[j])]["%s"%(listg[i])]["X2"], lw = 2.0, color = "firebrick")
                        plt.figure(figsize = (24,10),dpi=100) ## Y positions
                        plt.plot(game1["%s"%(n[j])]["%s"%(listg[i])]["Y1"], lw = 2.0, color = "darkorange")
                        plt.plot(game1["%s"%(n[j])]["%s"%(listg[i])]["Y2"], lw = 2.0, color = "firebrick")
                        plt.figure(figsize = (24,10),dpi=100) ## pupille dynamics
                        plt.plot(game1["%s"%(n[j])]["%s"%(listg[i])]["PUP1"], lw = 2.0,color = "darkorange")
                        plt.plot(game1["%s"%(n[j])]["%s"%(listg[i])]["PUP2"], lw = 2.0,color = "firebrick")
                        
#                        
### Tentative plot avec dataframe
def dfplot():
        import seaborn as sns
        sns.set(style="ticks")
        g=sns.countplot(x="Sujet",hue="N_Blinks",data=data1)
        g.set_xticklabels(g.get_xticklabels(),rotation = 45)                
        plt .figure()
        plt.subplot(411)
        bl = sns.barplot(x = "Game", y = "N_Blinks", data=data1)
        bl.set_xticklabels([])
        plt.subplot(412)
        al = sns.barplot(x = "Game", y = "Duration_Total_Blk - Seconde", data=data1)
        al.set_xticklabels([])
        al.set_ylabel("Duration_Total_Blk - sec")
        plt.subplot(413)
        cl = sns.barplot(x = "Game", y = "blink_minute", data=data1)
        cl.set_xticklabels([]) 
        cl.set_ylabel("NBlinks/min")
        plt.subplot(414)
        cl = sns.barplot(x = "Game", y = "Ratio_DurBlk_DurJeu", data=data1)
        cl.set_xticklabels(bl.get_xticklabels(),rotation = 45) 
        cl.set_ylabel("Ratio")


def dynplot(ns,name,name1,name2):
        import pyqtgraph as pg
        import pyqtgraph.exporters
        import numpy as np
        
        # define the data
        theTitle = "pyqtgraph plot"
        y = game["S%s"%(ns)]["%s"%(name)]["%s"%(name1)]
        y2 = game["S%s"%(ns)]["%s"%(name)]["%s"%(name2)]
        x = range(0,len(y))
        
        # create plot
        plt = pg.plot()
        plt.showGrid(x=True,y=True)
        plt.addLegend()
        
        # set properties
        if (name1 == "X1"):
                plt.setLabel('left', 'EyePosition', units='pxl')
        elif (name1 == "PUP1"):
                plt.setLabel('left', 'PupDynamic', units='-')
        plt.setLabel('bottom', 'Time', units='sec')
        plt.setXRange(0,len(y))
        plt.setYRange(0,max(y))
        plt.setWindowTitle('pyqtgraph plot')
        
        # plot
        c1 = plt.plot(x, y, pen='b', symbol='x', symbolPen='b', symbolBrush=0.2, name='blue')
        c2 = plt.plot(x, y2, pen='m', symbol='o', symbolPen='r', symbolBrush=0.2, name='magenta')
        
        ## Start Qt event loop.
        if __name__ == '__main__':
            import sys
            if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
                pg.QtGui.QApplication.exec_()
