# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:30:02 2018

@author: A.P
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:56:37 2017

@author: A.P
"""



import os; import sys 
import csv;from os import chdir;from pylab import *;from os import chdir;import pylab as p;from math import sqrt;from matplotlib.pyplot import *;import pandas as pd
from scipy.signal import butter, filtfilt;import sys;import scipy, pylab;from scipy import signal;from scipy.interpolate import interp1d
import numpy as np;from scipy import stats;from scipy.interpolate import UnivariateSpline;import copy; import time
from scipy.signal import medfilt; import re ; import pandas as pd
import pickle ; import subprocess


##################################
#FONCTION POUR ORDONNER LA LISTE DES FICHIERS EOS
##################################
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

## Check if string can be a number
def is_number(s):
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

## allow to find a specific string chain in str set
def containsAny(str, set):
    """Check whether 'str' contains ANY of the chars in 'set'"""
    return 1 in [c in str for c in set]

def containsAll(str, set):
    """Check whether 'str' contains ALL of the chars in 'set'"""
    return 0 not in [c in str for c in set]


def Sqr(a):
    return a*a

def Distance(x1,y1,x2,y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)
 
def moyenne(tableau):
    return sum(tableau, 0.0) / len(tableau)   

def variance(tableau):
    m=moyenne(tableau)
    return moyenne([(x-m)**2 for x in tableau])


def ecartype(tableau):
    return variance(tableau)**0.5
                
            
     

def stft(x, fs, framesz, hop):
    framesamp = int(framesz*fs)
    hopsamp = int(hop*fs)
    w = scipy.hamming(framesamp)
    X = scipy.array([scipy.fft(w*x[i:i+framesamp]) 
                    for i in range(0, len(x)-framesamp, hopsamp)])
    return X

def istft(X, fs, T, hop):
    x = scipy.zeros(T*fs)
    framesamp = X.shape[1]
    hopsamp = int(hop*fs)
    for n,i in enumerate(range(0, len(x)-framesamp, hopsamp)):
        x[i:i+framesamp] += scipy.real(scipy.ifft(X[n]))
    return x  

sys.setrecursionlimit(100000)    
def moyenne_mobile_impaire(y,k):
    def mobile(y,k,n):
        if n + k//2 >= len(y):
            return []
        else:
            return [sum(y[n - k//2 : n + 1 + k//2]) / k] + mobile(y,k,n + 1)
    return list(repeat(None,k//2)) + mobile(y,k,k//2)  

### LOWPASS FILTER ###
def lowpass(data,samprate,cutoff): 
      b,a = butter(2,(cutoff)/(samprate/2.0),btype='low',analog=0,output='ba')
      data_f = filtfilt(b,a,data)
      return data_f
  

def moving_average(x, window):
    """Moving average of 'x' with window size 'window'."""
    y = np.empty(len(x)-window+1)
    for i in range(len(y)):
        y[i] = np.sum(x[i:i+window])/window
    return y

def qqqmean(num):
    return sqrt(nansum([n*n for n in num])/len(num))



def moving_averageV1(x, window):
    """Moving average of 'x' with window size 'window'."""
    y = np.empty(len(x)-window+1)
    for i in range(len(y)):
        y[i] = np.sum(x[i:i+window])/window
    return y

def moving_averageV2(x, window):
    """Moving average of 'x' with window size 'window'."""
    xsum = np.cumsum(x)
    xsum[window:] = xsum[window:] - xsum[:-window]
    return xsum[window-1:]/window

def moving_averageV3(x, window):
    """Moving average of 'x' with window size 'window'."""
    return np.convolve(x, np.ones(window)/window, 'same')

from scipy.signal import lfilter

def moving_averageV4(x, window):
    """Moving average of 'x' with window size 'window'."""
    return lfilter(np.ones(window)/window, 1, x)

def sliding_mean(data_array, window=5):  
    data_array = array(data_array)  
    new_list = []  
    for i in range(len(data_array)):  
        indices = range(max(i - window + 1, 0),  
                        min(i + window + 1, len(data_array)))  
        avg = 0  
        for j in indices:  
            avg += data_array[j]  
        avg /= float(len(indices))  
        new_list.append(avg)  
          
    return array(new_list)  

def nan_helper(y):
    """Helper to handle indices and logical indices of NaNs.

    Input:
        - y, 1d numpy array with possible NaNs
    Output:
        - nans, logical indices of NaNs
        - index, a function, with signature indices= index(logical_indices),
          to convert logical indices of NaNs to 'equivalent' indices
    Example:
        >>> # linear interpolation of NaNs
        >>> nans, x= nan_helper(y)
        >>> y[nans]= np.interp(x(nans), x(~nans), y[~nans])
    """

    return np.isnan(y), lambda z: z.nonzero()[0]
### Convert Cm in Deg // A REFAIRE
#def CmtoDeg(D,L,pxl):
#        """
#        D = distance mesurée sur écran
#        L = Distance Oeil - Ecran
#        pxl = Nb pixels
#        """
#        global Dcm,T
#        Dcm = D*pxl
#        T = (2*arctan(Dcm/(2*L)))*57.3
#        print (u"%s cm font %s en degrée d'angle" %(Dcm,T))

