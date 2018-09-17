'''
Created on 11 de jul de 2018

@author: fcrocha
'''
import os

for i, f in enumerate(os.listdir(".")):

    f_new = '{}.jpg'.format(i)

    os.rename(f, f_new)

    print '{}.'.format(i), f, '->', f_new