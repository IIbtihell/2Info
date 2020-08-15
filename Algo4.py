from tkinter import*
from random import randint

print('Début Devinette')

C=randint(0,100)
score=0
while score<8:
    N= int(input("Donnez la valeur choisi par l'ordinateur"))
    if  N>C  :
        print("Votre choix > la valeur de l'ordinateur")
    if  N>C and C-N<=8 and C-N>=0 :
        print("Votre choix > la valeur de l'ordinateur")
        Score=Score+1
    elif N>C and C-N<=8 and C-N>=0 :
        print("Votre choix < la valeur de l'ordinateur")
        Score=Score+1
    elif N<C :
        print("Votre choix < la valeur de l'ordinateur")
    elif N==C :
        print("T.bien votre choix = la valeur de l'Ordinateur")
       
   
print("Réssayer une autre fois")
print("Le choix de l'ordinateur est : ", C)
print('Fin Devinette')
