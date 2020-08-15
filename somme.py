from Tkinter import*
import Tkinter as tk
fen1=Tk()
fen1.title('Somme')
txt1=Label(fen1,text='Saisir un nombre:', fg='purple')
e1=Entry(fen1)
txt1.grid(row=1)

e1.grid(row=1,   column=1)


b=Button(fen1,    text='Calculer')
b.grid(row=2)

res=Label(fen1,text='')
res.grid(row=3)




def fonction ():
    N=e1.get()
    s=0
    for i in (N):
         s=s+int(i)
     
    b.config(command=fonction)
    res.config(text='resultat= '+str(s),fg='green')
    

fonction()
fen1.mainloop()
