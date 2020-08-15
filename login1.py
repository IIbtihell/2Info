from tkinter import*
import tkinter as tk
from Tkinter import massagebox as mbox
txt1=Label(fen1,text ='Mot de passe:')
txt2=Label(fen1,text ='Login:')
e1=Entry(fen1,show="*")
e2=Entry(fen1)
txt1.grid(row=0)
txt2.grid(row=1)
e1.grid(row=0,   column=1)

e2.grid(row=1,   column=1)

b=Button(fen1,    text='valider')
b.grid(row=2)

res=Label(fen1,text='')
res.grid(row=3)


def valider ():
    contenu1=e1.get()
    contenu2=e2.get()
    b.config(command=valider)
if e1.get() == 'info1' and e2.get() == 'informatique1':
 mbox.showinfo('resultat ='+str('Authentification reussi'))
else :
 mbox.showerror('resultat ='+str('mot de passe incorrecte, veuillez ressayez'))


fen1.mainloop()

