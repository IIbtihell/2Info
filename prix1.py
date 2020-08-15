print("-1-flash USB: 12000")
print("-2-Sousris sans fil: 14000")
print("-3-Micro-Casque: 8000")
print("-4-Imprimente sharp: 550000")
print("-5-Clavier FR-AR: 7000")
print("-6-Power Bank: 55000")
montant=0
choix=0
while choix

from tkinter import *

def calculer():
    contenu1=int(e1.get())
    contenu2=int(e2.get())
    montant=contenu1*contenu2
    b.config(command=calculer)
    res.config (text='RÃ©sultat ='+str(montant) ,fg='pink' )

    
fen1=Tk()
txt1=Label(fen1,text ='Nom et prénom :')
txt2=Label(fen1,text ='G.S.M  :')
txt3=Label(fen1,text ='Adresse  :')
txt4=Label(fen1,text ='Choix :')
txt5=Label(fen1,text ='Prix unitaire :')
txt6=Label(fen1,text ='Qauntité :')

e1=Entry(fen1)
e2=Entry(fen1)
e3=Entry(fen1)
e4=Entry(fen1)
e5=Entry(fen1)
e6=Entry(fen1)

txt1.grid(row=0)
txt2.grid(row=1)
txt3.grid(row=2)
txt4.grid(row=3)
txt5.grid(row=4)
txt6.grid(row=5)
e1.grid(row=0,   column=1)

e2.grid(row=1,   column=1)

e3.grid(row=2,   column=1)

e4.grid(row=3,   column=2)

e5.grid(row=4,   column=2)

e6.grid(row=5,   column=2)




b=Button(fen1,    text='Calculer',command=calculer)
b.grid(row=2)

res=Label(fen1,text='monatnt')
res.grid(row=3)




fen1.mainloop()

