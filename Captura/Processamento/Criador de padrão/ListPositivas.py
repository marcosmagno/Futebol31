'''
Created on 11 de jul de 2018

@author: fcrocha
'''
import urllib

import numpy as np

import cv2

import os


for file_type in ['positivas']:

    for img in os.listdir(file_type):

        if file_type == 'positivas':

            line = file_type+'/'+img+'\n'

            with open('bg2.txt','a') as f:

                f.write(line)

        elif file_type == 'negativas':

            line = file_type+'/'+img+' 1 0 0 150 150\n'

            with open('info.dat','a') as f:

                f.write(line)
                
                
                
                