# =============================================================================
# ## FILTER
# =============================================================================
def lowpass(data,samprate,cutoff):
  b,a = butter(2,cutoff/(samprate/2.0),btype='low',analog=0,output='ba')
  data_f = filtfilt(b,a,data)
  return data_f


def s_g(y, window_size, order, deriv=0, rate=1):
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

# =============================================================================
# ############################################################################################
# =============================================================================
    
## CHECK AND CONVERT EDF TO ASC
def checkasc(m,n):     
        cmd = 'C:\\Users\\A.P\\Desktop\\Arthur\\Tools_EYELINK\\edf2asc.exe'
        os.chdir(datpath + "L%s\\S%s\\"%(m,n))
        dir1 = os.path.dirname(datpath + "L%s\\S%s\\"%(m,n))
        for root,dirs,files in os.walk(dir1):
           for file in sorted(files):
               if file.endswith(".edf"):
                       ascfile = file[:-3]+"asc"
                       if not os.path.isfile(ascfile) : #and not file.endswith(".asc"):
                           subprocess.run([cmd, file]) #shell = True, check = True)
#                           subprocess.Popen([cmd,file])
                           
  ## GET RAW DATA
def sub_cut(m,n):
        """ This function allows us to get all the namefiles ending with the extension .eos and .asc.
        In order to get the time onset and the offset timestamps in each eos files and use it to slice the ascii files. These timestamps are stored in 
        "index" dictionnary : column 3 : beginning of the game // column 4 : end of the game """
        global ajfile,allaj, eosall,ajall,index,elfile
        
        #        m = 7 ; n = 2 ;
        ajfile= list() ; allaj = {}
        os.chdir(datpath + "L%s\\S%s\\"%(m,n))
        dir1 = os.path.dirname(datpath + "L%s\\S%s\\"%(m,n))
        for root,dirs,files in os.walk(dir1):
            for file in sorted(files):
                if file.endswith(".eos"):
                    print(os.path.join(root,file))
                    ajfile.append(file)
                    ajfile.sort(key=natural_keys)
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
            

def sub_cut_LT(m,n,col):
        """ This function allows us to get all the namefiles ending with the extension .eos and .asc.
        In order to get the time onset and the offset timestamps in each eos files and use it to slice the ascii files. These timestamps are stored in 
        "index" dictionnary : column 3 : beginning of the game // column 4 : end of the game """
        global ajfile,allaj, eosall,ajall,index,ltfile
#        m = 7 ; n = 2 ;
        ajfile= list() ; allaj = {}
        os.chdir(datpath + "L%s\\S%s_L0\\"%(m,n))
        dir1 = os.path.dirname(datpath + "L%s\\S%s_L0\\"%(m,n))
        for root,dirs,files in os.walk(dir1):
            for file in files:
                if file.endswith(".eos"):
                    print(os.path.join(root,file))
                    ajfile.append(file)
                    ajfile.sort(key=natural_keys)
        #        if file.endswith(".ltd"):
                if file.endswith(".ltd"):
                    print(os.path.join(root,file))
                    ltfile = os.path.join(root,file)  
            global tab1,o1,row,data,l,aj,index
            import codecs


###################
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
                    
#            
            index = {}
            for i in range (0,len(ajall)):
                for j in range(0,len(ajall[ajfile[i]])-1):
                    if len(ajall[ajfile[i]][j]) == 5:    
                        index[ajfile[i]]= [ajall[ajfile[i]][j][1],ajall[ajfile[i]][j+1][1],int(ajall[ajfile[i]][j+1][2]),int(ajall[ajfile[i]][j+4][col]),int(ajall[ajfile[i]][-2][col])]
    
##        
#            index = {}
#            for i in range (0,len(ajall)):
#                for j in range(0,len(ajall[ajfile[i]])-1):
#                    if len(ajall[ajfile[i]][j]) == 5:    
#                        index[ajfile[i]]= [ajall[ajfile[i]][j][1],ajall[ajfile[i]][j+1][1],int(ajall[ajfile[i]][j+1][2]),int(ajall[ajfile[i]][j+3][15]),int(ajall[ajfile[i]][-2][15])]
#    
    

