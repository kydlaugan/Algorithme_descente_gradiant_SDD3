import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
#declaration de la fonction de depart
f_x_y = lambda x , y : 0.5*(x**2)+ (3.5)*(y**2)

#calcul du gradiant de la fonction
def gradient_f_x_y(x , y ):
    return  x , 7*y ;

def point_suivant(x , y , s):
    gradient_x ,gradient_y = gradient_f_x_y(x , y)
    return x - s*gradient_x , y - s*gradient_y

def direction_newton( x ,y):
    return -x , -y   
def pas_fixe(s) :
    
    #initialisation des paramètre
    tolerence = 10**(-5)
    i = 1
    x0 = 7
    y0 = 1.5
    abscis = [x0]
    ordone = [y0]
    x,y = point_suivant(x0 , y0 , s)
    pas = [s]
    # calcul du gradient suivant X et Y en un point précis
    gradient_x ,gradient_y = gradient_f_x_y(x, y)
    # calcul de la norme du gradient suivant X et Y en ce point précis
    norm_gradient = math.sqrt(gradient_x**2 + gradient_y**2) 
    while norm_gradient > tolerence and abs((f_x_y(x,y) - f_x_y(abscis[i-1] , ordone[i-1])))/ abs(f_x_y(abscis[i-1] , ordone[i-1])) > tolerence :
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
    i = 1
    x0 = 7
    y0 = 1.5
    abscis = [x0]
    ordone = [y0]
    s = (x0**2 + 49*(y0**2))/( x0**2 + 343*(y0**2))
    pas   = [0]
    x,y = point_suivant(x0 , y0 , s)
    # calcul du gradient suivant X et Y en un point précis
    gradient_x ,gradient_y = gradient_f_x_y(x0 , y0)
    # calcul de la norme du gradient suivant X et Y en ce point précis
    norm_gradient = math.sqrt(gradient_x**2 + gradient_y**2) 
    while norm_gradient > tolerence and abs(f_x_y(x,y) - f_x_y(abscis[i-1] , ordone[i-1]))/abs((f_x_y(abscis[i-1] , ordone[i-1]))) > tolerence :
        abscis.append(x)
        ordone.append(y)
        pas.append(s)
         # calcul du gradient suivant X et Y en un point précis
        gradient_x ,gradient_y = gradient_f_x_y(x , y)
        norm_gradient = math.sqrt(gradient_x**2 + gradient_y**2) # norme du gradient 
        s = (x**2 + 49*(y**2))/( x**2 + 343*(y**2))
        x  , y = point_suivant(x ,y , s)
        i += 1
    return abscis ,ordone ,i ,pas


def newton_local() :
    
    #initialisation des paramètre
    tolerence = 10**(-5)
    i = 1
    x0 = 7
    y0 = 1.5
    abscis = [7]
    ordone = [1.5]
    dx ,dy = direction_newton(abscis[i-1] , ordone[i-1])
    x,y  = x0+dx , y0+dy
    # calcul du gradient suivant X et Y en un point précis
    gradient_x ,gradient_y = gradient_f_x_y(abscis[i-1] , ordone[i-1])
    # calcul de la norme du gradient suivant X et Y en ce point précis
    norm_gradient = math.sqrt(gradient_x**2 + gradient_y**2) 
    while norm_gradient > tolerence:
        abscis.append(x)
        ordone.append(y)
         # calcul du gradient suivant X et Y en un point précis
        gradient_x ,gradient_y = gradient_f_x_y(x , y)
        norm_gradient = math.sqrt(gradient_x**2 + gradient_y**2) # norme du gradient 
        dx ,dy = direction_newton(x,y)
        x,y  = x0+dx , y0+dy
        i += 1
    return abscis ,ordone ,i

