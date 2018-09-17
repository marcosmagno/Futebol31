'''
Created on 10 de jul de 2018

@author: fcrocha
'''
import urllib

import numpy as np

import cv2

import os

link_imagens_positivas ='http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02121808'  
urls_imagens_positivas = urllib.urlopen(link_imagens_positivas).read().decode("utf8")

numero_imagem = 0
if not os.path.exists('positivas'):

    os.makedirs('positivas')


    numero_imagem = 1


for i in urls_imagens_positivas.splitlines():

    try:

        print(i)

        urllib.urlretrieve(i, "positivas/"+str(numero_imagem)+".jpg")

        img = cv2.imread("positivas/"+str(numero_imagem)+".jpg",cv2.IMREAD_GRAYSCALE)

        imagem_redimensionada = cv2.resize(img, (50,50))

        cv2.imwrite("positivas/"+str(numero_imagem)+".jpg",imagem_redimensionada)

        numero_imagem += 1
        
    except Exception as e:

            print(str(e))