###################
# =============================================================================
# #GET DATA FICHIER EOS // TIMESTAMP MENU FIN
# =============================================================================
###################
# =============================================================================
# ## GET DATA LIVETRACK
# =============================================================================
def get_etdata(m,n):
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
            if is_number(tmt[i]) == True :
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
                
#        except NameError:
#                        ## information fichier EOS / get timestamp début / fin // Slice in ASCII file 
#                menus_ind = {}
#                
#                for i in range (0,len(ajfile)):
#                    menus_ind[ajfile[i]] = [index[ajfile[i]][3],index[ajfile[i]][4]]## index de la timeline ASCII de début et de fin pour chaque menu 
#                                                   
#                with open(ltfile,"rt") as ltf:
#                    data= csv.reader(ltf,delimiter=' ') ##pour symboliser des colonnes delimiter = ";"
#                    tabo3=list(data)       
#                
#                taboo = tabo3[2:]
#                for i in range (2,len(taboo)):
#                    while '' in taboo[i]:
#                        taboo[i].remove('')
#                    
#                O3 = list()
#                for i in range(0,len(taboo)-2): ## recupere les colonnes de data
#                    O3.append(taboo[i])
#                    
#                O1 = list() ; O2 = list() ; tmt = list()
#                for i in range (0,len(O3)): ## Reduire aux coordonnées x,y et pupille (colonnes 1,2,3 respectivement)
#                    O1.append(O3[i][3:6])
#                    O2.append(O3[i][10:13])
#                    tmt.append(O3[i][0][:])
#                    
#                ## List to get information from OEIL1 et OEIL2
#                EX1 = list() ## coordonnée en x
#                EY1= list() ## coordonnée en y
#                PUP1 = list() ## pupille
#                EX2 = list()
#                EY2 = list()
#                PUP2 = list()
#                timeline = list()
#                recap=list()
#                
#                ## get OEIL 1    
#                for i in range(2,len(O1)):   
#                    EX1.append(float(O1[i][0]))
#                    EY1.append(float(O1[i][1]))
#                    PUP1.append(float(O1[i][2]))
#                
#                ## transform in array
#                EX1 = np.array(EX1)
#                EY1 = np.array(EY1)
#                PUP1 = np.array(PUP1)
#                
#                
#                # get OEIL 2
#                for i in range(2,len(O2)):
#                    EX2.append(float(O2[i][0]))
#                    EY2.append(float(O2[i][1]))
#                    PUP2.append(float(O2[i][2]))
#                
#                ## transform in array
#                EX2 = np.array(EX2)
#                EY2 = np.array(EY2)
#                PUP2 = np.array(PUP2)
#                ###################
#                ###################
#                ## timestamp
#                tmt1 = list()
#                for i in range(0,len(tmt)):
#                    if is_number(tmt[i]) == True :
#                        tmt1.append(int(tmt[i]))
#                    
#                tmt1 = np.array(tmt1)
#                TMT = np.transpose(tmt1)
#                
#                ## Transpose
#                EX1 = np.transpose(EX1)
#                EY1 = np.transpose(EY1)
#                PUP1 = np.transpose(PUP1)
#                EX2 = np.transpose(EX2)
#                EXY2 = np.transpose(EY2)
#                PUP2 = np.transpose(PUP2)
#                
#                duration_sec = (TMT[0]*0.002)/60
#                ## get dataEL par menu
#                MM1, MM2 = {},{}
#                for i in range (0,len(ajfile)):
#                    MM1[ajfile[i]] = [EX1[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],EY1[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],PUP1[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],TMT[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]]] ## EYE1
#                    MM2[ajfile[i]] = [EX2[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],EY2[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],PUP2[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],TMT[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]]] ## EYE1
#        
#        
#                #colors = cm.rainbow(np.linspace(0, 1, y[1]))
#                #listla = ["]
#                namenu = ["Sujet %s \n"%(n)]
#                for i in range (0,len(ajfile)):
#                    namenu.append("Game %s: "%(i+1) + ajfile[i]+ ' \n')   
#                nmenu = ''.join(namenu)

# =============================================================================
# PLOT
# =============================================================================

