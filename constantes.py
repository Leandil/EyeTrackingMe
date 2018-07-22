# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 09:41:53 2018
EYELINK
@author: A.P
"""


## ensemble des variables utilisées
m =[0,1,3,5,7] ## numéro des labos dont on a des données 

## num sujets en fonction de m
#si m=0
n0 = [3,4,5,6,7,8,9]
#si m=1
n1 = [1,2,3,4,5,6,7,8,9]
#si m=3
n3 = [1,2,3,4,5]
#si m = 5
n5 = [10]
#si m = 7
n7 = [6,7,8,9]
#variables uniques specifiques
s1000 = 0 ## indice de base de recodage des sujets

# =============================================================================
# ## convpixtodeg(dis,c,win,order,deriv) : fonction qui convertit les positions pixels en degrés
# =============================================================================
dis = 57 ##• distance oeil - screen
c = 2 ## setup pris en compte (taille d'écran, donc pixel)
win = 29 ## taille de la fenetre de filtrage du filtre savitzky & Golay
order = 0 ## ordre du filtre
deriv = 0 ## dérivée du filtre

# =============================================================================
# ## degtovel(sr) fonction qui dérive les positions degrés en vitesse
# =============================================================================
# =============================================================================
# ## veltoacc(sr) fonction qui dérive la vitesse en accélération
# =============================================================================
# =============================================================================
# ## rectime(sr) fonction qui transforme les timestamps de l'eyetracker en seconde
# =============================================================================
sr = 500 ## sample rate de l'EyeTracker


# =============================================================================
# ## nbloss(meth,wind,sep) fonction qui récupère les indexs des pertes de signal afin de les déterminer comme blinks, en découpant selon un fenetrage choisi (nb de points) et une séparation minimum ou maximum entre les détections
# =============================================================================
## deux méthodes possibles : considérer toutes les pertes de signal comme des potentiels blinks, ou seulement les pertes de signal conjuguées aux deux yeux sur l'AXE Y
meth = 0 #or 1 ## 0 --> uniquement les pertes communes aux deux yeux // 1 --> toutes les pertes de signal
wind = 60 ## à 500 Hz cela équivaut à 120 ms de chaque côté
sep = 50 ## à 500 Hz cela équivaut à 100 de séparation minimum entre deux blinks 

# =============================================================================
# ## recode() fonction qui remplace toutes les pertes de signal détectées selon méthode et fenêtrage. 
# =============================================================================

# =============================================================================
# ## blink_count(dmin) fonction qui compte le nombre de blink par jeu par sujet avec une durée de blink minimum
# =============================================================================
dmin = 100 ## durée minimum d'un blink, à 500 Hz cela correspond à 200 ms (avec fenêtrage)