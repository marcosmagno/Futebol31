'''
Created on 10 de jul de 2018

@author: fcrocha
'''
import urllib

import numpy as np

import cv2

import os

link_imagens_negativas ='http://image-net.org/api/text/imagenet.synset.geturls?wnid=n01317541'  
urls_imagens_negativas = urllib.urlopen(link_imagens_negativas).read().decode("utf8")

numero_imagem = 823
if not os.path.exists('negativas'):

    os.makedirs('negativas')
numero_imagem = 823

for i in urls_imagens_negativas.splitlines():

    try:

        print(i)

        urllib.urlretrieve(i, "negativas/"+str(numero_imagem)+".jpg")

        img = cv2.imread("negativas/"+str(numero_imagem)+".jpg",cv2.IMREAD_GRAYSCALE)

        imagem_redimensionada = cv2.resize(img, (100,100))

        cv2.imwrite("negativas/"+str(numero_imagem)+".jpg",imagem_redimensionada)

        numero_imagem += 1
        
    except Exception as e:

            print(str(e))