if __name__ == "__main__":
    
    pas_1 = 0.25
    pas_2 = 0.01
    points_abscisse_1 , points_ordonnée_1  , i1 = pas_fixe(pas_1)
    points_abscisse_2 , points_ordonnée_2  , i2 = pas_fixe(pas_2)
    points_abscisse_3 , points_ordonnée_3  , i3 , pas_optimal = pas_optimal()
    points_abscisse_4 , points_ordonnée_4  , i4 = newton_local()
    
    #on trace la courbe avec le second pas
    plt.figure(figsize=(19,8))
    plt.plot(points_abscisse_1 ,points_ordonnée_1 ,'*--', color='magenta',label= f'pas fixe de {pas_1} avec {i1} itérations') 
    #on trace la courbe avec le premier pas
    plt.plot( points_abscisse_2 ,points_ordonnée_2 ,'+:',color = 'blue' ,label= f'pas fixe de {pas_2} avec  {i2} itérations') 
    
     #on trace la courbe grace au pas optimal calculé à chaque fois
    plt.plot( points_abscisse_3 ,points_ordonnée_3 ,'x-' , color = 'red', label= f'pas optimal avec {i3} itérations ') 
    plt.plot( points_abscisse_4 ,points_ordonnée_4 ,'D-.' , color = 'cyan', label= f' newton local avec {i4} itérations ') 
    
     #on place le point critique sur la courbe
    plt.plot(points_abscisse_1[-1] , points_ordonnée_1[-1] ,color = 'green', marker = "o" , label ='point de minimun local')
    
    X , Y = np.meshgrid( np.linspace(-2 , 7 ,1000) ,np.linspace(-2 , 2 ,1000))
    Z = f_x_y( X, Y)
    cs = plt.contour(X,Y,Z,np.logspace(-1,3.5,20,base=10))
    plt.legend()
    
    #tracée des tableaux
    i = 0
    j = 0
    k = 0
    n = 0
    liste_1_f = []
    liste_1_norm_f = []
    liste_2_f = []
    liste_2_norm_f = []
    liste_3_f = []
    liste_3_norm_f = []
    liste_4_f = []
    liste_4_norm_f = []
    
    #Tableau  récapitulatif de l`algorithme de descente  pour un pas fixe de 0.25
    while i < len(points_abscisse_1):
        f = 0.5*(points_abscisse_1[i]**2) + 3.5*(points_ordonnée_1[i]**2)
        gradient_x ,gradient_y = gradient_f_x_y(points_abscisse_1[i] , points_ordonnée_1[i])
        norm_f = math.sqrt(gradient_x**2 + gradient_y**2)
        liste_1_f.append(f)
        liste_1_norm_f.append(norm_f)
        i += 1  
        
    #Tableau  récapitulatif de l`algorithme de descente  pour un pas fixe de 0.01    
    while k < len(points_abscisse_2):
        f = 0.5*(points_abscisse_2[k]**2) + 3.5*(points_ordonnée_2[k]**2)
        gradient_x ,gradient_y = gradient_f_x_y(points_abscisse_2[k] , points_ordonnée_2[k])
        norm_f = math.sqrt(gradient_x**2 + gradient_y**2)
        liste_2_f.append(f)
        liste_2_norm_f.append(norm_f)
        k += 1  
        
    #Tableau  récapitulatif de l`algorithme de descente  à  pas  optimal    
    while j < len(points_abscisse_3):
        f = 0.5*(points_abscisse_3[j]**2) + 3.5*(points_ordonnée_3[j]**2)
        gradient_x ,gradient_y = gradient_f_x_y(points_abscisse_3[j] , points_ordonnée_3[j])
        norm_f = math.sqrt(gradient_x**2 + gradient_y**2)
        liste_3_f.append(f)
        liste_3_norm_f.append(norm_f)
        j += 1
        
    #Tableau  récapitulatif de l`algorithme  par la méthode de Newton local
    while n < len(points_abscisse_4):
        f = 0.5*(points_abscisse_4[n]**2) + 3.5*(points_ordonnée_4[n]**2)
        gradient_x ,gradient_y = gradient_f_x_y(points_abscisse_4[n] , points_ordonnée_4[n])
        norm_f = math.sqrt(gradient_x**2 + gradient_y**2)
        liste_4_f.append(f)
        liste_4_norm_f.append(norm_f)
        n += 1 
    #Tableau  récapitulatif de l`algorithme de descente  pour un pas fixe de 0.25
    tableau_1 = pd.DataFrame({ 'F(x,y)': liste_1_f,'||Vf(x,y)||': liste_1_norm_f,'Sk': pas_1,'Xk': points_abscisse_1, 'Yk': points_ordonnée_1})
    print('Tableau  récapitulatif de l`algorithme de descente  pour un pas fixe de 0.25 \n')
    print(tableau_1) 
    #Tableau  récapitulatif de l`algorithme de descente  pour un pas fixe de 0.01
    tableau_2 = pd.DataFrame({ 'F(x,y)': liste_2_f,'||Vf(x,y)||': liste_2_norm_f,'Sk': pas_2,'Xk': points_abscisse_2, 'Yk': points_ordonnée_2})
    print('\nTableau  récapitulatif de l`algorithme de descente  pour un pas fixe de 0.01 \n')
    print(tableau_2) 
    #Tableau  récapitulatif de l`algorithme  par la méthode de Newton local
    tableau_4 = pd.DataFrame({ 'F(x,y)': liste_4_f,'||Vf(x,y)||': liste_4_norm_f,'Sk': 1,'Xk': points_abscisse_4,'Yk': points_ordonnée_4})
    print('\nTableau  récapitulatif de l`algorithme  par la méthode de Newton locale\n')
    print(tableau_4)
