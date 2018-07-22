# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:50:35 2018
EyeLink Data File converter. Same process than edf2asc.exe (called)
Function is able to go through a folder, scan all files within, and if an edf file is present, convert edf to asc 
If ascfile does not already exist the function is executed, if not it stops.
For my specific case, m matches with the number of name folder, n 
@author: A.P
"""

def checkasc(m,n):     
        cmd = path + "\edf2asc.exe" ## path and call of edf2asc.exe 
        os.chdir(pathfolder+filename ) ## folder + file path - type str
        dir1 = os.path.dirname(pathfolder+filename) ## file path - type str
        for root,dirs,files in os.walk(dir1):
           for file in sorted(files):
               if file.endswith(".edf"): ## ☻check edf 
                       ascfile = file[:-3]+"asc" ## create ascfile name
                       if not os.path.isfile(ascfile) : ## check if ascfile already exists
                           subprocess.run([cmd, file]) ## if not execute and convert edftoasc
#                           subprocess.Popen([cmd,file])