#y = np.linspace(0,len(MM1[ajfile[i]][0])),len(MM1[ajfile[i]][0])
#colors = [str(item/255.) for item in y]
def games_plot():
        import time
        k = 0 ; m=0.1
        plt.figure(figsize = (24,10),dpi=100)
        for i in range (0,len(ajfile)):
            textstr = " Game %s"%(i+1)
            plt.subplot(6,6,k+1)    
            plt.scatter(MM1[ajfile[i]][0],MM1[ajfile[i]][1],s=1,color="b", marker='o',alpha =.2,lw=0)
            plt.scatter(MM2[ajfile[i]][0],MM1[ajfile[i]][1],s=1,color="r", marker='o',alpha =.2,lw=0)
            plt.text(400,-50,textstr,fontweight ='bold')
            plt.xlim(0,1024)
            plt.ylim(768,0)
            plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.060, right=0.75,wspace = 0.220, hspace=0.355)
            k+=1;m+=5
        #plt.subplots_adjust( top = 0.930, bottom = 0.060 , left = 0.125, right=0.75,wspace = 0.220, hspace=0.355)
        plt.text(2750,-2500,nmenu, va="center",fontsize=14)
        #plt.annotate(str(namenu), xy = (6500,-3000),xytext=(6500,-3000))
        plt.subplot(6,6,k+1)
        plt.xticks([])
        plt.yticks([])
        plt.xlabel("Eye on x in pixels",fontweight = "bold")
        plt.ylabel("Eye on y in pixels",fontweight = "bold")
        manager = plt.get_current_fig_manager()
        manager.window.showMaximized()
        time.sleep(2)
        plt.savefig("game_LT_S%s"%(n), dpi=100, facecolor='w', edgecolor='w',orientation='landscape')
        
        

## FIRST ORDER FUNCTION
def getpxlposition():
        """
        Get dataEL par menu // en PIXEL pour les positions // MM1[X][0] = poistion en x de l'oeil1  // MM1[X][1] = poistion en y de l'oeil1
        MM1[X][2] = dynamique pupille de l'oeil1 // same structure for MM2 for oeil2 
        """
        global MM1,MM2
        MM1, MM2 = {},{}
        for i in range (0,len(ajfile)):
            MM1[ajfile[i]] = [EX1[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],EY1[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],PUP1[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],TMT[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]]] ## EYE1
            MM2[ajfile[i]] = [EX2[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],EY2[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],PUP2[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]],TMT[np.where(menus_ind[ajfile[i]][0] == TMT)[0][0]:np.where(menus_ind[ajfile[i]][1] == TMT)[0][0]]] ## EYE1


def convpxltodeg(dis,c,win,order,deriv):
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
                MDEG1[ajfile[i]] = [(s_g(MM1[ajfile[i]][0],win,order,deriv)*tpx)/factdis,(s_g(MM1[ajfile[i]][1],win,order,deriv)*tpy)/factdis,MM1[ajfile[i]][2],MM1[ajfile[i]][3]]
                MDEG2[ajfile[i]] = [(s_g(MM2[ajfile[i]][0],win,order,deriv)*tpx)/factdis,(s_g(MM2[ajfile[i]][1],win,order,deriv)*tpy)/factdis,MM2[ajfile[i]][2],MM2[ajfile[i]][3]]
                
#                MDEG1[ajfile[i]] = [(MM1[ajfile[i]][0]*tpx)/factdis,(MM1[ajfile[i]][1]*tpy)/factdis,MM1[ajfile[i]][2],MM1[ajfile[i]][3]]
#                MDEG2[ajfile[i]] = [(MM2[ajfile[i]][0]*tpx)/factdis,(MM2[ajfile[i]][1]*tpy)/factdis,MM2[ajfile[i]][2],MM2[ajfile[i]][3]]

def degtovel(sr):
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
                
def veltoacc(sr):
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
                
def rectime(sr):
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
                
    
def inflab():
        global ilab
        clabo = ["Institut de la Vision","ICM","GIBSA","IMPACT","Inférence et Comportements Visuels","Perception et Sensori-Motricité","Perception et Attention","Vision Action Cognition","Psychologie de la Perception","SCAlab","Neuroergonomie"]
        llabo = ["Paris - 75012","Paris - 75013","Grenoble - 38185","Lyon - 69123","Marseille - 13055","Grenoble - 38185", "Marseille - 13055", "Boulogne Billancourt - 92012", "Paris - 75006", "Lille - 59350", "Toulouse - 31555"]
        rlabo = ["Jean Lorenceau", "Pierre Pouget", "Nathalie Guyader", "Denis Pelisson", "Anna Montagnini", "Carole Peyrin", "Françoise Vitu", "Céline Paeye", "Thérèse Collins", "Laurent Madelain", "Vsevolod Peysakhovich"]

        for p in range (0,len(m)):
                ilab = [clabo[m[p]],llabo[m[p]],rlabo[m[p]]]             
                


#def readcs(): ## fonction qui a pour but de récupérer les données liées à la lecture de la consigne d'un jeu.
        
# =============================================================================
# A FINIR
# =============================================================================


def gnames():
        """ 
        renomme name file 
        """
        global names, spl,spl1, nam
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
        names.sort(key=natural_keys)

        for i in range (0,len(names)):
                nam.append(names[i].split("_")[1])
                