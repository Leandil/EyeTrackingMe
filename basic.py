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
from scipy.signal import medfilt; import re



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


def convpxltodeg(dis,hs,vs):
        """
        Function pixel to angular degree (pour une distance oeil écran de 1000 mm ):
        dis = distance Oeil/Ecran en cm ; 
        hs = taille horizontale de l'écran en cm ; vs = taille verticale de l'écran en cm 
        Facdis = ref distance O/Screen = 57 cm --> 1 cm == 1°
        Taille H pixel sur dispositif LiveTrack avec écran BenQ XL2411 pour une résolution 1024*768 = 0.0521 cm 
        Taille V pixel sur dispositif LiveTrack avec écran BenQ XL2411 pour une résolution 1024*768 = 0.0390 cm 
        """
        global MDEG1,MDEG2
        MDEG1 = {} ; MDEG2 =  {}
        ## variables setup :
        factdis = (dis / 57.0) ##◘ facteur de correspondance distance oeil/ecran pour 1° = x cm sur l'écran
        tpx = hs/1024.0 ; tpy = vs/1024.0
        for i in range (0,len(ajfile)):
                MDEG1[ajfile[i]] = [(MM1[ajfile[i]][0]*tpx)/factdis,(MM1[ajfile[i]][1]*tpy)/factdis,MM1[ajfile[i]][2],MM1[ajfile[i]][3]]
                MDEG2[ajfile[i]] = [(MM2[ajfile[i]][0]*tpx)/factdis,(MM2[ajfile[i]][1]*tpy)/factdis,MM2[ajfile[i]][2],MM2[ajfile[i]][3]]

def degtovel(sr,lowfi):
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
                                mvela.append(abs((a[k+1]-a[k])/ufs))
                                mvelb.append(abs((b[k+1]-b[k])/ufs))
                if MDEG2[ajfile[i]][0] != []:
                        aa = MDEG2[ajfile[i]][0]
                        bb = MDEG2[ajfile[i]][1]
                        for k in range (0,len(a)-1):
                                mvelaa.append(abs((aa[k+1]-aa[k])/ufs))
                                mvelbb.append(abs((bb[k+1]-bb[k])/ufs))
                MVEL1[ajfile[i]] = [lowpass(mvela,sr,lowfi),lowpass(mvelb,sr,lowfi), MDEG1[ajfile[i]][2],MDEG1[ajfile[i]][3]]
                MVEL2[ajfile[i]] = [lowpass(mvelaa,sr,lowfi),lowpass(mvelbb,sr,lowfi),MDEG2[ajfile[i]][2],MDEG2[ajfile[i]][3]]
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
                MACC1[ajfile[i]] = [lowpass(macca,500,25),lowpass(maccb,500,25), MDEG1[ajfile[i]][2],MDEG1[ajfile[i]][3]]
                MACC2[ajfile[i]] = [lowpass(maccaa,500,25),lowpass(maccbb,500,25),MDEG2[ajfile[i]][2],MDEG2[ajfile[i]][3]]
                macca,maccb, maccaa, maccbb = [],[],[],[]