#!/usr/bin/env python
# coding: utf-8

# In[111]:


import  matplotlib.pyplot as plt
import math
from random import randrange
#programme principal de recherche de points critiques


def vecteurSuivant(s,v):
    # s représente le pas qui a été fixé
    v[0]= v[0]-(s*v[0])
    v[1]= v[1]-(7*s*v[1])
    return v

def imageF(v):
    f =((pow(v[0],2)+(7*pow(v[1],2)))*0.5)
    return f
def norm(v):
    return math.sqrt((v[0]**2) + (v[1]**2))
def pasFixe(s,p):
    #p désigne la précision 
    Y=[[7],[1.5]]
    x=7
    y=1.5
    i=1
    while norm([x,y])> p   and abs((imageF(vecteurSuivant(s,[x,y]))/imageF([x,y]))-1)> p :
        x=vecteurSuivant(s,[x,y])[0]
        y=vecteurSuivant(s,[x,y])[1]
        Y[0].append(x)
        Y[1].append(y)
        i+=1
    return Y,i

def pasOptimal(p):
    #p désigne la précision 
    Y=[[7],[1.5]]
    x=7
    y=1.5
    i=1
    s=((x**2) +(49*(y**2)))/((x**2) +(343*(y**2)))
    while norm([x,y])> p   and abs((imageF(vecteurSuivant(s,[x,y]))/imageF([x,y]))-1)> p :
        x=vecteurSuivant(s,[x,y])[0]
        y=vecteurSuivant(s,[x,y])[1]
        Y[0].append(x)
        Y[1].append(y)
        i+=1
        s=((x**2) +(49*(y**2)))/((x**2) +(343*(y**2)))
    return Y,i

if __name__=="__main__":
    Y1,i1=pasFixe(0.01,10**(-5))
    plt.plot(Y1[0],Y1[1],'+-',label='0.01 fix iter')
    Y2,i2=pasFixe(0.25,10**(-5))
    plt.plot(Y2[0],Y2[1],'+-')
    Y3,i3=pasOptimal(10**(-5))
    plt.plot(Y3[0],Y3[1],'+-')

