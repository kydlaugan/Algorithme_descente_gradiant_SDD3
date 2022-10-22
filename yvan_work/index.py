import numpy as np
import matplotlib.pyplot as plt
import math
#declaration de la fonction de depart
f_x_y = lambda x , y : (1/2)*(x**2 )+ (7/2)*(y**2)

#calcul du gradiant de la fonction
def gradient_f_x_y(x , y) :
   return  x , 7*y ;
#algorithme de descente a pas fixe 

def pas_fixe(s) :
    
    #initialisation des paramètre
    iter_max = 1000
    tolerence = 10**(-5)
    i = 0
    x0 = 7
    y0 = 1.5
    abscis = []
    ordone = []
    
    # calcul du gradient suivant X et Y en un point précis
    gradient_x ,gradient_y = gradient_f_x_y(x0 , y0)
    # calcul de la norme du gradient suivant X et Y en ce point précis
    norm_gradient = math.sqrt(gradient_x**2 + gradient_y**2) 
    while(abs(norm_gradient) > tolerence):
        #calcul des coordonnées du point X de i+1
        x0 = x0 - s*gradient_x 
        y0 = y0 - s*gradient_y
        # on stocke les coordonnées de ce point dans deux vecteurs différents
        abscis.append(x0)
        ordone.append(y0)
         # calcul du gradient suivant X et Y en un point précis
        gradient_x ,gradient_y = gradient_f_x_y(x0 , y0)
        norm_gradient = math.sqrt(gradient_x**2 + gradient_y**2) # norme du gradient 
       
        i += 1
        if i > iter_max:
            return None 
    return abscis ,ordone

def pas_optimal() :
    
    #initialisation des paramètre
    iter_max = 1000
    tolerence = 10**(-5)
    i = 0
    x0 = 7
    y0 = 1.5
    abscis = []
    ordone = []
    
    # calcul du gradient suivant X et Y en un point précis
    gradient_x ,gradient_y = gradient_f_x_y(x0 , y0)
    # calcul de la norme du gradient suivant X et Y en ce point précis
    norm_gradient = math.sqrt(gradient_x**2 + gradient_y**2) 
    while(abs(norm_gradient) > tolerence):
        #calcul des coordonnées du point X de i+1 et le pas_optimal s
        s = (x0**2 + 49*(y0**2))/( x0**2 + 343*(y0**2))
        x0 = x0 - s*gradient_x 
        y0 = y0 - s*gradient_y
        # on stocke les coordonnées de ce point dans deux vecteurs différents
        abscis.append(x0)
        ordone.append(y0)
         # calcul du gradient suivant X et Y en un point précis
        gradient_x ,gradient_y = gradient_f_x_y(x0 , y0)
        norm_gradient = math.sqrt(gradient_x**2 + gradient_y**2) # norme du gradient 
        i += 1
        if i > iter_max:
            return None 
    return abscis ,ordone


if __name__ == "__main__":
    points_abscisse_1 , points_ordonnée_1 = pas_fixe(0.25)
    points_abscisse_2 , points_ordonnée_2 = pas_fixe(0.125)
    points_abscisse_3 , points_ordonnée_3 = pas_optimal()
    
    #on trace la courbe pour le pas = 0.25
    X , Y = np.meshgrid(points_abscisse_1 , points_ordonnée_1)
    Z = (1/2)*(X**2) + (7/2)*(Y**2)
    plt.plot(points_abscisse_1 ,points_ordonnée_1 ,'k+--') 
    
    #on trace la courbe pour le pas = 0.125
    X , Y = np.meshgrid(points_abscisse_2 , points_ordonnée_2)
    Z = (1/2)*(X**2) + (7/2)*(Y**2)
    plt.plot( points_abscisse_2 ,points_ordonnée_2 ,'+-',color = 'blue') 
    
     #on trace la courbe grace au pas optimal calculé à chaque fois
    X , Y = np.meshgrid(points_abscisse_3 , points_ordonnée_3)
    Z = (1/2)*(X**2) + (7/2)*(Y**2)
    plt.plot( points_abscisse_3 ,points_ordonnée_3 ,'+-' , color = 'red') 
    
     #on place le point critique sur la courbe
    plt.plot(points_abscisse_1[-1] , points_ordonnée_1[-1] ,color = 'green', marker = "o")
