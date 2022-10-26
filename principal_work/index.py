import numpy as np
import matplotlib.pyplot as plt
import math
#declaration de la fonction de depart
f_x_y = lambda x , y : 0.5*(x**2)+ (3.5)*(y**2)

#calcul du gradiant de la fonction
def gradient_f_x_y(x , y ) :
   return  x , 7*y 

def point_suivant(x , y , s) :
    gradient_x ,gradient_y = gradient_f_x_y(x , y)
    return x - s*gradient_x , y - s*gradient_y
#algorithme de descente a pas fixe 


def pas_fixe(s) :
    
    #initialisation des paramètre
    tolerence = 10**(-5)
    i = 0
    x0 = 7
    y0 = 1.5
    abscis = [x0]
    ordone = [y0]
    x,y = point_suivant(x0 , y0 , s)
    # calcul du gradient suivant X et Y en un point précis
    gradient_x ,gradient_y = gradient_f_x_y(x, y)
    # calcul de la norme du gradient suivant X et Y en ce point précis
    norm_gradient = math.sqrt(gradient_x**2 + gradient_y**2) 
    while norm_gradient > tolerence and abs((f_x_y(x,y) - f_x_y(abscis[i] , ordone[i])))/ abs(f_x_y(abscis[i] , ordone[i])) > tolerence :
        abscis.append(x)
        ordone.append(y)
        x  , y = point_suivant(x ,y , s)
        gradient_x ,gradient_y = gradient_f_x_y(x, y)
        norm_gradient = math.sqrt(gradient_x**2 + gradient_y**2) # norme du gradient 
        i += 1

    return abscis ,ordone ,i

def pas_optimal() :
    
    #initialisation des paramètre
    tolerence = 10**(-5)
    i = 0
    x0 = 7
    y0 = 1.5
    abscis = [x0]
    ordone = [y0]
    s = (x0**2 + 49*(y0**2))/( x0**2 + 343*(y0**2))
    x,y = point_suivant(x0 , y0 , s)
    # calcul du gradient suivant X et Y en un point précis
    gradient_x ,gradient_y = gradient_f_x_y(x0 , y0)
    # calcul de la norme du gradient suivant X et Y en ce point précis
    norm_gradient = math.sqrt(gradient_x**2 + gradient_y**2) 
    while norm_gradient > tolerence and abs(f_x_y(x,y) - f_x_y(abscis[i] , ordone[i]))/abs((f_x_y(abscis[i] , ordone[i]))) > tolerence :
        abscis.append(x)
        ordone.append(y)
         # calcul du gradient suivant X et Y en un point précis
        gradient_x ,gradient_y = gradient_f_x_y(x , y)
        norm_gradient = math.sqrt(gradient_x**2 + gradient_y**2) # norme du gradient 
        s = (x**2 + 49*(y**2))/( x**2 + 343*(y**2))
        x  , y = point_suivant(x ,y , s)
        i += 1
    return abscis ,ordone ,i


if __name__ == "__main__":
    
    pas_1 = 0.25
    pas_2 = 0.01
    points_abscisse_1 , points_ordonnée_1  , i1 = pas_fixe(pas_1)
    points_abscisse_2 , points_ordonnée_2  , i2 = pas_fixe(pas_2)
    points_abscisse_3 , points_ordonnée_3  , i3 = pas_optimal()
    
    #on trace la courbe avec le second pas
    plt.figure(figsize=(14,4))
    plt.plot(points_abscisse_1 ,points_ordonnée_1 ,'k*--',label= f'pas fixe de {pas_1} avec {i1} itérations') 
    #on trace la courbe avec le premier pas
    plt.plot( points_abscisse_2 ,points_ordonnée_2 ,'+:',color = 'blue' ,label= f'pas fixe de {pas_2} avec  {i2} itérations') 
    
     #on trace la courbe grace au pas optimal calculé à chaque fois
    plt.plot( points_abscisse_3 ,points_ordonnée_3 ,'x-' , color = 'red', label= f'pas optimal avec {i3} itérations ') 
    
     #on place le point critique sur la courbe
    plt.plot(points_abscisse_1[-1] , points_ordonnée_1[-1] ,color = 'green', marker = "o" , label ='point de minimun local')
    plt.legend()

